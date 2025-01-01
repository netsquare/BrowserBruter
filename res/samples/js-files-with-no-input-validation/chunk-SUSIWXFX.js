import {
  b as le
}
from'./chunk-HDY5DP2O.js';
import {
  d as F,
  e as Z
}
from'./chunk-5AP4EZAW.js';
import {
  Aa as J,
  Ab as P,
  B as h,
  Bb as ie,
  C as f,
  Cb as ne,
  Db as V,
  Gb as re,
  Jb as oe,
  Ka as $,
  Ma as H,
  N as d,
  Na as E,
  O as g,
  Pb as ae,
  Qa as K,
  Rb as se,
  T as u,
  V as m,
  aa as r,
  ba as n,
  ca as c,
  cd as de,
  eb as Q,
  fa as k,
  fb as X,
  ga as v,
  gb as C,
  ha as p,
  hb as I,
  jb as Y,
  pa as s,
  r as A,
  ra as G,
  s as q,
  sb as L,
  u as S,
  ua as z,
  va as W,
  wa as B,
  wb as ee,
  x,
  y as U,
  yb as _,
  za as T,
  zb as te
}
from'./chunk-EJ5MYF22.js';
import {
  a as N,
  b as D,
  h as j
}
from'./chunk-RVFOIZLJ.js';
var me = (
  () => {
    let o = class o {
      constructor(t, e, l) {
        this.router = t,
        this.commonService = e,
        this.toastr = l,
        this.checkActivity()
      }
      checkActivity() {
        let t = this;
        document.addEventListener('mousemove', () => t.resetLogoutTimer()),
        document.addEventListener('keypress', () => t.resetLogoutTimer()),
        this.startLogoutTimer()
      }
      resetLogoutTimer() {
        clearTimeout(this.logoutTimer),
        this.startLogoutTimer()
      }
      startLogoutTimer() {
        this.logoutTimer = setTimeout(() => this.logoutUser(), 90000000)
      }
      logoutUser() {
        return this.commonService.remove('token'),
        this.router.navigate(['/auth/login']),
        this.toastr.warning('Logout', 'Session expired')
      }
    };
    o.ɵfac = function (e) {
      return new (e || o) (S(C), S(F), S(L))
    },
    o.ɵprov = A({
      token: o,
      factory: o.ɵfac,
      providedIn: 'root'
    });
    let i = o;
    return i
  }
) ();
var xe = () => ({
  'background-image': 'url(assets/images/photos/img2.jpg)'
}),
Ce = i => ({
  'block-cursor': i
});
function be(i, o) {
  return;
}
function ye(i, o) {
  return;
}
function Se(i, o) {
  if (
    i & 1 &&
    (r(0, 'div', 14), u(1, be, 2, 0, 'div', 10) (2, ye, 2, 0, 'div', 10), n()),
    i & 2
  ) {
    let a,
    t,
    e = p(2);
    d(),
    m(
      'ngIf',
      e.validateForm == null ||
      (a = e.validateForm.get('emailId')) == null ||
      a.errors == null ? null : a.errors.email
    ),
    d(),
    m(
      'ngIf',
      (
        e.validateForm == null ||
        (t = e.validateForm.get('emailId')) == null ||
        t.errors == null ? null : t.errors.required
      ) ||
      !e.wrongMailId
    )
  }
}
function ke(i, o) {
  i & 1 &&
  (r(0, 'div'), s(1, 'Password is required.'), n())
}
function Te(i, o) {
  return;
}
function Ee(i, o) {
  if (
    i & 1 &&
    (r(0, 'div', 14), u(1, ke, 2, 0, 'div', 10) (2, Te, 2, 0, 'div', 10), n()),
    i & 2
  ) {
    let a,
    t,
    e = p(2);
    d(),
    m(
      'ngIf',
      (a = e.validateForm.get('password')) == null ||
      a.errors == null ? null : a.errors.required
    ),
    d(),
    m(
      'ngIf',
      (t = e.validateForm.get('password')) == null ||
      t.errors == null ? null : t.errors.minlength
    )
  }
}
function Ie(i, o) {
  i & 1 &&
  c(0, 'span', 26)
}
function Fe(i, o) {
  if (i & 1) {
    let a = k();
    r(0, 'div') (1, 'form', 11) (2, 'div'),
    c(3, 'br'),
    r(4, 'div', 12) (5, 'label', 13),
    s(6, 'Email address'),
    n(),
    r(7, 'span', 14),
    s(8, ' *'),
    n(),
    r(9, 'div'),
    c(10, 'input', 15),
    u(11, Se, 3, 2, 'div', 16),
    n() (),
    r(12, 'div', 12) (13, 'label', 13),
    s(14, 'Password'),
    n(),
    r(15, 'span', 14),
    s(16, ' *'),
    n(),
    r(17, 'div'),
    c(18, 'input', 17),
    u(19, Ee, 3, 2, 'div', 16),
    n() () (),
    r(20, 'div', 18),
    c(21, 'input', 19),
    r(22, 'label', 20),
    s(23, ' Remember me '),
    n() (),
    r(24, 'div') (25, 'button', 21),
    v(
      'click',
      function () {
        h(a);
        let e = p();
        return f(e.getVerificationCode())
      }
    ),
    u(26, Ie, 1, 0, 'span', 22),
    s(27, ' Login '),
    n() (),
    r(28, 'a', 23),
    v(
      'click',
      function () {
        h(a);
        let e = p();
        return f(e.forgetPassword())
      }
    ),
    s(29, 'Forgot password ? Click here'),
    n() (),
    r(30, 'div', 24) (31, 'a', 25),
    v(
      'click',
      function () {
        h(a);
        let e = p();
        return f(e.goToCvss4Calculator('CVSS4'))
      }
    ),
    s(32, 'CVSS4 Calculator'),
    n(),
    s(33, '     '),
    r(34, 'a', 25),
    v(
      'click',
      function () {
        h(a);
        let e = p();
        return f(e.goToRiskCalculator('Risk'))
      }
    ),
    s(35, 'Risk Assessment Calculator '),
    n() () ()
  }
  if (i & 2) {
    let a,
    t,
    e = p();
    d(),
    m('formGroup', e.validateForm),
    d(4),
    m('for', 'emailId'),
    d(6),
    m(
      'ngIf',
      (
        e.validateForm == null ||
        (a = e.validateForm.get('emailId')) == null ? null : a.dirty
      ) &&
      (
        e.validateForm == null ||
        (a = e.validateForm.get('emailId')) == null ? null : a.errors
      ) ||
      (
        e.validateForm == null ||
        (a = e.validateForm.get('emailId')) == null ? null : a.touched
      ) ||
      !e.wrongMailId
    ),
    d(2),
    m('for', 'password'),
    d(6),
    m(
      'ngIf',
      ((t = e.validateForm.get('password')) == null ? null : t.invalid) &&
      (
        ((t = e.validateForm.get('password')) == null ? null : t.dirty) ||
        ((t = e.validateForm.get('password')) == null ? null : t.touched)
      )
    ),
    d(6),
    m('disabled', e.loading),
    d(),
    m('ngIf', e.loading)
  }
}
function Le(i, o) {
  i & 1 &&
  (r(0, 'div'), s(1, 'New password is required.'), n())
}
function Pe(i, o) {
  i & 1 &&
  (
    r(0, 'div'),
    s(1, 'Password should not be less than 12 characters!'),
    n()
  )
}
function Ve(i, o) {
  if (
    i & 1 &&
    (r(0, 'div', 14), u(1, Le, 2, 0, 'div', 10) (2, Pe, 2, 0, 'div', 10), n()),
    i & 2
  ) {
    let a,
    t,
    e = p(2);
    d(),
    m(
      'ngIf',
      (a = e.passwordForm.get('newPassword')) == null ||
      a.errors == null ? null : a.errors.required
    ),
    d(),
    m(
      'ngIf',
      (t = e.passwordForm.get('newPassword')) == null ||
      t.errors == null ? null : t.errors.minlength
    )
  }
}
function Me(i, o) {
  i & 1 &&
  (r(0, 'div'), s(1, 'Confirmation is required.'), n())
}
function Re(i, o) {
  i & 1 &&
  (r(0, 'div'), s(1, 'Passwords do not match.'), n())
}
function Oe(i, o) {
  if (
    i & 1 &&
    (r(0, 'div', 14), u(1, Me, 2, 0, 'div', 10) (2, Re, 2, 0, 'div', 10), n()),
    i & 2
  ) {
    let a,
    t,
    e = p(2);
    d(),
    m(
      'ngIf',
      (a = e.passwordForm.get('confirm')) == null ||
      a.errors == null ? null : a.errors.required
    ),
    d(),
    m(
      'ngIf',
      (t = e.passwordForm.get('confirm')) == null ||
      t.errors == null ? null : t.errors.mismatch
    )
  }
}
function Ne(i, o) {
  if (i & 1) {
    let a = k();
    r(0, 'div') (1, 'h5', 9),
    s(2, 'Set your new password'),
    n(),
    r(3, 'form', 11) (4, 'div', 12) (5, 'label', 27),
    s(6, 'New Password'),
    n(),
    r(7, 'span', 14),
    s(8, ' *'),
    n(),
    r(9, 'div', 28),
    c(10, 'input', 29),
    n(),
    u(11, Ve, 3, 2, 'div', 16),
    n(),
    r(12, 'div', 12) (13, 'label', 30),
    s(14, 'Confirm Password'),
    n(),
    r(15, 'span', 14),
    s(16, ' *'),
    n(),
    c(17, 'input', 31),
    u(18, Oe, 3, 2, 'div', 16),
    n() (),
    r(19, 'button', 21),
    v(
      'click',
      function () {
        h(a);
        let e = p();
        return f(e.changePassword())
      }
    ),
    s(20, 'Change password'),
    n() ()
  }
  if (i & 2) {
    let a,
    t,
    e = p();
    d(3),
    m('formGroup', e.passwordForm),
    d(8),
    m(
      'ngIf',
      ((a = e.passwordForm.get('newPassword')) == null ? null : a.invalid) &&
      (
        ((a = e.passwordForm.get('newPassword')) == null ? null : a.dirty) ||
        ((a = e.passwordForm.get('newPassword')) == null ? null : a.touched)
      )
    ),
    d(7),
    m(
      'ngIf',
      ((t = e.passwordForm.get('confirm')) == null ? null : t.invalid) &&
      (
        ((t = e.passwordForm.get('confirm')) == null ? null : t.dirty) ||
        ((t = e.passwordForm.get('confirm')) == null ? null : t.touched)
      )
    ),
    d(),
    m('disabled', e.passwordForm.invalid)
  }
}
function De(i, o) {
  i & 1 &&
  (r(0, 'div'), s(1, 'Enter your OTP!'), n())
}
function je(i, o) {
  if (i & 1 && (r(0, 'div', 14), u(1, De, 2, 0, 'div', 10), n()), i & 2) {
    let a = p(2);
    d(),
    m('ngIf', a.otp_input)
  }
}
function Ae(i, o) {
  i & 1 &&
  (
    r(0, 'div', 14) (1, 'div'),
    s(2, 'Enter valid verification code'),
    n() ()
  )
}
function qe(i, o) {
  i & 1 &&
  c(0, 'span', 26)
}
function Ue(i, o) {
  if (i & 1) {
    let a = k();
    r(0, 'div') (1, 'div'),
    c(2, 'br'),
    r(3, 'div', 12) (4, 'h5', 9),
    s(5, '2-Step Verification.'),
    n(),
    r(6, 'div') (7, 'label', 13),
    s(8, 'Verification Code'),
    n(),
    r(9, 'span', 14),
    s(10, ' *'),
    n(),
    r(11, 'input', 32),
    B(
      'ngModelChange',
      function (e) {
        h(a);
        let l = p();
        return W(l.otp_input, e) ||
        (l.otp_input = e),
        f(e)
      }
    ),
    v(
      'keydown.enter',
      function () {
        h(a);
        let e = p();
        return f(e.submitForm())
      }
    ),
    n(),
    u(12, je, 2, 1, 'div', 16),
    n(),
    u(13, Ae, 3, 0, 'div', 16),
    c(14, 'br'),
    r(15, 'div', 33) (16, 'p'),
    s(17),
    n(),
    c(18, 'br'),
    r(19, 'div', 34) (20, 'button', 35),
    v('click', function () {
      h(a);
      let e = p();
      return f(e.resendCode())
    }),
    s(21, ' Resend code '),
    n() () () () (),
    r(22, 'div') (23, 'button', 21),
    v('click', function () {
      h(a);
      let e = p();
      return f(e.submitForm())
    }),
    u(24, qe, 1, 0, 'span', 22),
    s(25, ' Login'),
    n() () ()
  }
  if (i & 2) {
    let a = p();
    d(7),
    m('for', 'emailId'),
    d(4),
    z('ngModel', a.otp_input),
    d(),
    m('ngIf', !a.otp_input),
    d(),
    m('ngIf', !a.wrongCode),
    d(4),
    G('Resend code in ', a.display, ' seconds'),
    d(2),
    m('ngClass', J(9, Ce, a.resendOtp)),
    d(),
    m('disabled', a.resendOtp),
    d(3),
    m('disabled', !a.validateForm.valid),
    d(),
    m('ngIf', a.loading)
  }
}
var ce = (
  () => {
    let o = class o {
      constructor(t, e, l, w, b, y, R, ge) {
        this.router = t,
        this.route = e,
        this.fb = l,
        this.authService = w,
        this.commonService = b,
        this.autoLogoutService = y,
        this.toastr = R,
        this.recaptchaV3Service = ge,
        this.isFirstTime = !1,
        this.isSecondTime = !1,
        this.display = '',
        this.isTokens = !1,
        this.otp_input = void 0,
        this.passwordVisible = !1,
        this.status = !0,
        this.wrongCode = !0,
        this.wrongMailId = !0,
        this.recaptchaStatus = !1,
        this.grecaptchaToken = '',
        this.loading = !1,
        this.isglobalData = !1,
        this.log = [],
        this.resendOtp = !0,
        this.displayTimer = !1
      }
      ngOnInit() {
        localStorage.clear(),
        this.executeRecaptchaV3(),
        this.returnUrl = this.route.snapshot.queryParams.returnUrl ||
        '/',
        this.validateForm = this.fb.group({
          emailId: [
            '',
            [
              _.email,
              _.required
            ]
          ],
          password: [
            '',
            [
              _.required,
              _.minLength(12)
            ]
          ]
        }),
        this.passwordForm = this.fb.group({
          newPassword: [
            '',
            [
              _.required,
              _.minLength(12)
            ]
          ],
          confirm: [
            '',
            [
              _.required
            ]
          ]
        }, {
          validator: this.passwordMatchValidator
        })
      }
      executeRecaptchaV3() {
        this.loading = !0,
        this.log.push('Recaptcha v3 execution requested...'),
        this.recaptchaV3Service.execute('myAction').subscribe({
          next: t => {
            this.grecaptchaToken = t,
            this.loading = !1
          },
          error: t => {
            this.loading = !1
          }
        })
      }
      passwordMatchValidator(t) {
        let e = t.get('newPassword').value,
        l = t.get('confirm').value;
        e !== l ? t.get('confirm').setErrors({
          mismatch: !0
        }) : t.get('confirm').setErrors(null)
      }
      broadcastAuthChange() {
        window.dispatchEvent(new Event('authChange'))
      }
      submitForm() {
        if (this.loading = !0, this.validateForm.valid) {
          let t = {
            emailId: this.validateForm.value.emailId,
            password: this.validateForm.value.password,
            code: this.otp_input,
            grecaptchaToken: this.grecaptchaToken
          };
          this.authService.Login(t).subscribe({
            next: e => j(
              this,
              null,
              function * () {
                if (e.status === !0) {
                  if (
                    this.commonService.create('token', e.token),
                    this.autoLogoutService.startLogoutTimer(),
                    this.broadcastAuthChange(),
                    this.wrongCode = e.status,
                    yield this.globalData(),
                    this.isglobalData
                  ) {
                    this.loading = !1,
                    this.toastr.success(e.message, 'Login'),
                    this.router.navigate(['/main/dashboard']);
                    return
                  }
                } else return
              }
            ),
            error: e => (
              this.wrongCode = e.error.status,
              this.executeRecaptchaV3(),
              this.loading = !1,
              this.toastr.error(e.error.message, 'Login')
            )
          })
        } else Object.values(this.validateForm.controls).forEach(
          t => {
            t.invalid &&
            (t.markAsDirty(), t.updateValueAndValidity({
              onlySelf: !0
            }))
          }
        )
      }
      globalData() {
        return new Promise(
          (t, e) => {
            this.authService.GetUserGlobalData().subscribe({
              next: l => {
                l.status === !0 ? (
                  this.isglobalData = l.status,
                  this.commonService.setItem('access-data', JSON.stringify(l.data)),
                  t()
                ) : e('Error: Status is not true')
              },
              error: l => {
                e(l)
              }
            })
          }
        )
      }
      getVerificationCode() {
        let t = !1;
        if (this.validateForm?.valid) {
          this.loading = !0;
          let e = D(
            N({
            }, this.validateForm.value),
            {
              isLogin: !0,
              grecaptchaToken: this.grecaptchaToken
            }
          );
          this.authService.GetVerificationCode(e).subscribe({
            next: l => {
              if (l.status === !0) {
                let w = l.firstTimeLogin;
                this.status = l.status,
                this.resendOtp = !l.status,
                this.executeRecaptchaV3(),
                w ? (this.isFirstTime = w, this.passwordForm.reset()) : this.isSecondTime = !0,
                this.isTokens = !0,
                this.startTimer(1),
                this.loading = !1,
                this.toastr.success(l.message, 'Verification Code')
              }
            },
            error: l => (
              l.error.message == 'Invalid email address.' ? this.wrongMailId = l.error.status : this.wrongMailId = !0,
              l.error.message == 'Incorrect password.' ? this.status = l.error.status : this.status = !0,
              this.executeRecaptchaV3(),
              this.loading = !1,
              this.resendOtp = !0,
              this.toastr.error(l.error.message, 'Login')
            )
          })
        } else Object.values(this.validateForm.controls).forEach(
          e => {
            e.invalid &&
            (e.markAsDirty(), e.updateValueAndValidity({
              onlySelf: !0
            }), t = !0)
          }
        ),
        t &&
        this.toastr.warning('Please verify all required fields', 'Login')
      }
      changePassword() {
        let t = {
          emailId: this.validateForm.value.emailId,
          oldPassword: this.validateForm.value.password,
          newPassword: this.passwordForm.value.newPassword,
          grecaptchaToken: this.grecaptchaToken
        };
        this.authService.ChangePassword(t).subscribe({
          next: e => {
            e.status === !0 &&
            (
              this.isFirstTime = !1,
              this.isSecondTime = !1,
              this.validateForm.reset(),
              this.executeRecaptchaV3(),
              this.toastr.success(e.message, 'Change Password')
            )
          },
          error: e => (
            this.executeRecaptchaV3(),
            this.toastr.error(e.error.message, 'Login')
          )
        })
      }
      startTimer(t) {
        this.displayTimer = !0,
        this.resendOtp = !0;
        let e = t * 120,
        l = t < 10 ? '0' : '',
        w = setInterval(
          () => {
            e--;
            let b = Math.floor(e / 60),
            y = e % 60,
            R = y < 10 ? '0' + y : y;
            this.display = `${ l }${ b }:${ R }`,
            e === 0 &&
            (clearInterval(w), this.resendOtp = !1, this.displayTimer = !1)
          },
          1000
        )
      }
      resendCode() {
        clearTimeout(1),
        this.getVerificationCode()
      }
      forgetPassword() {
        let t = this.validateForm.get('emailId');
        if (t.invalid) {
          t.errors?.required ? (t.markAsDirty(), t.updateValueAndValidity({
            onlySelf: !0
          })) : t.errors?.email &&
          (t.markAsDirty(), t.updateValueAndValidity({
            onlySelf: !0
          }));
          return
        }
        let e = {
          emailId: this.validateForm.value.emailId,
          grecaptchaToken: this.grecaptchaToken
        };
        this.authService.ForgetPasswrod(e).subscribe({
          next: l => {
            l.status === !0 &&
            this.toastr.success(l.message, 'Forget Password')
          },
          error: l => (
            this.executeRecaptchaV3(),
            this.toastr.error(l.error.message, 'Forget Password')
          )
        })
      }
      goToRiskCalculator(t) {
        this.router.navigate(['/calculators/risk_assessment_calculator'])
      }
      goToCvss4Calculator(t) {
        this.router.navigate(['/calculators/cvss4_calculator'])
      }
    };
    o.ɵfac = function (e) {
      return new (e || o) (g(C), g(Q), g(se), g(Z), g(F), g(me), g(L), g(le))
    },
    o.ɵcmp = x({
      type: o,
      selectors: [
        ['app-login']
      ],
      decls: 17,
      vars: 5,
      consts: [
        [1,
        'row',
        'w-100',
        'mx-0',
        'auth-page'],
        [
          1,
          'col-md-8',
          'col-xl-6',
          'mx-auto'
        ],
        [
          1,
          'card'
        ],
        [
          1,
          'row'
        ],
        [
          1,
          'col-md-4',
          'pe-md-0'
        ],
        [
          1,
          'auth-side-wrapper',
          3,
          'ngStyle'
        ],
        [
          1,
          'col-md-8',
          'ps-md-0'
        ],
        [
          1,
          'auth-form-wrapper',
          'px-4',
          'py-5'
        ],
        [
          'routerLink',
          '.',
          1,
          'nobleui-logo',
          'logo-light',
          'd-block',
          'mb-2'
        ],
        [
          1,
          'text-muted',
          'fw-normal',
          'mb-4'
        ],
        [
          4,
          'ngIf'
        ],
        [
          1,
          'login-form',
          3,
          'formGroup'
        ],
        [
          1,
          'mb-3'
        ],
        [
          1,
          'form-label',
          3,
          'for'
        ],
        [
          1,
          'text-danger'
        ],
        [
          'formControlName',
          'emailId',
          'id',
          'emailId',
          'placeholder',
          'Enter Email-ID',
          'type',
          'email',
          1,
          'form-control'
        ],
        [
          'class',
          'text-danger',
          4,
          'ngIf'
        ],
        [
          'formControlName',
          'password',
          'id',
          'password',
          'placeholder',
          'Enter password',
          'type',
          'password',
          'minlength',
          '12',
          1,
          'form-control'
        ],
        [
          1,
          'form-check',
          'mb-3'
        ],
        [
          'type',
          'checkbox',
          'id',
          'authCheck',
          1,
          'form-check-input'
        ],
        [
          'for',
          'authCheck',
          1,
          'form-check-label'
        ],
        [
          'type',
          'submit',
          1,
          'btn',
          'btn-primary',
          'btn-sm',
          'me-2',
          'mb-2',
          'mb-md-0',
          3,
          'click',
          'disabled'
        ],
        [
          'class',
          'spinner-grow spinner-grow-sm',
          'role',
          'status',
          'aria-hidden',
          'true',
          4,
          'ngIf'
        ],
        [
          1,
          'd-block',
          'mt-3',
          'text-muted',
          3,
          'click'
        ],
        [
          1,
          'd-flex'
        ],
        [
          1,
          'd-block',
          'mt-3',
          3,
          'click'
        ],
        [
          'role',
          'status',
          'aria-hidden',
          'true',
          1,
          'spinner-grow',
          'spinner-grow-sm'
        ],
        [
          'for',
          'newPassword',
          1,
          'form-label'
        ],
        [
          1,
          'input-group'
        ],
        [
          'id',
          'newPassword',
          'name',
          'newPassword',
          'placeholder',
          'New password',
          'type',
          'password',
          'minlength',
          '12',
          'formControlName',
          'newPassword',
          1,
          'form-control'
        ],
        [
          'for',
          'confirmPassword',
          1,
          'form-label'
        ],
        [
          'type',
          'password',
          'id',
          'confirmPassword',
          'name',
          'confirmPassword',
          'placeholder',
          'Confirm password',
          'formControlName',
          'confirm',
          1,
          'form-control'
        ],
        [
          'type',
          'text',
          'placeholder',
          'Enter your verification code',
          1,
          'form-control',
          3,
          'ngModelChange',
          'keydown.enter',
          'ngModel'
        ],
        [
          1,
          'textCenter'
        ],
        [
          1,
          'd-inline-block',
          3,
          'ngClass'
        ],
        [
          'type',
          'button',
          1,
          'btn',
          'btn-outline-primary',
          'btn-sm',
          'mb-1',
          'mb-md-0',
          3,
          'click',
          'disabled'
        ]
      ],
      template: function (e, l) {
        e & 1 &&
        (
          r(0, 'div', 0) (1, 'div', 1) (2, 'div', 2) (3, 'div', 3) (4, 'div', 4),
          c(5, 'div', 5),
          n(),
          r(6, 'div', 6) (7, 'div', 7) (8, 'a', 8),
          s(9, 'N'),
          r(10, 'span'),
          s(11, 'STAR'),
          n() (),
          r(12, 'h5', 9),
          s(13, 'Welcome back! Log in to your account.'),
          n(),
          u(14, Fe, 36, 7, 'div', 10) (15, Ne, 21, 4, 'div', 10) (16, Ue, 26, 11, 'div', 10),
          n() () () () () ()
        ),
        e & 2 &&
        (
          d(5),
          m('ngStyle', T(4, xe)),
          d(9),
          m('ngIf', !l.isSecondTime && !l.isFirstTime),
          d(),
          m('ngIf', l.isFirstTime),
          d(),
          m('ngIf', l.isSecondTime)
        )
      },
      dependencies: [
        $,
        H,
        E,
        V,
        ee,
        te,
        P,
        ae,
        ne,
        re,
        oe,
        I
      ],
      styles: [
        '[_nghost-%COMP%]{height:100vh;display:flex;align-items:center;justify-content:center}.auth-side-wrapper[_ngcontent-%COMP%]{width:100%;height:100%;background-size:cover}.text-muted[_ngcontent-%COMP%], .dropzone.dz-clickable[_ngcontent-%COMP%]   .dz-message[_ngcontent-%COMP%]   *[_ngcontent-%COMP%]{--bs-text-opacity: 1;color:#7987a1!important}.fw-normal[_ngcontent-%COMP%]{font-weight:400!important}.mb-4[_ngcontent-%COMP%]{margin-bottom:1.5rem!important}.h[_ngcontent-%COMP%]{height:45vh}.block-cursor[_ngcontent-%COMP%]{cursor:not-allowed!important}.no-pointer[_ngcontent-%COMP%]{pointer-events:none}.d-inline-block[_ngcontent-%COMP%]{display:inline-block!important}'
      ]
    });
    let i = o;
    return i
  }
) ();
var Ge = () => ({
  'background-image': 'url(https://via.placeholder.com/219x452)'
}),
pe = (
  () => {
    let o = class o {
      constructor(t) {
        this.router = t
      }
      ngOnInit() {
      }
      onRegister(t) {
        t.preventDefault(),
        localStorage.setItem('isLoggedin', 'true'),
        localStorage.getItem('isLoggedin') &&
        this.router.navigate(['/'])
      }
    };
    o.ɵfac = function (e) {
      return new (e || o) (g(C))
    },
    o.ɵcmp = x({
      type: o,
      selectors: [
        ['app-register']
      ],
      decls: 39,
      vars: 2,
      consts: [
        [1,
        'row',
        'w-100',
        'mx-0',
        'auth-page'],
        [
          1,
          'col-md-8',
          'col-xl-6',
          'mx-auto'
        ],
        [
          1,
          'card'
        ],
        [
          1,
          'row'
        ],
        [
          1,
          'col-md-4',
          'pe-md-0'
        ],
        [
          1,
          'auth-side-wrapper',
          3,
          'ngStyle'
        ],
        [
          1,
          'col-md-8',
          'ps-md-0'
        ],
        [
          1,
          'auth-form-wrapper',
          'px-4',
          'py-5'
        ],
        [
          'routerLink',
          '.',
          1,
          'nobleui-logo',
          'logo-light',
          'd-block',
          'mb-2'
        ],
        [
          1,
          'text-muted',
          'fw-normal',
          'mb-4'
        ],
        [
          1,
          'forms-sample'
        ],
        [
          1,
          'mb-3'
        ],
        [
          'for',
          'exampleInputUsername1',
          1,
          'form-label'
        ],
        [
          'type',
          'text',
          'id',
          'exampleInputUsername1',
          'autocomplete',
          'Username',
          'placeholder',
          'Username',
          1,
          'form-control'
        ],
        [
          'for',
          'exampleInputEmail1',
          1,
          'form-label'
        ],
        [
          'type',
          'email',
          'id',
          'exampleInputEmail1',
          'placeholder',
          'Email',
          1,
          'form-control'
        ],
        [
          'for',
          'exampleInputPassword1',
          1,
          'form-label'
        ],
        [
          'type',
          'password',
          'id',
          'exampleInputPassword1',
          'autocomplete',
          'current-password',
          'placeholder',
          'Password',
          1,
          'form-control'
        ],
        [
          1,
          'form-check',
          'mb-3'
        ],
        [
          'type',
          'checkbox',
          'id',
          'authCheck',
          1,
          'form-check-input'
        ],
        [
          'for',
          'authCheck',
          1,
          'form-check-label'
        ],
        [
          'type',
          'submit',
          1,
          'btn',
          'btn-primary',
          'btn-sm',
          'm-1',
          3,
          'click'
        ],
        [
          'type',
          'button',
          1,
          'btn',
          'btn-outline-primary',
          'btn-sm',
          'm-1'
        ],
        [
          1,
          'feather',
          'icon-twitter',
          'btn-icon-prepend'
        ],
        [
          'routerLink',
          '/auth/login',
          1,
          'd-block',
          'mt-3',
          'text-muted'
        ]
      ],
      template: function (e, l) {
        e & 1 &&
        (
          r(0, 'div', 0) (1, 'div', 1) (2, 'div', 2) (3, 'div', 3) (4, 'div', 4),
          c(5, 'div', 5),
          n(),
          r(6, 'div', 6) (7, 'div', 7) (8, 'a', 8),
          s(9, 'Noble'),
          r(10, 'span'),
          s(11, 'UI'),
          n() (),
          r(12, 'h5', 9),
          s(13, 'Create a free account.'),
          n(),
          r(14, 'form', 10) (15, 'div', 11) (16, 'label', 12),
          s(17, 'Username'),
          n(),
          c(18, 'input', 13),
          n(),
          r(19, 'div', 11) (20, 'label', 14),
          s(21, 'Email address'),
          n(),
          c(22, 'input', 15),
          n(),
          r(23, 'div', 11) (24, 'label', 16),
          s(25, 'Password'),
          n(),
          c(26, 'input', 17),
          n(),
          r(27, 'div', 18),
          c(28, 'input', 19),
          r(29, 'label', 20),
          s(30, ' Remember me '),
          n() (),
          r(31, 'div') (32, 'button', 21),
          v('click', function (b) {
            return l.onRegister(b)
          }),
          s(33, 'Sign up'),
          n(),
          r(34, 'button', 22),
          c(35, 'i', 23),
          s(36, ' Sign up with twitter '),
          n() (),
          r(37, 'a', 24),
          s(38, 'Already a user? Sign in'),
          n() () () () () () () ()
        ),
        e & 2 &&
        (d(5), m('ngStyle', T(1, Ge)))
      },
      dependencies: [
        E,
        V,
        P,
        ie,
        I
      ],
      styles: [
        '[_nghost-%COMP%]{height:100vh;display:flex;align-items:center;justify-content:center}'
      ]
    });
    let i = o;
    return i
  }
) ();
var ue = (
  () => {
    let o = class o {
      constructor() {
      }
      ngOnInit() {
      }
    };
    o.ɵfac = function (e) {
      return new (e || o)
    },
    o.ɵcmp = x({
      type: o,
      selectors: [
        ['app-auth']
      ],
      decls: 1,
      vars: 0,
      template: function (e, l) {
        e & 1 &&
        c(0, 'router-outlet')
      },
      dependencies: [
        X
      ],
      encapsulation: 2
    });
    let i = o;
    return i
  }
) ();
var ze = [
  {
    path: '',
    component: ue,
    children: [
      {
        path: '',
        redirectTo: 'login',
        pathMatch: 'full'
      },
      {
        path: 'login',
        component: ce
      },
      {
        path: 'register',
        component: pe
      }
    ]
  }
],
nt = (
  () => {
    let o = class o {
    };
    o.ɵfac = function (e) {
      return new (e || o)
    },
    o.ɵmod = U({
      type: o
    }),
    o.ɵinj = q({
      imports: [
        K,
        de,
        Y.forChild(ze)
      ]
    });
    let i = o;
    return i
  }
) ();
export {
  nt as AuthModule
};
