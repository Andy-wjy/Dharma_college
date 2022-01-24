from app import db
if __name__ == '__main__':
    db.create_all()

    role = Role(
        name='superadmin',
        auths='iii'
    )

    db.session.add(role)
    db.session.commit()

    from werkzeug.security import generate_password_hash
    print(len(generate_password_hash('testpassword')))
    admin = Admin(
        name='textadmin',
        pwd=generate_password_hash('testpassword'),
        is_super=0,
        role_id=1
    )
    db.session.add(admin)
    db.session.commit()