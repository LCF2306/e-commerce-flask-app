import unittest
from flask_app.app import db  # importing the db instance

# test case to check database write operations
class TestDBWrite(unittest.TestCase):
    # test if a document can be inserted into the database
    def test_insert_document(self):
        collection = db['test_collection']  # get the test_collection from the database
        document = {"field": "value"}  # define a sample document to insert
        insert_result = collection.insert_one(document)  # insert the document
        self.assertIsNotNone(insert_result.inserted_id)  # ensure the document was inserted

        # verify the inserted document exists in the collection
        inserted_doc = collection.find_one({"field": "value"})
        self.assertIsNotNone(inserted_doc)  # assert the document was found

# run the tests when the script is executed
if __name__ == '__main__':
    unittest.main()