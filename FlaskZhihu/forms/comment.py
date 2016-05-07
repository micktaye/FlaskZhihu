# -*- coding: utf-8 -*-
__author__ = 'shn7798'

from flask.ext.wtf import Form
from wtforms import TextAreaField, SubmitField, HiddenField
from wtforms.validators import required

__all__ = ['CommentAddForm']


class CommentAddForm(Form):
    target_type = HiddenField(validators=[required(message=u'请输入评论类型')])
    target_id = HiddenField(validators=[required(message=u'请输入评论所属ID')])
    content = TextAreaField(validators=[required(message=u'请输入内容')])