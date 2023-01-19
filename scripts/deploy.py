from brownie import Sellable, accounts, network, config

def deploy():
   account = getAccount()

   print("Deploying...")
   
   network.gas_price("1.6 gwei")

   deploy = Sellable.deploy({"from": account}, publish_source=True)
   #deploy = Sellable.deploy({"from": account}, publish_source=False)


   print(f"Deployed at {deploy.address} !!!")

   title = "Odele Token"

   link = "https://mumbai.polygonscan.com/address/"
   with open("../Deployment Address.txt", "a+") as file:
      file.write(f"{title} => {link}{deploy.address}\n\n")


def getAccount():
   if network.show_active() == "development":
      return accounts[0]
   else:
      return accounts.add(config['wallet']['from_key'])

def main():
   deploy()