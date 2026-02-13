def validate_telco_data(df):
    """
    Lightweight dataframe validation without Great Expectations.
    Returns: (is_valid: bool, failed: list[dict])
    """
    failed = []

    # Basic checks
    if df is None or df.empty:
        failed.append({"check": "non_empty", "message": "DataFrame is empty"})
        return False, failed

    # Required columns (adjust if your dataset differs)
    required_cols = {
        "customerID", "gender", "SeniorCitizen", "Partner", "Dependents",
        "tenure", "PhoneService", "InternetService", "Contract",
        "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges",
        "Churn"
    }
    missing = sorted(required_cols - set(df.columns))
    if missing:
        failed.append({"check": "required_columns", "message": "Missing required columns", "missing": missing})

    # Target values
    if "Churn" in df.columns:
        bad = sorted(set(df["Churn"].dropna().unique()) - {"Yes", "No"})
        if bad:
            failed.append({"check": "churn_values", "message": "Unexpected Churn values", "bad_values": bad})

    # Null checks (only for key fields)
    key_not_null = ["customerID", "Churn"]
    for c in key_not_null:
        if c in df.columns:
            n_null = int(df[c].isna().sum())
            if n_null > 0:
                failed.append({"check": "not_null", "column": c, "null_count": n_null})

    # Numeric sanity
    if "MonthlyCharges" in df.columns:
        if (df["MonthlyCharges"] < 0).any():
            failed.append({"check": "monthlycharges_nonnegative", "message": "MonthlyCharges has negatives"})

    is_valid = (len(failed) == 0)
    return is_valid, failed
