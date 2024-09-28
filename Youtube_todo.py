import json



def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def data_save_helper(videos):
    with open('youtube.txt', 'w') as file:
         json.dump(videos , file)


def list_of_videos(videos):
    print('\n')
    print("*" * 70)
    for index , video in enumerate(videos , start=1):
        print(f'{index}. {video['name']} , Duration: {video['time']}')
    print('\n')
    print("*" * 70)    

def add_videos(videos):
    name = input("enter video name: ")
    time = input('enter video time: ')
    videos.append({'name': name , 'time':time})
    data_save_helper(videos)

def update_videos(videos):
    list_of_videos(videos)
    index = int(input("enter the video num for update: "))
    if 1<= index <= len(videos):
        name = input("enter the updated name: ")
        time = input("enter the updated time: ")
        videos[index - 1] = {'name':name , 'time':time}
        data_save_helper(videos)
    else:
        print("Invalid user Index")

def delete_videos(videos):
    list_of_videos(videos)
    index = int(input("enter the number of videos to be deleted: "))
    if 1<=index<len(videos):
        del videos[index-1]
        data_save_helper(videos)
    else:
        print("enter invalid input")

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager")
        print(" Select a choice from 1 to 5")
        print("1. list of all videos: ")
        print("2. add new youtube videos: ")
        print("3. update a youtube videos: ")
        print("4. delete a youtube videos: ")
        print("5. Exist to app")

        choice = input("enter the choice: ") 

        match choice:
            case '1':
                list_of_videos(videos)

            case '2':
                add_videos(videos)
            
            case '3':
                update_videos(videos)

            case '4':
                delete_videos(videos)

            case '5':
                break

            case _:
                print("please enter valid option")
    
        
if __name__ == "__main__":
    main()