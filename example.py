import cloudstitch

# User Variables
user = "jeffl"
app = "pythonsdk-test"
worksheet = "Sheet2"

# Load worksheet as local object.
myWorksheet = cloudstitch.load_worksheet(user,app,worksheet)

# Print data.
print("Before Add: \n",myWorksheet.data)

# Add an Entry.
myWorksheet.add_entry(Year="Test",team="Phillies")

# Print data showing added entry.
print("After Add is the same because no new snapshot of the data: \n",myWorksheet.data)