from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import Contact
from app.forms import ContactForm
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('contact_list.html', contacts=contacts)

@main.route('/contact/new', methods=['GET', 'POST'])
def create_contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            email=form.email.data,
            telefono=form.telefono.data
        )
        db.session.add(contact)
        try:
            db.session.commit()
            flash('Contacto creado exitosamente', 'success')
            return redirect(url_for('main.index'))
        except:
            db.session.rollback()
            flash('Error al crear el contacto. El email o teléfono ya existe.', 'danger')
    return render_template('create_contact.html', form=form)

@main.route('/contact/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)
    form = ContactForm(obj=contact)
    if form.validate_on_submit():
        contact.nombre = form.nombre.data
        contact.apellido = form.apellido.data
        contact.email = form.email.data
        contact.telefono = form.telefono.data
        try:
            db.session.commit()
            flash('Contacto actualizado exitosamente', 'success')
            return redirect(url_for('main.index'))
        except:
            db.session.rollback()
            flash('Error al actualizar el contacto', 'danger')
    return render_template('edit_contact.html', form=form, contact=contact)

@main.route('/contact/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contacto eliminado exitosamente', 'success')
    return redirect(url_for('main.index'))

@main.route('/contact/search')
def search_contact():
    phone = request.args.get('phone', '')
    if phone:
        contacts = Contact.query.filter(Contact.telefono.contains(phone)).all()
    else:
        contacts = []
    return render_template('contact_list.html', contacts=contacts)