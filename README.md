## elucidat_test

### UI Tests
Run the UI tests by running the following commands
```
$ python -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ cd tests/ui_tests/step_defs
$ python3 -m pytest test_finding_the_truth.py -v -s --selenium_hub <selenium_hub address> --url <application url>
$ python3 -m pytest test_finding_the_truth_select.py -v -s --selenium_hub <selenium_hub address> --url <application url>

```

I have created running tests for the first two pages:
* finding_the_truth.feature and test_finding_the_truth.py
* finding_the_truth_select.feature and test_finding_the_truth_select.py

I created BDD for the further pages:
* evidence.feature
* explore_the_evidence.feature
* is_kevin_guilty.feature
* murder_has_been_committed.feature
* you_decide.feature

### UI Tests
I have to admit that I had some trouble with the API tests.  I looked for an api specification on the endpoint, but I couldn't find one.
I think I would have added tests to record test the state changes made during the progress through the app and at the various decision points.
