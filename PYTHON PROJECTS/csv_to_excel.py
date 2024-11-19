import pandas as pd # type: ignore
import os

def csv_to_excel():
    print("Welcome to the CSV to Excel Converter!")
    print("Follow the instructions to convert your CSV file to Excel format.")
    
    # Prompt user for CSV file path
    csv_file_path = input("Enter the full path of the CSV file you want to convert: ").strip()
    
    # Check if the CSV file exists
    #Escape Backslashes
    #Add double backslashes (\\) or prefix the path with r (raw string) to correctly interpret backslashes.
    if not os.path.exists(csv_file_path) or not csv_file_path.endswith('.csv'):
        print(" Error: The file does not exist or is not a CSV file. Please try again.")
        return
    
    # Prompt user for the output Excel file path
    default_excel_path = os.path.splitext(csv_file_path)[0] + ".xlsx"
    excel_file_path = input(f"Enter the desired Excel file path (Press Enter to save as '{default_excel_path}'): ").strip()
    
    # Use default path if none provided
    if not excel_file_path:
        excel_file_path = default_excel_path
    
    # Convert CSV to Excel
    try:
        print("\n⏳ Converting your CSV to Excel...")
        data = pd.read_csv(csv_file_path)
        data.to_excel(excel_file_path, index=False)
        print(f"✅ Success! Your Excel file has been saved at: {excel_file_path}")
    except Exception as e:
        print(f"❌ An error occurred during the conversion: {e}")

    print("\nThank you for using the CSV to Excel Converter! Have a great day!")

# Run the converter
csv_to_excel()
