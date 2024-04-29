import pandas as pd
import streamlit as st

def read_excel(excel_file):
    df = pd.read_excel(excel_file)
    return df

def read_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df

def process_files(files):
    dfs = []
    for file in files:
        if file is not None:
            file_extension = file.name.split('.')[-1]
            if file_extension == 'csv':
                df = read_csv(file)
            elif file_extension in ['xls', 'xlsx']:
                df = read_excel(file)
            else:
                st.error(f"Unsupported file format for {file.name}. Please upload a CSV or Excel file.")
                continue
            # Drop duplicates
            df.drop_duplicates(inplace=True)
            dfs.append(df)
    if len(dfs) == 0:
        return None
    else:
        # Concatenate all data frames
        combined_df = pd.concat(dfs, ignore_index=True)
        return combined_df

def main():
    st.title("Upload and Merge Files")

    uploaded_files = st.file_uploader("Upload CSV or Excel files", type=['csv', 'xls', 'xlsx'], accept_multiple_files=True)

    if uploaded_files:
        st.write("### Uploaded Data")
        combined_df = process_files(uploaded_files)
        if combined_df is not None:
            st.write(combined_df)

            csv_file = combined_df.to_csv(index=False)
            # excel_file = combined_df.to_excel(index=False)
            st.download_button(
                label="Download CSV",
                data=csv_file,
                file_name="merged_data.csv",
                mime="text/csv",
            )
            # st.download_button(
            #     label="Download Excel",
            #     data=excel_file,
            #     file_name="merged_data.xlsx",
            #     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            # )


if __name__ == "__main__":
    main()
