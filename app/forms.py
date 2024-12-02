from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from app.models import Contact

class ContactForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50)])
    apellido = StringField('Apellido', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telefono = StringField('Teléfono', validators=[DataRequired(), Length(min=9, max=15)])
    submit = SubmitField('Guardar')

    def validate_telefono(self, field):
        if not Contact.validate_phone(field.data):
            raise ValidationError('Número de teléfono inválido')