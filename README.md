# Assignment 4 — Forms and Validation

Yerkebulan Abenov

Open `index.html` to choose a task. Bootstrap CSS and Montserrat are included locally. The pages contain no JavaScript.

To try all forms, run:

```powershell
python serve.py
```

Open http://localhost:8765. The server shows a confirmation page after registration and does not save the data. Use a sample password. You can also open the HTML files directly to view the forms and try validation.

## Files

- `task1.html`: train ticket form.
- `task2.html`: registration with native HTML validation.
- `task3.html`: corrected café form.
- `styles.css`: shared styles and responsive layouts.
- `assets/`: local Bootstrap CSS, Montserrat and license information.
- `screenshots/`: actual browser screenshots at 375px and 1280px.
- `verification/`: browser and W3C results.
- `Assignment4_Yerkebulan_Abenov.docx` and `.pdf`: report.
- `reference/task3-original.txt`: numbered source for the report's problem table.

Before submission, add your group and GitHub repository URL to the report, then upload the source to that repository.

## Quick notes for the defense

- `required` prevents an empty required field.
- `minlength` and `maxlength` limit text length.
- `min`, `max` and `step` set number and date/time limits.
- A time `step` is in seconds, so 1800 means 30 minutes.
- An empty select option fails `required`.
- Radios with the same name form one choice group.
- `id` connects a field to its label; `name` identifies its submitted value.
- `:user-invalid` shows errors after editing a field.
- A reset button restores defaults. A submit button triggers native validation.
- CSS changes the visual button order on phones without changing the HTML.
"# Web-technology-4-assignment" 
