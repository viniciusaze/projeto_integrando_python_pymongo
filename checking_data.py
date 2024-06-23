import pprint
import os
from time import sleep
import pymongo as pyM


def main():
    os.system('cls')
    print("View Documents in Atlas MongoDB:")
    password = input("Password: ")
    # Connecting
    client = pyM.MongoClient(f"mongodb+srv://ar-vinicius:{password}@cluster0.cx1y4t0.mongodb.net/"
                             f"?retryWrites=true&w=majority&appName=Cluster0")

    db = client.test
    posts = db.posts

    choice = int(input("""Select your choice
    [1] - View documents
    [2] - Search by name
    [3] - End
    ---> """))
    user_choice(choice, posts)


def user_choice(choice, posts):
    try:
        if choice == 1:
            view_documents(posts)
        elif choice == 2:
            search_document(posts)
        elif choice == 3:
            end()
        else:
            print("Invalid choice. Please select again.")
            main()
    except ValueError:
        print("[ERROR] Invalid input: Please enter a number.")
        return_to_principal()
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        return_to_principal()


def view_documents(posts):
    os.system('cls')
    print("\nRecovering all documents")
    for post in posts.find({}):
        print("\nClient:")
        pprint.pprint(post)
    return_to_principal()


def search_document(posts):
    os.system('cls')
    print("\nSearch document by name")
    name = input("Enter the name to search for: ")
    result = posts.find_one({"client": name})
    if result:
        print("\nClient :")
        pprint.pprint(result)
        return_to_principal()
    else:
        print("No client found with that name.")
        return_to_principal()


def return_to_principal():
    input('Press enter to return')
    main()


def end():
    os.system('cls')
    print("End system...")
    sleep(2)
    os.system('cls')


if __name__ == '__main__':
    main()
