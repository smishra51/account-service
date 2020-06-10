from flask import request, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Account
from flask import jsonify


@app.route('/', methods=['GET'])
def healthcheck():
    return make_response(jsonify({"health": "ok"}), 200)


@app.route("/account", methods=['POST'])
def add():
    account: Account = request.json
    if account:
        existing_account = Account.query.filter(
            Account.name == account["name"] or Account.email == account["email"]).first()
        if existing_account:
            return make_response(jsonify({"username": account["name"]}), 409)
        newaccount = Account(name=account["name"],
                             email=account["email"],
                             created=dt.now(),
                             address=account["address"],
                             mobile=account["mobile"],
                             admin=False)
        db.session.add(newaccount)
        db.session.commit()
        return make_response(jsonify(data=[e.serialize() for e in Account.query.all()]), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/account", methods=['GET'])
def get():
    data = Account.query.all()
    if data:
        return make_response(jsonify(data=[e.serialize() for e in Account.query.all()]), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/account/<int:accountid>", methods=['GET'])
def findbyid(accountid):
    if accountid:
        account = Account.query.filter(Account.accountId == accountid).first()
        if account:
            return make_response(jsonify(data=account.serialize()), 200)
        return make_response(jsonify({"resp": "Not found"}), 404)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/account", methods=['PUT'])
def update():
    account: Account = request.json
    if account:
        existing_account: Account = Account.query.filter(Account.accountId == account["accountId"]).first()
        if not existing_account:
            return make_response(jsonify({"username": account["name"]}), 404)
        existing_account.name = account["name"]
        existing_account.admin = account["admin"]
        existing_account.email = account["email"]
        existing_account.mobile = account["mobile"]
        existing_account.address = account["address"]
        db.session.add(existing_account)
        db.session.commit()
        return make_response(jsonify(data=existing_account.serialize()), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/account", methods=['DELETE'])
def delete():
    account: Account = request.json
    if account:
        existing_account: Account = Account.query.filter(Account.accountId == account["accountId"]).first()
        if not existing_account:
            return make_response(jsonify({"accountId": account["accountId"]}), 404)
        db.session.delete(existing_account)
        db.session.commit()
        return make_response(jsonify({"resp": "Successfully deleted"}), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)
