# Create a BankAccount classi
class Bank_Account:
    MAX_TRANSACTION = 100000
    def __init__(self, withdrawal, deposit):
        if  withdrawal >= Bank_Account.MAX_TRANSACTION:
            self.withdrawal = withdrawal
        else:
            self.withdrawal = Bank_Account.MAX_TRANSACTION
        
        if deposit >= Bank_Account.MAX_TRANSACTION:
            self.deposit = deposit
        else:
            self.deposit = Bank_Account.MAX_TRANSACTION
        
client_1 = Bank_Account(50000, 380000)
client_2 = Bank_Account(173000, 292000)

print("Total transaction for client 1: ", client_1.MAX_TRANSACTION)     
print("Total transaction for client 2: ", client_2.MAX_TRANSACTION)

print("Client 1 proposed withdrawal: ", client_1.withdrawal)   
print("Client 2 proposed withdrawal: ", client_2.withdrawal) 
  
print("Client 1 proposed deposit: ", client_1.deposit)   
print("Client 2 proposed deposit: ", client_2.deposit) 

