def transform(data):
    # Standardize column names
    for df in data.values():
        df.columns = df.columns.str.lower().str.strip()

    # Remove invalid donations
    data["donations"] = data["donations"][data["donations"]["amount"] > 0]

    # Clean region values
    data["beneficiaries"]["region"] = (
        data["beneficiaries"]["region"]
        .str.strip()
        .str.title()
    )

    # Validate completion status
    valid_status = ["Completed", "In Progress", "Dropped"]
    data["participation"] = data["participation"][
        data["participation"]["completion_status"].isin(valid_status)
    ]

    return data


if __name__ == "__main__":
    from extract import extract

    raw_data = extract()
    clean_data = transform(raw_data)

    for name, df in clean_data.items():
        print(f"{name}: {df.shape}")
