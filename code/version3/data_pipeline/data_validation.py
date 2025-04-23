# Ensure Great Expectations is installed: pip install great-expectations
from great_expectations.core.batch import BatchRequest
from great_expectations.data_context import DataContext

# Initialize Great Expectations context
context = DataContext()

# Define batch request
batch_request = BatchRequest(
    datasource_name="my_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="cleaned_data.csv",
)

# Validate data
validator = context.get_validator(batch_request=batch_request)
expectation_suite_name = "default"
results = validator.validate(expectation_suite_name=expectation_suite_name)

# Print validation results
print(results)