import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A22rILr2wrN9s5nPY8PEuvOa5q92_fAXlgcq0J9bRiL-V__zxv2xQPf9hMABPvwzHWxGcoQk-4wjvgTouhiIPv3_0Vkz9Akhb8rXxScYAxB-oFbBhk_ovE-hEp0hTBrpQonALGM'
    transferData = TransferData(access_token)

    file_from = input("Enter The File Path To Transfer: ")
    file_to = input("Enter The Full Path To Upload To Dropbox: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved: ")

main()