from brownie import accounts, reverts, T, config

def owner():
    return accounts[0]

def deploy():
    t = T.deploy({"from": owner()})
    return t

def test_fund():
    t = deploy()
    bal1 = owner().balance()

    with reverts():
        t.fund({"value": "10 ether", "from": owner()})
    
    t.fund({"value": "11 ether", "from": owner()})

    bal2 = owner().balance()

    assert bal1 - bal2 == "11 ether"
    assert bal2 == "989 ether"
