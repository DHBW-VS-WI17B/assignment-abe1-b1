class Response_Helper():
    """handle status codes of the server responses"""
    @staticmethod
    def handle_exception(status_code, error_msg):
        if status_code == 500:
            print("An unexpected error has occurred! Please try again.")
        else:
            print(error_msg)

    @staticmethod
    def successfull():
        print("The request was successfully processed!")
