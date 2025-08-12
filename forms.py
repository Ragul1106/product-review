from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Length

class ProductReviewForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    rating = IntegerField("Rating (1–5)", validators=[DataRequired(), NumberRange(min=1, max=5)])
    review = TextAreaField("Review Message", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Submit Review")
