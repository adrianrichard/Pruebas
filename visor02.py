import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(photo):
    try:
        sqliteConnection = sqlite3.connect('image_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO Image VALUES (?)"""

        #empPhoto = convertToBinaryData(photo)
        #resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        #data_tuple = (empId, name, empPhoto, resume)
        cursor.execute(sqlite_insert_blob_query)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

insertBLOB("6.png")
#insertBLOB(2, "David", "E:\pynative\Python\photos\david.jpg", "E:\pynative\Python\photos\david_resume.txt")
