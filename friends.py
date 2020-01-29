
friend1 = input("Enter the name of first friend:").lower()
friend2 = input("Enter the name of second friend:").lower()
friend3 = input("Enter the name of third friend:").lower()
friends_list=[friend1,friend2,friend3]

all_friends = open('people.txt','r')
friends_content = set([line.strip() for line in all_friends.readlines()])
#friends_content_set=set(friends_content)
all_friends.close()

friends_nearby=set(friends_list)

common_data=friends_nearby.intersection(friends_content)
nearby=open('nearby_friends.txt','w')
for friends in common_data:
    print(f'{friends} is nearby..meet him/her')
    nearby.write(friends+"\n")


nearby.close()

