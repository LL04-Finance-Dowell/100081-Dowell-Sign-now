# 100081-Dowell-Sign-now

Function Description

    The upload_pdf_and_get_url function uploads a PDF file to a specific URL.
    It handles various error cases and returns relevant error messages.

Error Handling

    If the upload is successful, it returns the URL of the uploaded PDF.
    If the server response is not in JSON format or does not contain the 'file_url' field, it provides an appropriate error message.
    If the server returns an error status code, it reports the error along with the response text.
    If there is a JSONDecodeError during the response processing, it returns an internal server error response.

Note

Please replace 'your_file.pdf' with the actual path to the PDF file you want to upload.