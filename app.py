from flask import Flask, render_template, request

app = Flask(__name__)

# Route 1: Home Page (Static)
@app.route("/")
def home():
    return render_template("index.html")

# Route 2: Module A - Tea Culture (Static)
@app.route("/tea-culture")
def tea_culture():
    return render_template("tea.html")

# Route 3: Module B - Tourism (Static)
@app.route("/tourism")
def tourism():
    return render_template("tourism.html")

# Route 4: Module C - Booking System (Dynamic)
# This fulfills the "Request-Response Flow" requirement
@app.route("/book-experience", methods=['GET', 'POST'])
def book_experience():
    if request.method == 'POST':
        # Step 4: Server Processing (Backend Logic)
        visitor_name = request.form.get('name')
        visit_date = request.form.get('date')
        selected_farm = request.form.get('farm')
        activity = request.form.get('activity')
        
        # In a real app, we would save this to a database here.
        # For the MVP, we pass the data back to the template to show confirmation.
        return render_template("booking.html", success=True, name=visitor_name, date=visit_date, farm=selected_farm)
    
    # Step 1: The Request (GET) - Show the form
    return render_template("booking.html", success=False)

if __name__ == "__main__":
    app.run(debug=True, port=5001)