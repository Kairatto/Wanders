import React from 'react';
import style from './style.module.css'

const EmailMssg = () => {
    return (
        <div className={style.wrapBox} >
            <div className={style.grayBox}>
                <p >Привет ✌🏻</p>
                <p>это Wanders</p>
            </div>
            <p className={style.star}>✨</p>
            <div className={style.grayBox}>
                <p className={style.grayBoxItem}>Спасибо <br /> за регистрацию!</p>
                <p className={style.grayBoxDesc}>
                    Осталось совсем немного.
                </p>
                <p className={style.grayBoxDesc}>Для завершении регистрации необходимо перейти по кнопке ниже, чтобы активировать аккаунт.</p>
                <button className={style.emailButton}>Активировать аккаунт</button>
            </div>
            <p className={style.desc}>Вы получили это письмо, поскольку указали свой почтовый адрес при регистрации</p>
        </div>
    );
};

export default EmailMssg;