from flask import Flask, render_template, request
from sorting_algorithms import bubble_sort, selection_sort

app = Flask(__name__)

SAMPLE_STUDENTS = [
    {"name": "Aarav", "marks": 78},
    {"name": "Priya", "marks": 92},
    {"name": "Rohan", "marks": 65},
    {"name": "Sneha", "marks": 84},
    {"name": "Ishaan", "marks": 71},
]

@app.route("/", methods=["GET", "POST"])
def index():
    rows = SAMPLE_STUDENTS.copy()
    algorithm = "bubble"
    order = "ascending"
    error = None
    sorted_rows = None

    if request.method == "POST":
        algorithm = request.form.get("algorithm", "bubble")
        order = request.form.get("order", "ascending")
        names = request.form.getlist("student_name")
        marks = request.form.getlist("student_marks")
        rows = []
        try:
            for name, mark in zip(names, marks):
                name = name.strip()
                if not name:
                    continue
                value = float(mark)
                if value < 0 or value > 100:
                    raise ValueError("Marks must be between 0 and 100.")
                rows.append({"name": name, "marks": value})
            if not rows:
                raise ValueError("Please enter at least one student.")
            if algorithm == "selection":
                sorted_rows = selection_sort(rows, order)
            else:
                sorted_rows = bubble_sort(rows, order)
        except ValueError as exc:
            error = str(exc)
            sorted_rows = None

    return render_template(
        "index.html",
        rows=rows,
        sorted_rows=sorted_rows,
        algorithm=algorithm,
        order=order,
        error=error,
    )

if __name__ == "__main__":
    app.run(debug=True)
