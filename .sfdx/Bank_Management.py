balance=0.0
kyc_docs ={}


def show():
    print(f"Your current balance is {balance}")
    print("============================")


def deposit (amount):
    global balance

    if amount > 0:
        balance+= amount
        print(f"Amount of {amount} Rs. is deposited")
        print("============================")

    else:
        print("amount cannot be negative")
        print("============================")


def withdraw (amount):

    global balance

    if amount > balance:
        print("Your balance is lower than entered amount")
        show()

    elif amount < 0:
        print("amount cannot be negative")
        print("============================")

    else:
        balance -= amount
        print(f"Amount of {amount} Rs. is withdrawn")
        print("============================")


def update_kyc(docs):
    global kyc_docs

    kyc_docs.update(docs)


def check_kyc():
    if len(kyc_docs) == 0:
        print("KYC not done")
        print("============================")
    else:
        for docs in kyc_docs:
            print(f"{docs} : {kyc_docs[docs]}")


if __name__=="__main__":
    print("============================")
    print("Welcome to Bank Management")
    print("============================")

    while True:
        print("1. Show Balance")
        print("2. Deposit Money ")
        print("3. Withdraw Money ")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Exit")
        print("============================")
        choice = input("Enter your choice(1-6):")
        print("============================")

        if choice == "1":
            show()

        elif choice == "2":
            amount = int(input("Enter amount to deposit:"))
            print("============================")
            deposit(amount)

        elif choice == "3":
            amount = int(input("Enter amount to withdraw:"))
            print("============================")
            withdraw(amount)

        elif choice == "4":
            check_kyc()

        elif choice == "5":
            kyc_documents={}
            n_documents=int(input("Enter the number of documents ypu want to add:"))

            for _ in range(n_documents):
                key = input("Enter the document type:")
                value = input("Enter the document number:")
                kyc_documents[key] = value

            update_kyc(kyc_documents)

            print("=============================")
            print("KYC updated successfully")
            print("=============================")

        elif choice == "6":
            print("=============================")
            print("You Quit")
            print("=============================")
            break

        else:
            print("=============================")
            print("Invalid Choice")
            print("=============================")

    print("Thank you for banking with us")
    print("============================")