#No Authentication  
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

#Basic Authentication
sheet_response = requests.post(
  sheet_endpoint, 
  json=sheet_inputs, 
  auth=(
      YOUR USERNAME, 
      YOUR PASSWORD,
  )
)

#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {YOUR TOKEN}"
}
sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)