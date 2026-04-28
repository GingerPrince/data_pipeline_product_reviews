from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
import os 

def main():
    df_reviews, products_df = extract_data()
    combined_df = transform_data(df_reviews, products_df)
    # Retrieve the token from an environment variable
    github_token = os.getenv("GH_TOKEN")
    
    # Update the URL to include the token for authentication
    repo_url = f"https://{github_token}@github.com/GingerPrince/data_pipeline_product_reviews.git"
    
    load_data(repo_url=repo_url)
    print("Pipeline completed successfully!")
if __name__ == "__main__":
    main()
