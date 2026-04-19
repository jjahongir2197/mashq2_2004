from flask import Flask, render_template, request

app = Flask(__name__)

# ====================== KONTAKT FORMA ======================
@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    res = None
    if request.method == 'POST':
        ism = request.form.get('ism', '').strip()
        email = request.form.get('email', '').strip()
        xabar = request.form.get('xabar', '').strip()

        if len(ism) > 2 and '@' in email and len(xabar) >= 15:
            res = [ism, email, xabar]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('kontakt.html', res=res, title="Kontakt")


# ====================== RO‘YXATDAN O‘TISH ======================
@app.route('/', methods=['GET', 'POST'])          # Asosiy sahifa
@app.route('/register', methods=['GET', 'POST'])
def register():
    res = None
    if request.method == 'POST':
        foydalanuvchi_nomi = request.form.get('foydalanuvchi_nomi', '').strip()
        telefon = request.form.get('telefon', '').strip()
        yosh_str = request.form.get('yosh', '').strip()

        # Validatsiya
        try:
            yosh = int(yosh_str)
            yosh_to_gri = 18 <= yosh <= 99
        except ValueError:
            yosh_to_gri = False

        if (len(foydalanuvchi_nomi) > 4 and 
            telefon.startswith('+') and len(telefon) >= 11 and 
            yosh_to_gri):
            
            res = [foydalanuvchi_nomi, telefon, str(yosh)]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('register.html', res=res, title="Ro'yxatdan o'tish")


if __name__ == '__main__':
    app.run(debug=True)
