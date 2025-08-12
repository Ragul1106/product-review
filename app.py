from flask import Flask, render_template, redirect, url_for, flash
from forms import ProductReviewForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"  

@app.route("/", methods=["GET", "POST"])
def review():
    form = ProductReviewForm()
    if form.validate_on_submit():
        flash(f"Thank you for your review, {form.name.data}!", "success")
        return redirect(url_for("review"))
    return render_template("review.html", form=form)

if __name__ == "__main__":
    app.run(debug=False)
