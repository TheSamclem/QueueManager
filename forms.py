# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import data
from flask import session
from customize import mdal
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, DateField, HiddenField
from wtforms import SubmitField, PasswordField, SelectField
from wtforms import TextAreaField, IntegerField, BooleanField
from flask_wtf.file import FileAllowed
from wtforms.validators import InputRequired, Length, NumberRange, Optional
from os import name

# WTF Forms

# -- List Tuples of colors, sizes, text background


font_sizes = [("600%", "Very large"), ("500%", "large"), ("400%", "Medium"),
              ("300%", "Small medium"), ("200%", "small"),
              ("150%", "Very small")]
font_sizar = [("600%", u"كبير جداً"),
              ("500%", u"كبير"),
              ("400%", u"متوسط"),
              ("300%", u"متوسط صغير"),
              ("200%", u"صغير"),
              ("150%", u"صغير جداً")]
btn_colors = [("btn-success", "Green"), ("btn-info", "Light blue"),
              ("btn-primary", "Blue"), ("btn-danger", "Red"),
              ("btn-link", "White")]
btn_coloar = [("btn-success", u"أخضر"),
              ("btn-info", u"أزرق فاتح"),
              ("btn-primary", u"أزرق"),
              ("btn-danger", u"أحمر"),
              ("btn-link", u"أبيض")]
durations = [("500", "Half a second"), ("1000", "One second"),
             ("2000", "Two seconds"), ("3000", "Three seconds"),
             ("4000", "Four seconds"), ("5000", "Five seconds"),
             ("8000", "Eight seconds"), ("10000", "Ten seconds")]
duratioar = [("500", u"نصف ثانية"),
             ("1000", u"ثانية واحدة"),
             ("2000", u"ثانيتين"),
             ("3000", u"ثلاث ثواني"),
             ("4000", u"أربع ثواني"),
             ("5000", u"خمس ثواني"),
             ("8000", u"ثمان ثواني"),
             ("10000", u"عشر ثواني")]
tms = [(0, "First Template"), (1, "Second Template"), (2, "Third Template")]
tar = [(0, u"القالب الأول"),
       (1, u"القالب الثاني"),
       (2, u"القالب الثالث")]

# -- Customizing and updating touch


class Touch_c(FlaskForm):
    touch = SelectField("Select a template for Touch screen :",
                        choices=tms,
                        coerce=int)
    title = StringField("Title text :", validators=[
        InputRequired("Must enter at least 5 letters and Title" +
                      " should be maximum of 300 letters"),
        Length(5, 300)])
    hsize = SelectField("Choose title font size :", choices=font_sizes,
                        coerce=str)
    hcolor = StringField("Select title font color :")
    hfont = StringField("choose a font for title :")
    hbfont = HiddenField("HB")
    hbg = StringField("Select heading background color :")
    tsize = SelectField("choose task font size :", choices=font_sizes,
                        coerce=str)
    tcolor = SelectField("choose tasks color :",
                         choices=btn_colors, coerce=str)
    tfont = StringField("choose tasks font :")
    tbfont = HiddenField("TB")
    msize = SelectField("choose message font size :", choices=font_sizes,
                        coerce=str)
    mcolor = StringField("Select message font color :")
    mfont = StringField("choose message font : ")
    mbfont = HiddenField("MB")
    mduration = SelectField("choose message duration of appearing : ",
                            choices=durations, coerce=str)
    mbg = StringField("Select message background color :")
    message = TextAreaField("Insert message to be displayed," +
                            " when any task choosen :",
                            validators=[InputRequired
                                        ("Must enter at least 5" +
                                         " letter and Message should" +
                                         " be maximum of 300 letters .."),
                                        Length(5, 300)])
    background = SelectField("Select background : ", coerce=int)
    bcolor = StringField("Select a background color : ")
    naudio = SelectField("Select audio notification : ", coerce=int)
    submit = SubmitField("Customize")

    def __init__(self, *args, **kwargs):
        super(Touch_c, self).__init__(*args, **kwargs)
        bgs = []
        aud = []
        bgs.append((00, "Use color selection .."))
        aud.append((00, "Disable audio notification .."))
        if data.Media.query.count() >= 1:
            for v in data.Media.query.filter_by(img=True):
                bgs.append((v.id, str(v.id) + ".  " + v.name))
            for v in data.Media.query.filter_by(audio=True):
                aud.append((v.id, str(v.id) + ".  " + v.name))
        self.naudio.choices = aud
        self.background.choices = bgs


class Touch_c_ar(FlaskForm):
    touch = SelectField(u"إختار قالب للشاشة اللمس :",
                        choices=tar,
                        coerce=int)
    title = StringField(u"نص العنوان :", validators=[
        InputRequired(u"العنوان لا يقل عن 5 حروف و لا يزيد عن 300 حرف"),
        Length(5, 300)])
    hsize = SelectField(u"إختر حجم العنوان :", choices=font_sizar,
                        coerce=str)
    hcolor = StringField(u"إختر لون العنوان :")
    hfont = StringField(u"إختر خط العنوان :")
    hbfont = HiddenField("HB")
    hbg = StringField(u"إختر خلفية العنوان :")
    tsize = SelectField(u"إختر حجم نص المهمة :", choices=font_sizar,
                        coerce=str)
    tcolor = SelectField(u"إختر لون المهمات :",
                         choices=btn_coloar, coerce=str)
    tfont = StringField(u"إختر خط المهمات :")
    tbfont = HiddenField("TB")
    msize = SelectField(u"إختر حجم الرسالة :", choices=font_sizar,
                        coerce=str)
    mcolor = StringField(u"إختر لون الرسالة :")
    mfont = StringField(u"إختر خط الرسالة :")
    mbfont = HiddenField("MB")
    mduration = SelectField(u"إختر مدة ظهور الرسالة :",
                            choices=duratioar, coerce=str)
    mbg = StringField(u"إختار خلفية الرسالة :")
    message = TextAreaField(
        u"أدخل نص الرسالة :",
        validators=[InputRequired(
            u"الرسالة لا تقل عن 5 حروف و لا تزيد عن 300 حرف"),
            Length(5, 300)])
    background = SelectField(u"إختر خلفية :", coerce=int)
    bcolor = StringField(u"إختر لون الخلفية :")
    naudio = SelectField(u"إختر ملف التنبيه الصوتي :", coerce=int)
    submit = SubmitField(u"تخصيص")

    def __init__(self, *args, **kwargs):
        super(Touch_c_ar, self).__init__(*args, **kwargs)
        bgs = []
        aud = []
        bgs.append((00, u"إستخدم اللون المختار كبديل"))
        aud.append((00, u"عطل التنبيه الصوتي"))
        if data.Media.query.count() >= 1:
            for v in data.Media.query.filter_by(img=True):
                bgs.append((v.id, str(v.id) + ".  " + v.name))
            for v in data.Media.query.filter_by(audio=True):
                aud.append((v.id, str(v.id) + ".  " + v.name))
        self.naudio.choices = aud
        self.background.choices = bgs

# -- Customizing and updating display


class Display_c(FlaskForm):
    display = SelectField("Select a template for Display screen :",
                          choices=tms,
                          coerce=int)
    title = StringField("A tiitle for display page:", validators=[
        InputRequired("Title should be maximum of 300 letters .."),
        Length(0, 300)])
    background = SelectField("Select a background :", coerce=int)
    hsize = SelectField("choose title font size :", choices=font_sizes,
                        coerce=str)
    hcolor = StringField("choose title font color :")
    hfont = StringField("choose title font :")
    hbfont = HiddenField("HB")
    hbg = StringField("choose title background color :")
    tsize = SelectField("choose main heading office font size :",
                        choices=font_sizes,
                        coerce=str)
    tcolor = StringField("choose main heading office color :")
    tfont = StringField("choose main heading office font :")
    tbfont = HiddenField("TB")
    h2color = StringField("choose main heading ticket color :")
    h2size = SelectField("choose main heading ticket font size :",
                         choices=font_sizes, coerce=str)
    h2font = StringField("choose main heading ticket font :")
    h2bfont = HiddenField("H2B")
    ssize = SelectField("choose secondery heading font size :",
                        choices=font_sizes, coerce=str)
    scolor = StringField("choose secondery heading color :")
    sfont = StringField("choose secondery heading font :")
    sbfont = HiddenField("SB")
    mduration = SelectField("choose message duration of appearing : ",
                            choices=durations, coerce=str)
    rrate = SelectField("choose page refreash rate : ", choices=durations,
                        coerce=str)
    announce = SelectField("Verbal announcement : ",
                           choices=[("en-us",
                                    "English"),
                                    ("ar", "Arabic"),
                                    ("both", "English and Arabic"),
                                    ("false", "Disable")],
                           coerce=str)
    anr = SelectField('Number of announcement repeating : ',
                      choices=[(1, 'One time'),
                               (2, 'Two times'),
                               (3, 'Three times'),
                               (4, 'Four time'),
                               (5, 'Five times')],
                      coerce=int)
    naudio = SelectField("Select audio notification : ", coerce=int)
    bgcolor = StringField("Select a background color :")
    submit = SubmitField("Customize")

    def __init__(self, *args, **kwargs):
        super(Display_c, self).__init__(*args, **kwargs)
        bgs = []
        aud = []
        bgs.append((00, "Use color selection .."))
        aud.append((00, "Disable audio notification .."))
        if data.Media.query.count() >= 1:
            for v in data.Media.query.filter_by(img=True):
                bgs.append((v.id, str(v.id) + ".  " + v.name))
            for v in data.Media.query.filter_by(audio=True):
                aud.append((v.id, str(v.id) + ".  " + v.name))
        self.naudio.choices = aud
        self.background.choices = bgs


class Display_c_ar(FlaskForm):
    display = SelectField(u"إختار قالب للشاشة العرض :",
                          choices=tar,
                          coerce=int)
    title = StringField(u"نص العنوان :", validators=[
        InputRequired(u"العنوان يجب أن لا يتعدا 300 حرف"),
        Length(0, 300)])
    background = SelectField(u"إختار الخلفية :", coerce=int)
    hsize = SelectField(u"إختار حجم العنوان :", choices=font_sizar,
                        coerce=str)
    hcolor = StringField(u"إختار لون العنوان :")
    hfont = StringField(u"إختار خط العنوان :")
    hbfont = HiddenField("HB")
    hbg = StringField(u"إختار خلفية العنوان :")
    tsize = SelectField(u"إختار حجم المكتب الحالي :",
                        choices=font_sizar,
                        coerce=str)
    tcolor = StringField(u"إختار لون المكتب الحالي :")
    tfont = StringField(u"إختار خط المكتب الحالي :")
    tbfont = HiddenField("TB")
    h2color = StringField(u"إختار لون التذكرة الحالية :")
    h2size = SelectField(u"إختار حجم التذكرة الحالية :",
                         choices=font_sizar, coerce=str)
    h2font = StringField(u"إختار خط التذكرة الحالية :")
    h2bfont = HiddenField("H2B")
    ssize = SelectField(u"إختار حجم لائحة الإنتضار :",
                        choices=font_sizar, coerce=str)
    scolor = StringField(u"إختار لون لائحة الإنتضار :")
    sfont = StringField(u"إختار خط لائحة الإنتضار :")
    sbfont = HiddenField("SB")
    mduration = SelectField(u"إختار مدة عرض التنبيه :",
                            choices=duratioar, coerce=str)
    rrate = SelectField(u"إختار مدة تجديد بيانات الشاشة :",
                        choices=duratioar,
                        coerce=str)
    announce = SelectField(u"تنبيه المناداة الصوتي :",
                           choices=[("en-us",
                                    u"إنجليزي"),
                                    ("ar", u"عربي"),
                                    ("false", u"تعطيل")],
                           coerce=str)
    anr = SelectField(u'عدد مرات تكرار المناداة الصوتي :',
                      choices=[(1, u'مرة واحدة'),
                               (2, u'مرتين'),
                               (3, u'ثلاث مرات'),
                               (4, u'أربع مرات'),
                               (5, u'خمس مرات')],
                      coerce=int)
    naudio = SelectField(u"إختار ملف التنبيه الصوتي :", coerce=int)
    bgcolor = StringField(u"إختار لون الخلفية :")
    submit = SubmitField(u"تخصيص")

    def __init__(self, *args, **kwargs):
        super(Display_c_ar, self).__init__(*args, **kwargs)
        bgs = []
        aud = []
        bgs.append((00, u"إستخدم اللون المختار كبديل"))
        aud.append((00, u"عطل التنبيه الصوتي"))
        if data.Media.query.count() >= 1:
            for v in data.Media.query.filter_by(img=True):
                bgs.append((v.id, str(v.id) + ".  " + v.name))
            for v in data.Media.query.filter_by(audio=True):
                aud.append((v.id, str(v.id) + ".  " + v.name))
        self.naudio.choices = aud
        self.background.choices = bgs


# -- Customizing and updating display

class Slide_a(FlaskForm):
    title = StringField("Enter a slide title :")
    hsize = SelectField("Select a title font size :", choices=font_sizes,
                        coerce=str)
    hcolor = StringField("Select a title font color :")
    hfont = StringField("Select a title font :")
    hbfont = HiddenField("HB")
    hbg = StringField("Select title background color :")
    subti = StringField("Enter a subtitle :")
    tsize = SelectField("Select subtitle font size :", choices=font_sizes,
                        coerce=str)
    tcolor = StringField("Select sub title color :")
    tfont = StringField("Select subtitle font :")
    tbfont = HiddenField("TB")
    tbg = StringField("Select subtitle background color :")
    background = SelectField("Select background : ", coerce=int)
    bgcolor = StringField("Select background color : ")
    submit = SubmitField("Add slide")

    def __init__(self, *args, **kwargs):
        super(Slide_a, self).__init__(*args, **kwargs)
        bgs = []
        bgs.append((00, "Use color selection .."))
        if data.Media.query.count() >= 1:
            for v in data.Media.query.filter_by(img=True):
                bgs.append((v.id, str(v.id) + ".  " + v.name))
        self.background.choices = bgs


class Slide_a_ar(FlaskForm):
    title = StringField(u"عنوان الشريحة الرئيسي :")
    hsize = SelectField(u"إختار حجم العنوان الرئيسي :", choices=font_sizar,
                        coerce=str)
    hcolor = StringField(u"إختار لون العنوان الرئيسي :")
    hfont = StringField(u"إختار خط العنوان الرئيسي :")
    hbfont = HiddenField("HB")
    hbg = StringField(u"إختار خلفية العنوان الرئيسي :")
    subti = StringField(u"عنوان الشريحة الجانبي :")
    tsize = SelectField(u"حجم عنوان الشريحة الجانبي :", choices=font_sizar,
                        coerce=str)
    tcolor = StringField(u"إختار لون عنوان الشريحة الجانبي :")
    tfont = StringField(u"إختار خط الشريحة الجانبي :")
    tbfont = HiddenField("TB")
    tbg = StringField(u"إختار خلفية الشريحة الجانبي :")
    background = SelectField(u"إختار الخلفية :", coerce=int)
    bgcolor = StringField(u"إختار لون الخلفية :")
    submit = SubmitField(u"إضافة الشريحة")

    def __init__(self, *args, **kwargs):
        super(Slide_a_ar, self).__init__(*args, **kwargs)
        bgs = []
        bgs.append((00, u"إستخدم اللون المختار كبديل"))
        if data.Media.query.count() >= 1:
            for v in data.Media.query.filter_by(img=True):
                bgs.append((v.id, str(v.id) + ".  " + v.name))
        self.background.choices = bgs


class Slide_c(FlaskForm):
    status = SelectField("Disable or enable slide-show :", choices=[
        (1, "Enable"), (2, "Disable")], coerce=int)
    effect = SelectField("Select transition effect :", choices=[
        ("fade", "Fade effect"), ("slide", "Slide effect")])
    navigation = SelectField("Slide navigation bars :",
                             choices=[(1, "Enable"),
                                      (2, "Disable")],
                             coerce=int)
    rotation = SelectField("Slide images rotation :",
                           choices=[("1000", "Every second"),
                                    ("3000", "Every three seconds"),
                                    ("5000", "Every five seconds"),
                                    ("8000", "Every eight seconds"),
                                    ("60000", "Every minute"),
                                    ("false", "Disable rotation")],
                           coerce=str)
    submit = SubmitField("Customize slide-show")


class Slide_c_ar(FlaskForm):
    status = SelectField(u"تفعيل أو تعطيل عرض الشرائح :", choices=[
        (1, u"تفعيل"),
        (2, u"تعطيل")], coerce=int)
    effect = SelectField(u"إختار حركة إنتقالية :", choices=[
        ("fade", u"تأثير التلاشي"),
        ("slide", u"تأثير الإنزلاق")])
    navigation = SelectField(u"مؤشرات التوجيه :",
                             choices=[(1, u"تفعيل"),
                                      (2, u"تعطيل")],
                             coerce=int)
    rotation = SelectField(u"مدة تبديل الشرائح :",
                           choices=[("1000", u"كل ثانية"),
                                    ("3000", u"كل ثلث ثواني"),
                                    ("5000", u"كل خمس ثواني"),
                                    ("8000", u"كل ثمن ثواني"),
                                    ("60000", u"كل دقيقة"),
                                    ("false", u"تعطيل تبديل الشرائح")],
                           coerce=str)
    submit = SubmitField(u"إعداد")


# -- Adding Office


class Offices_a(FlaskForm):
    name = IntegerField("Enter a unique office number : ",
                        validators=[NumberRange(
                            min=1, max=9999,
                            message="Only allowed range of " +
                            "numbers 1-9999")])
    operator = SelectField("Select a user operator for the office : ",
                           validators=[InputRequired(
                               "You must select unassigned operator ..")],
                           coerce=int)
    prefix = SelectField("Select unique prefix for the office : ",
                         validators=[
                             InputRequired(
                                 "You must choose unique prefix ..")])
    submit = SubmitField("Add")

    def __init__(self, upd=None, uid=None, *args, **kwargs):
        super(Offices_a, self).__init__(*args, **kwargs)
        ll = [(00, "Without an operator")]
        prefixs = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'),
                   ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'),
                   ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'),
                   ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'),
                   ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'),
                   ('Y', 'Y'), ('Z', 'Z')]
        upd = upd
        for v in data.Office.query.order_by(data.Office.timestamp):
            if (v.prefix, v.prefix) in prefixs:
                prefixs.remove((v.prefix, v.prefix))
        for n in data.User.query.filter_by(role_id=3):
            if data.Office.query.filter_by(operator_id=n.id).first() is None:
                ll.append((n.id, n.name))
        if upd is not None:
            prefixs.append((upd, upd))
        if uid is not None:
            ll.append((uid, data.User.query.filter_by(id=uid).first().name))
        self.prefix.choices = prefixs
        self.operator.choices = ll


class Offices_a_ar(FlaskForm):
    name = IntegerField(
        u"إدخل رقم مكتب مميز :",
        validators=[
            NumberRange(
                min=1, max=9999,
                message=u"أقل قيمة 1 و أقصى قيمة 9999")])
    operator = SelectField(u"إختر مشغل للمكتب :",
                           validators=[InputRequired(
                               u"يجب إختيار مشغل غير معين")],
                           coerce=int)
    prefix = SelectField(u"إختار رمز حرفي مميز :",
                         validators=[
                             InputRequired(
                                 u"You must choose unique prefix ..")])
    submit = SubmitField(u"إضافة")

    def __init__(self, upd=None, uid=None, *args, **kwargs):
        super(Offices_a_ar, self).__init__(*args, **kwargs)
        ll = [(00, u"من غير مشغل")]
        prefixs = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'),
                   ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'),
                   ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'),
                   ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'),
                   ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'),
                   ('Y', 'Y'), ('Z', 'Z')]
        upd = upd
        for v in data.Office.query.order_by(data.Office.timestamp):
            if (v.prefix, v.prefix) in prefixs:
                prefixs.remove((v.prefix, v.prefix))
        for n in data.User.query.filter_by(role_id=3):
            if data.Office.query.filter_by(operator_id=n.id).first() is None:
                ll.append((n.id, n.name))
        if upd is not None:
            prefixs.append((upd, upd))
        if uid is not None:
            ll.append((uid, data.User.query.filter_by(id=uid).first().name))
        self.prefix.choices = prefixs
        self.operator.choices = ll


# -- Adding Task

class Task_a(FlaskForm):
    name = StringField("Enter unique title for the task : ",
                       validators=[InputRequired
                                   ("Required not less than " +
                                    "5 nor more than 300 letters"),
                                   Length(5, 300)])
    submit = SubmitField("Add")


class Task_a_ar(FlaskForm):
    name = StringField(
        u"أدخل عنوان مهمة مميز :",
        validators=[
            InputRequired(
                u"الحد الأدنى 5 حروف و الحد الأقصى 300 حرف"),
            Length(5, 300)])
    submit = SubmitField(u"إضافة")


# -- Searching serials

class Search_s(FlaskForm):
    number = IntegerField("Please enter a ticket number : ",
                          validators=[Optional()])
    tl = SelectField("Select ticket prefix : ", coerce=int,
                     validators=[
                         InputRequired(
                             "You must select a prefix to search for ..")])
    date = DateField("Select date to search for:", validators=[Optional()])
    submit = SubmitField("Search")

    def __init__(self, *args, **kwargs):
        super(Search_s, self).__init__(*args, **kwargs)
        prf = []
        prf.append((0, "Without a prefix"))
        for v in data.Office.query:
            p = data.Office.query.filter_by(id=v.id).first()
            if p is not None:
                prf.append((p.id, p.prefix +
                            str(p.name) + " , Prefix: " + p.prefix))
        self.tl.choices = prf


class Search_s_ar(FlaskForm):
    number = IntegerField(u"أدخل رقم تذكرة :",
                          validators=[Optional()])
    tl = SelectField(u"إختار رمز حرفي :", coerce=int,
                     validators=[
                         InputRequired(
                             u"يتوجب إختيار رمز حرفي")])
    date = DateField(u"إختار تاريخ إصدار تذكرة :", validators=[Optional()])
    submit = SubmitField(u"بحث")

    def __init__(self, *args, **kwargs):
        super(Search_s_ar, self).__init__(*args, **kwargs)
        prf = []
        prf.append((0, u"بحث من غير رمز حرفي"))
        for v in data.Office.query:
            p = data.Office.query.filter_by(id=v.id).first()
            if p is not None:
                prf.append((p.id, p.prefix +
                            str(p.name) + u" , رمز حرفي : " + p.prefix))
        self.tl.choices = prf


# -- Users Forms

class Login(FlaskForm):
    name = StringField("Enter user name : ",
                       validators=[InputRequired(
                           "Required not less than " +
                           " 5 nor more than 200 letters"), Length(5, 200)])
    password = PasswordField("Enter password : ", validators=[
        InputRequired("Password must be at least of " +
                      " 5 and at most 15 letters .."),
        Length(5, 15)])
    rm = BooleanField("Remeber me : ")
    submit = SubmitField("Login")


class Login_ar(FlaskForm):
    name = StringField(
        u"أدخل إسم مستخدم :",
        validators=[
            InputRequired(
                u"الحد الأقصى 200 حرف  و الحد الأدنى 5 حروف"),
            Length(5, 200)])
    password = PasswordField(u"أدخل كلمة السر :", validators=[
        InputRequired(
            u"الحد الأدنى 5 حروف و الحد الأقصى 15 حرف"),
        Length(5, 15)])
    rm = BooleanField(u"تذكرني :")
    submit = SubmitField(u"تسجيل الدخول")


class User_a(FlaskForm):
    name = StringField("Enter a unique user name : ",
                       validators=[InputRequired
                                   ("Required not less than 5 " +
                                    "nor more than 200 letters"),
                                   Length(5, 200)])
    password = PasswordField("Enter password : ", validators=[
        InputRequired("Password must be at least " +
                      " of 5 and at most 15 letters .."),
        Length(5, 15)])
    role = SelectField("Select a role for the user : ", coerce=int,
                       validators=[InputRequired
                                   ("You must select a role " +
                                    " to add user in ..")])
    submit = SubmitField("Add")

    def __init__(self, *args, **kwargs):
        super(User_a, self).__init__(*args, **kwargs)
        prf = []
        for v in data.Roles.query:
            prf.append((v.id, v.name))
        self.role.choices = prf


class User_a_ar(FlaskForm):
    name = StringField(
        u"أدخل إسم مستخدم مميز :",
        validators=[
            InputRequired(
                u"الحد الأقصى 200 حرف و الحد الأدنى 5 حروف"),
            Length(5, 200)])
    password = PasswordField(u"أدخل كلمة سر :", validators=[
        InputRequired(u"الحد الأدنى 5 حروف و الحد الأقصى 15 حرف"),
        Length(5, 15)])
    role = SelectField(
        u"إختار دور المستخدم :",
        coerce=int,
        validators=[
            InputRequired(u"يتوجب إختيار دور للمستخدم")])
    submit = SubmitField(u"إضافة مستخدم")

    def __init__(self, *args, **kwargs):
        super(User_a_ar, self).__init__(*args, **kwargs)
        prf = []
        for v in data.Roles.query:
            prf.append((v.id, v.name))
        self.role.choices = prf


# Multimedia upload form

class Multimedia(FlaskForm):
    mf = FileField("Select multimedia file :", validators=[
        FileAllowed(mdal[0] + mdal[1] + mdal[2],
                    'make sure you followed the given conditions !')])
    submit = SubmitField("Upload")


class Multimedia_ar(FlaskForm):
    mf = FileField(u"إختار ملف وسائط متعددة :", validators=[
        FileAllowed(
            mdal[0] + mdal[1] + mdal[2],
            u'تأكد من تتبع التعليمات الواردة بخصوص الملفات المسموح بها')])
    submit = SubmitField(u"إرفع الملف")


# Add name to ticket form

class Touch_name(FlaskForm):
    name = StringField("Full name : ",
                       validators=[InputRequired
                                   ("Required not less than " +
                                    "5 nor more than 300 letters"),
                                   Length(5, 300)])
    submit = SubmitField("Register")


class Touch_name_ar(FlaskForm):
    name = StringField(
        u"أدخل الإسم الكامل :",
        validators=[
            InputRequired(
                u"الحد الأدنى 5 حروف و الحد الأقصى 300 حرف"),
            Length(5, 300)])
    submit = SubmitField(u"تسجيل")


# Download CSV form ------

class CSV(FlaskForm):
    table = SelectField("Select table to download its csv :",
                        choices=[("User", "Users"),
                                 ("Roles", "Roles of usesrs"),
                                 ("Office", "Offices"),
                                 ("Task", "Tasks"),
                                 ("Serial", "Tickets"),
                                 ("Waiting", "Witing tickets")],
                        coerce=str)
    submit = SubmitField("Extract table")


class CSV_ar(FlaskForm):
    table = SelectField(u"إختار جدول بيانات , لتتحصل على ملفه النصي :",
                        choices=[("User", u"مستخدمين"),
                                 ("Roles", u"أدوار المستخدمين"),
                                 ("Office", u"المكاتب"),
                                 ("Task", u"المهمات"),
                                 ("Serial", u"التذاكر"),
                                 ("Waiting", u"تذاكر الإنتضار")],
                        coerce=str)
    submit = SubmitField(u"إستخرج جدول البيانات")

# Templates form


class Templates(FlaskForm):
    touch = SelectField("Select a template for Touch screen :",
                        choices=tms,
                        coerce=int)
    display = SelectField("Select a template for Display screen :",
                          choices=tms,
                          coerce=int)
    submit = SubmitField("Update templates")


class Templates_ar(FlaskForm):
    touch = SelectField(u"إختار قالب للشاشة اللمس :",
                        choices=tar,
                        coerce=int)
    display = SelectField(u"إختار قالب للشاشة العرض :",
                          choices=tar,
                          coerce=int)
    submit = SubmitField(u"إعداد القوالب")


# Updating admin form

class U_admin(FlaskForm):
    password = PasswordField("Enter password : ", validators=[
        InputRequired("Password must be at least " +
                      " of 5 and at most 15 letters .."),
        Length(5, 15)])
    submit = SubmitField('Update Admin')


class U_admin_ar(FlaskForm):
    password = PasswordField(
        u"أدخل كلمة سر :",
        validators=[
            InputRequired(
                u"الحد الأدنى 5 حروف و الحد الأقصى 15 حرف"),
            Length(5, 15)])
    submit = SubmitField(u'تحديث حساب المدير')


# Settings form

class Settings_f(FlaskForm):
    ar_d = IntegerField('Enter a duration for auto reload in seconds : ',
                        validators=[
                            InputRequired("Must be in-between 1 to 100"),
                            NumberRange(1, 100)])
    submit = SubmitField('Set settings')


class Settings_f_ar(FlaskForm):
    ar_d = IntegerField(
        u'أدخل الوقت المحدد بالثواني : ',
        validators=[
            InputRequired(u"الحد الأدنى 1 و الحد الأقصى 100"),
            NumberRange(1, 100)])
    submit = SubmitField(u'تعديل')


# Video form

class Video(FlaskForm):
    video = SelectField("Select uploaded video to use : ",
                        coerce=int, validators=[
                            InputRequired(
                                "You must select a video " +
                                " to be used ..")])
    enable = SelectField("Enable or disable video : ",
                         choices=[(2, 'Disable'),
                                  (1, 'Enable')],
                         validators=[InputRequired()],
                         coerce=int)
    ar = SelectField("Auto replaying the video : ",
                     choices=[(2, 'Disable'),
                              (1, 'Enable')],
                     validators=[InputRequired()],
                     coerce=int)
    controls = SelectField("Enable or disable video controls : ",
                           choices=[(2, 'Disable'), (1, 'Enable')],
                           validators=[InputRequired()],
                           coerce=int)
    mute = SelectField("Mute sound : ",
                       choices=[(2, 'Disable'),
                                (1, 'Enable')],
                       validators=[InputRequired()],
                       coerce=int)
    submit = SubmitField('Set video')

    def __init__(self, *args, **kwargs):
        super(Video, self).__init__(*args, **kwargs)
        vds = []
        if data.Media.query.filter_by(vid=True).count() >= 1:
            for v in data.Media.query.filter_by(vid=True):
                vds.append((v.id, str(v.id) + ".  " + v.name))
            vds.append((00, "Do not assign video .."))
        else:
            vds.append((00, "No videos were found .."))
        self.video.choices = vds


class Video_ar(FlaskForm):
    video = SelectField(
        u"إختار ملف فيديو مرفوع :",
        coerce=int,
        validators=[
            InputRequired(
                u"يجب إختيار ملف فيديو")])
    enable = SelectField(
        u"تفعيل أو تعطيل عرض الفيديو :",
        choices=[(2, u'تعطيل'),
                 (1, u'تفعيل')],
        validators=[InputRequired()],
        coerce=int)
    ar = SelectField(u"إعادة تشغيل الفيديو تلقائياً :",
                     choices=[(2, u'تعطيل'),
                              (1, u'تفعيل')],
                     validators=[InputRequired()],
                     coerce=int)
    controls = SelectField(
        u"تفعيل أو تعطيل لوحة تحكم الفيديو :",
        choices=[(2, u'تعطيل'),
                 (1, u'تفعيل')],
        validators=[InputRequired()],
        coerce=int)
    mute = SelectField(
        u"تعطيل أو تفعيل صوت الفيديو :",
        choices=[(2, u'تفعيل'),
                 (1, u'تعطيل')],
        validators=[InputRequired()], coerce=int)
    submit = SubmitField(u'إعداد عرض الفيديو')

    def __init__(self, *args, **kwargs):
        super(Video_ar, self).__init__(*args, **kwargs)
        vds = []
        if data.Media.query.filter_by(vid=True).count() >= 1:
            for v in data.Media.query.filter_by(vid=True):
                vds.append((v.id, str(v.id) + ".  " + v.name))
            vds.append((00, u"لا تستخدم أي فيديو"))
        else:
            vds.append((00, u"لا يوجد أي ملف فيديو مرفوع"))
        self.video.choices = vds


# Printers form

class Printer_f(FlaskForm):
    kind = SelectField("Select type of ticket to use : ",
                       choices=[(1, 'Registered'),
                                (2, 'Printed')],
                       coerce=int)
    langu = SelectField("Select language of printed ticket : ",
                        choices=[
                            (1, 'English'),
                            (2, 'Arabic')],
                        coerce=int)
    printers = SelectField('Select a usb printer : ',
                           coerce=str)
    submit = SubmitField('Set ticket')

    def __init__(self, vv, *args, **kwargs):
        super(Printer_f, self).__init__(*args, **kwargs)
        prt = []
        listp = vv
        if len(listp) >= 1:
            for v in listp:
                if name == 'nt':
                    prt.append((str(v), 'Printer Name: ' + str(v)))
                else:
                    ful = str(v[0]) + '_' + str(v[1])
                    ful += '_' + str(v[2]) + '_' + str(v[3])
                    prt.append((ful,
                                'Printer ID : ' + str(v[0]) + '_' + str(v[1])))
        else:
            prt.append(('00', "No printers were found .."))
        self.printers.choices = prt


class Printer_f_ar(FlaskForm):
    kind = SelectField(
        u"إختار نوع التذاكر :",
        choices=[(1, u'مسجلة'),
                 (2, u'مطبوعة')],
        coerce=int)
    langu = SelectField(u"إختر لغة التذكرة المطبوعة :",
                        choices=[
                            (1, u'الإنجليزية'),
                            (2, u'العربية')],
                        coerce=int)
    printers = SelectField(u'إختار طابعة يو أس بي :',
                           coerce=str)
    submit = SubmitField(u'إعداد التذاكر')

    def __init__(self, vv, *args, **kwargs):
        super(Printer_f_ar, self).__init__(*args, **kwargs)
        prt = []
        listp = vv
        if len(listp) >= 1:
            for v in listp:
                if name == 'nt':
                    prt.append((str(v), u'إسم الطابعة : ' + str(v)))
                else:
                    ful = str(v[0]) + '_' + str(v[1])
                    ful += '_' + str(v[2]) + '_' + str(v[3])
                    prt.append((
                        ful,
                        u'رقم الطابعة : ' + str(v[0]) + '_' + str(v[1])))
        else:
            prt.append(('00', u"لا يوجد أي طابعة معرفة "))
        self.printers.choices = prt
