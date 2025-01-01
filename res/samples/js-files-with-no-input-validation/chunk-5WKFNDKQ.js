import {
  AuthService,
  CommonService
} from "/chunk-RTM3KQT4.js";
import {
  SharedModule,
  __async,
  __spreadProps,
  __spreadValues
} from "/chunk-2CBLJUUC.js";

// src/app/auth/auth.module.ts
import { NgModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { CommonModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";

// src/app/auth/login/login.component.ts
import { Component } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { Validators } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i02 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i12 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i2 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";

// src/app/services/auto-logout.service.ts
import { Injectable } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i0 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i1 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i3 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";
var _AutoLogoutService = class _AutoLogoutService {
  constructor(router, commonService, toastr) {
    this.router = router;
    this.commonService = commonService;
    this.toastr = toastr;
    this.checkActivity();
  }
  checkActivity() {
    const self = this;
    document.addEventListener("mousemove", () => self.resetLogoutTimer());
    document.addEventListener("keypress", () => self.resetLogoutTimer());
    this.startLogoutTimer();
  }
  resetLogoutTimer() {
    clearTimeout(this.logoutTimer);
    this.startLogoutTimer();
  }
  startLogoutTimer() {
    const timeout = 1500 * 60 * 1e3;
    this.logoutTimer = setTimeout(() => this.logoutUser(), timeout);
  }
  logoutUser() {
    this.commonService.remove("token");
    this.router.navigate(["/auth/login"]);
    return this.toastr.warning("Logout", "Session expired");
  }
};
_AutoLogoutService.\u0275fac = function AutoLogoutService_Factory(t) {
  return new (t || _AutoLogoutService)(i0.\u0275\u0275inject(i1.Router), i0.\u0275\u0275inject(CommonService), i0.\u0275\u0275inject(i3.ToastrService));
};
_AutoLogoutService.\u0275prov = /* @__PURE__ */ i0.\u0275\u0275defineInjectable({ token: _AutoLogoutService, factory: _AutoLogoutService.\u0275fac, providedIn: "root" });
var AutoLogoutService = _AutoLogoutService;

// src/app/auth/login/login.component.ts
import * as i6 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";
import * as i7 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-recaptcha.js?v=ca23e844";
import * as i8 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
var _c0 = () => ({ "background-image": "url(assets/images/photos/img2.jpg)" });
var _c1 = (a0) => ({ "block-cursor": a0 });
function LoginComponent_div_14_div_11_div_1_Template(rf, ctx) {
return;
}
function LoginComponent_div_14_div_11_div_2_Template(rf, ctx) {
return;
}
function LoginComponent_div_14_div_11_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 14);
    i02.\u0275\u0275template(1, LoginComponent_div_14_div_11_div_1_Template, 2, 0, "div", 10)(2, LoginComponent_div_14_div_11_div_2_Template, 2, 0, "div", 10);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    const ctx_r1 = i02.\u0275\u0275nextContext(2);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r1.validateForm == null ? null : (tmp_2_0 = ctx_r1.validateForm.get("emailId")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["email"]);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx_r1.validateForm == null ? null : (tmp_3_0 = ctx_r1.validateForm.get("emailId")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["required"]) || !ctx_r1.wrongMailId);
  }
}
function LoginComponent_div_14_div_19_div_1_Template(rf, ctx) {
  return;
}
function LoginComponent_div_14_div_19_div_2_Template(rf, ctx) {
 return;
}
function LoginComponent_div_14_div_19_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 14);
    i02.\u0275\u0275template(1, LoginComponent_div_14_div_19_div_1_Template, 2, 0, "div", 10)(2, LoginComponent_div_14_div_19_div_2_Template, 2, 0, "div", 10);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    const ctx_r1 = i02.\u0275\u0275nextContext(2);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_2_0 = ctx_r1.validateForm.get("password")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_3_0 = ctx_r1.validateForm.get("password")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["minlength"]);
  }
}
function LoginComponent_div_14_span_26_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275element(0, "span", 26);
  }
}
function LoginComponent_div_14_Template(rf, ctx) {
  if (rf & 1) {
    const _r1 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div")(1, "form", 11)(2, "div");
    i02.\u0275\u0275element(3, "br");
    i02.\u0275\u0275elementStart(4, "div", 12)(5, "label", 13);
    i02.\u0275\u0275text(6, "Email address");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(7, "span", 14);
    i02.\u0275\u0275text(8, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(9, "div");
    i02.\u0275\u0275element(10, "input", 15);
    i02.\u0275\u0275template(11, LoginComponent_div_14_div_11_Template, 3, 2, "div", 16);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(12, "div", 12)(13, "label", 13);
    i02.\u0275\u0275text(14, "Password");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(15, "span", 14);
    i02.\u0275\u0275text(16, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(17, "div");
    i02.\u0275\u0275element(18, "input", 17);
    i02.\u0275\u0275template(19, LoginComponent_div_14_div_19_Template, 3, 2, "div", 16);
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275elementStart(20, "div", 18);
    i02.\u0275\u0275element(21, "input", 19);
    i02.\u0275\u0275elementStart(22, "label", 20);
    i02.\u0275\u0275text(23, " Remember me ");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(24, "div")(25, "button", 21);
    i02.\u0275\u0275listener("click", function LoginComponent_div_14_Template_button_click_25_listener() {
      i02.\u0275\u0275restoreView(_r1);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.getVerificationCode());
    });
    i02.\u0275\u0275template(26, LoginComponent_div_14_span_26_Template, 1, 0, "span", 22);
    i02.\u0275\u0275text(27, " Login ");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(28, "a", 23);
    i02.\u0275\u0275listener("click", function LoginComponent_div_14_Template_a_click_28_listener() {
      i02.\u0275\u0275restoreView(_r1);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.forgetPassword());
    });
    i02.\u0275\u0275text(29, "Forgot password ? Click here");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(30, "div", 24)(31, "a", 25);
    i02.\u0275\u0275listener("click", function LoginComponent_div_14_Template_a_click_31_listener() {
      i02.\u0275\u0275restoreView(_r1);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.goToCvss4Calculator("CVSS4"));
    });
    i02.\u0275\u0275text(32, "CVSS4 Calculator");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275text(33, " \xA0 \xA0 ");
    i02.\u0275\u0275elementStart(34, "a", 25);
    i02.\u0275\u0275listener("click", function LoginComponent_div_14_Template_a_click_34_listener() {
      i02.\u0275\u0275restoreView(_r1);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.goToRiskCalculator("Risk"));
    });
    i02.\u0275\u0275text(35, "Risk Assessment Calculator ");
    i02.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    let tmp_3_0;
    let tmp_5_0;
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("formGroup", ctx_r1.validateForm);
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("for", "emailId");
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("ngIf", (ctx_r1.validateForm == null ? null : (tmp_3_0 = ctx_r1.validateForm.get("emailId")) == null ? null : tmp_3_0.dirty) && (ctx_r1.validateForm == null ? null : (tmp_3_0 = ctx_r1.validateForm.get("emailId")) == null ? null : tmp_3_0.errors) || (ctx_r1.validateForm == null ? null : (tmp_3_0 = ctx_r1.validateForm.get("emailId")) == null ? null : tmp_3_0.touched) || !ctx_r1.wrongMailId);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("for", "password");
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("ngIf", ((tmp_5_0 = ctx_r1.validateForm.get("password")) == null ? null : tmp_5_0.invalid) && (((tmp_5_0 = ctx_r1.validateForm.get("password")) == null ? null : tmp_5_0.dirty) || ((tmp_5_0 = ctx_r1.validateForm.get("password")) == null ? null : tmp_5_0.touched)));
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("disabled", ctx_r1.loading);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r1.loading);
  }
}
function LoginComponent_div_15_div_11_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "New password is required.");
    i02.\u0275\u0275elementEnd();
  }
}
function LoginComponent_div_15_div_11_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Password should not be less than 12 characters!");
    i02.\u0275\u0275elementEnd();
  }
}
function LoginComponent_div_15_div_11_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 14);
    i02.\u0275\u0275template(1, LoginComponent_div_15_div_11_div_1_Template, 2, 0, "div", 10)(2, LoginComponent_div_15_div_11_div_2_Template, 2, 0, "div", 10);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    const ctx_r1 = i02.\u0275\u0275nextContext(2);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_2_0 = ctx_r1.passwordForm.get("newPassword")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_3_0 = ctx_r1.passwordForm.get("newPassword")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["minlength"]);
  }
}
function LoginComponent_div_15_div_18_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Confirmation is required.");
    i02.\u0275\u0275elementEnd();
  }
}
function LoginComponent_div_15_div_18_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Passwords do not match.");
    i02.\u0275\u0275elementEnd();
  }
}
function LoginComponent_div_15_div_18_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 14);
    i02.\u0275\u0275template(1, LoginComponent_div_15_div_18_div_1_Template, 2, 0, "div", 10)(2, LoginComponent_div_15_div_18_div_2_Template, 2, 0, "div", 10);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    const ctx_r1 = i02.\u0275\u0275nextContext(2);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_2_0 = ctx_r1.passwordForm.get("confirm")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_3_0 = ctx_r1.passwordForm.get("confirm")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["mismatch"]);
  }
}
function LoginComponent_div_15_Template(rf, ctx) {
  if (rf & 1) {
    const _r3 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div")(1, "h5", 9);
    i02.\u0275\u0275text(2, "Set your new password");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(3, "form", 11)(4, "div", 12)(5, "label", 27);
    i02.\u0275\u0275text(6, "New Password");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(7, "span", 14);
    i02.\u0275\u0275text(8, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(9, "div", 28);
    i02.\u0275\u0275element(10, "input", 29);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(11, LoginComponent_div_15_div_11_Template, 3, 2, "div", 16);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(12, "div", 12)(13, "label", 30);
    i02.\u0275\u0275text(14, "Confirm Password");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(15, "span", 14);
    i02.\u0275\u0275text(16, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(17, "input", 31);
    i02.\u0275\u0275template(18, LoginComponent_div_15_div_18_Template, 3, 2, "div", 16);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(19, "button", 21);
    i02.\u0275\u0275listener("click", function LoginComponent_div_15_Template_button_click_19_listener() {
      i02.\u0275\u0275restoreView(_r3);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.changePassword());
    });
    i02.\u0275\u0275text(20, "Change password");
    i02.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance(3);
    i02.\u0275\u0275property("formGroup", ctx_r1.passwordForm);
    i02.\u0275\u0275advance(8);
    i02.\u0275\u0275property("ngIf", ((tmp_2_0 = ctx_r1.passwordForm.get("newPassword")) == null ? null : tmp_2_0.invalid) && (((tmp_2_0 = ctx_r1.passwordForm.get("newPassword")) == null ? null : tmp_2_0.dirty) || ((tmp_2_0 = ctx_r1.passwordForm.get("newPassword")) == null ? null : tmp_2_0.touched)));
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275property("ngIf", ((tmp_3_0 = ctx_r1.passwordForm.get("confirm")) == null ? null : tmp_3_0.invalid) && (((tmp_3_0 = ctx_r1.passwordForm.get("confirm")) == null ? null : tmp_3_0.dirty) || ((tmp_3_0 = ctx_r1.passwordForm.get("confirm")) == null ? null : tmp_3_0.touched)));
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("disabled", ctx_r1.passwordForm.invalid);
  }
}
function LoginComponent_div_16_div_12_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Enter your OTP!");
    i02.\u0275\u0275elementEnd();
  }
}
function LoginComponent_div_16_div_12_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 14);
    i02.\u0275\u0275template(1, LoginComponent_div_16_div_12_div_1_Template, 2, 0, "div", 10);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const ctx_r1 = i02.\u0275\u0275nextContext(2);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r1.otp_input);
  }
}
function LoginComponent_div_16_div_13_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 14)(1, "div");
    i02.\u0275\u0275text(2, "Enter valid verification code");
    i02.\u0275\u0275elementEnd()();
  }
}
function LoginComponent_div_16_span_24_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275element(0, "span", 26);
  }
}
function LoginComponent_div_16_Template(rf, ctx) {
  if (rf & 1) {
    const _r4 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div")(1, "div");
    i02.\u0275\u0275element(2, "br");
    i02.\u0275\u0275elementStart(3, "div", 12)(4, "h5", 9);
    i02.\u0275\u0275text(5, "2-Step Verification.");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(6, "div")(7, "label", 13);
    i02.\u0275\u0275text(8, "Verification Code");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(9, "span", 14);
    i02.\u0275\u0275text(10, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(11, "input", 32);
    i02.\u0275\u0275twoWayListener("ngModelChange", function LoginComponent_div_16_Template_input_ngModelChange_11_listener($event) {
      i02.\u0275\u0275restoreView(_r4);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      i02.\u0275\u0275twoWayBindingSet(ctx_r1.otp_input, $event) || (ctx_r1.otp_input = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275listener("keydown.enter", function LoginComponent_div_16_Template_input_keydown_enter_11_listener() {
      i02.\u0275\u0275restoreView(_r4);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.submitForm());
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(12, LoginComponent_div_16_div_12_Template, 2, 1, "div", 16);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(13, LoginComponent_div_16_div_13_Template, 3, 0, "div", 16);
    i02.\u0275\u0275element(14, "br");
    i02.\u0275\u0275elementStart(15, "div", 33)(16, "p");
    i02.\u0275\u0275text(17);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(18, "br");
    i02.\u0275\u0275elementStart(19, "div", 34)(20, "button", 35);
    i02.\u0275\u0275listener("click", function LoginComponent_div_16_Template_button_click_20_listener() {
      i02.\u0275\u0275restoreView(_r4);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.resendCode());
    });
    i02.\u0275\u0275text(21, " Resend code ");
    i02.\u0275\u0275elementEnd()()()()();
    i02.\u0275\u0275elementStart(22, "div")(23, "button", 21);
    i02.\u0275\u0275listener("click", function LoginComponent_div_16_Template_button_click_23_listener() {
      i02.\u0275\u0275restoreView(_r4);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.submitForm());
    });
    i02.\u0275\u0275template(24, LoginComponent_div_16_span_24_Template, 1, 0, "span", 22);
    i02.\u0275\u0275text(25, " Login");
    i02.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275property("for", "emailId");
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx_r1.otp_input);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", !ctx_r1.otp_input);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", !ctx_r1.wrongCode);
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275textInterpolate1("Resend code in ", ctx_r1.display, " seconds");
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("ngClass", i02.\u0275\u0275pureFunction1(9, _c1, ctx_r1.resendOtp));
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("disabled", ctx_r1.resendOtp);
    i02.\u0275\u0275advance(3);
    i02.\u0275\u0275property("disabled", !ctx_r1.validateForm.valid);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r1.loading);
  }
}
var _LoginComponent = class _LoginComponent {
  constructor(router, route, fb, authService, commonService, autoLogoutService, toastr, recaptchaV3Service) {
    this.router = router;
    this.route = route;
    this.fb = fb;
    this.authService = authService;
    this.commonService = commonService;
    this.autoLogoutService = autoLogoutService;
    this.toastr = toastr;
    this.recaptchaV3Service = recaptchaV3Service;
    this.isFirstTime = false;
    this.isSecondTime = false;
    this.display = "";
    this.isTokens = false;
    this.otp_input = void 0;
    this.passwordVisible = false;
    this.status = true;
    this.wrongCode = true;
    this.wrongMailId = true;
    this.recaptchaStatus = false;
    this.grecaptchaToken = "";
    this.loading = false;
    this.isglobalData = false;
    this.log = [];
    this.resendOtp = true;
    this.displayTimer = false;
  }
  ngOnInit() {
    localStorage.clear();
    this.executeRecaptchaV3();
    this.returnUrl = this.route.snapshot.queryParams["returnUrl"] || "/";
    this.validateForm = this.fb.group({
      emailId: ["", [Validators.email, Validators.required]],
      password: ["", [Validators.required, Validators.minLength(12)]]
    });
    this.passwordForm = this.fb.group({
      newPassword: ["", [Validators.required, Validators.minLength(12)]],
      confirm: ["", [Validators.required]]
    }, { validator: this.passwordMatchValidator });
  }
  executeRecaptchaV3() {
    this.loading = true;
    this.log.push(`Recaptcha v3 execution requested...`);
    this.recaptchaV3Service.execute("myAction").subscribe({
      next: (token) => {
        this.grecaptchaToken = token;
        this.loading = false;
      },
      error: (err) => {
        this.loading = false;
        return;
      }
    });
  }
  passwordMatchValidator(formGroup) {
    const newPassword = formGroup.get("newPassword").value;
    const confirm = formGroup.get("confirm").value;
    if (newPassword !== confirm) {
      formGroup.get("confirm").setErrors({ mismatch: true });
    } else {
      formGroup.get("confirm").setErrors(null);
    }
  }
  broadcastAuthChange() {
    window.dispatchEvent(new Event("authChange"));
  }
  submitForm() {
    this.loading = true;
    if (this.validateForm.valid) {
      let obj = {
        emailId: this.validateForm.value.emailId,
        password: this.validateForm.value.password,
        code: this.otp_input,
        grecaptchaToken: this.grecaptchaToken
      };
      this.authService.Login(obj).subscribe({
        next: (response) => __async(this, null, function* () {
          if (response.status === true) {
            this.commonService.create("token", response.token);
            this.autoLogoutService.startLogoutTimer();
            this.broadcastAuthChange();
            this.wrongCode = response.status;
            yield this.globalData();
            if (this.isglobalData) {
              this.loading = false;
              this.toastr.success(response.message, "Login");
              this.router.navigate(["/main/dashboard"]);
              return;
            }
          } else
            return;
        }),
        error: (err) => {
          this.wrongCode = err.error.status;
          this.executeRecaptchaV3();
          this.loading = false;
          return this.toastr.error(err.error.message, "Login");
        }
      });
    } else {
      Object.values(this.validateForm.controls).forEach((control) => {
        if (control.invalid) {
          control.markAsDirty();
          control.updateValueAndValidity({ onlySelf: true });
        }
      });
    }
  }
  globalData() {
    return new Promise((resolve, reject) => {
      this.authService.GetUserGlobalData().subscribe({
        next: (response) => {
          if (response.status === true) {
            this.isglobalData = response.status;
            this.commonService.setItem("access-data", JSON.stringify(response.data));
            resolve();
          } else {
            reject("Error: Status is not true");
          }
        },
        error: (err) => {
          reject(err);
        }
      });
    });
  }
  getVerificationCode() {
    let hasErrors = false;
    if (this.validateForm?.valid) {
      this.loading = true;
      const payload = __spreadProps(__spreadValues({}, this.validateForm.value), {
        isLogin: true,
        grecaptchaToken: this.grecaptchaToken
      });
      this.authService.GetVerificationCode(payload).subscribe({
        next: (response) => {
          if (response.status === true) {
            const firstTimeLogin = response.firstTimeLogin;
            this.status = response.status;
            this.resendOtp = !response.status;
            this.executeRecaptchaV3();
            if (firstTimeLogin) {
              this.isFirstTime = firstTimeLogin;
              this.passwordForm.reset();
            } else {
              this.isSecondTime = true;
            }
            this.isTokens = true;
            this.startTimer(1);
            this.loading = false;
            this.toastr.success(response.message, "Verification Code");
          }
        },
        error: (err) => {
          if (err.error.message == "Invalid email address.") {
            this.wrongMailId = err.error.status;
          } else {
            this.wrongMailId = true;
          }
          if (err.error.message == "Incorrect password.") {
            this.status = err.error.status;
          } else {
            this.status = true;
          }
          this.executeRecaptchaV3();
          this.loading = false;
          this.resendOtp = true;
          return this.toastr.error(err.error.message, "Login");
        }
      });
    } else {
      Object.values(this.validateForm.controls).forEach((control) => {
        if (control.invalid) {
          control.markAsDirty();
          control.updateValueAndValidity({ onlySelf: true });
          hasErrors = true;
        }
      });
      if (hasErrors) {
        this.toastr.warning("Please verify all required fields", "Test Checklist Management");
      }
    }
  }
  changePassword() {
    const payload = {
      emailId: this.validateForm.value.emailId,
      oldPassword: this.validateForm.value.password,
      newPassword: this.passwordForm.value.newPassword,
      grecaptchaToken: this.grecaptchaToken
    };
    this.authService.ChangePassword(payload).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.isFirstTime = false;
          this.isSecondTime = false;
          this.validateForm.reset();
          this.executeRecaptchaV3();
          this.toastr.success(response.message, "Change Password");
        }
      },
      error: (err) => {
        this.executeRecaptchaV3();
        return this.toastr.error(err.error.message, "Login");
      }
    });
  }
  startTimer(minutes) {
    this.displayTimer = true;
    this.resendOtp = true;
    let seconds = minutes * 60;
    const prefix = minutes < 10 ? "0" : "";
    const timer = setInterval(() => {
      seconds--;
      const remainingMinutes = Math.floor(seconds / 60);
      const remainingSeconds = seconds % 60;
      const formattedSeconds = remainingSeconds < 10 ? "0" + remainingSeconds : remainingSeconds;
      this.display = `${prefix}${remainingMinutes}:${formattedSeconds}`;
      if (seconds === 0) {
        clearInterval(timer);
        this.resendOtp = false;
        this.displayTimer = false;
      }
    }, 1e3);
  }
  resendCode() {
    clearTimeout(1);
    this.getVerificationCode();
  }
  forgetPassword() {
    const emailIdControl = this.validateForm.get("emailId");
    if (emailIdControl.invalid) {
      if (emailIdControl.errors?.required) {
        emailIdControl.markAsDirty();
        emailIdControl.updateValueAndValidity({ onlySelf: true });
      } else if (emailIdControl.errors?.email) {
        emailIdControl.markAsDirty();
        emailIdControl.updateValueAndValidity({ onlySelf: true });
      }
      return;
    }
    const payload = {
      emailId: this.validateForm.value.emailId,
      grecaptchaToken: this.grecaptchaToken
    };
    this.authService.ForgetPasswrod(payload).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Forget Password");
        }
      },
      error: (err) => {
        this.executeRecaptchaV3();
        return this.toastr.error(err.error.message, "Forget Password");
      }
    });
  }
  goToRiskCalculator(type) {
    this.router.navigate(["/calculators/risk_assessment_calculator"]);
  }
  goToCvss4Calculator(type) {
    this.router.navigate(["/calculators/cvss4_calculator"]);
  }
};
_LoginComponent.\u0275fac = function LoginComponent_Factory(t) {
  return new (t || _LoginComponent)(i02.\u0275\u0275directiveInject(i12.Router), i02.\u0275\u0275directiveInject(i12.ActivatedRoute), i02.\u0275\u0275directiveInject(i2.FormBuilder), i02.\u0275\u0275directiveInject(AuthService), i02.\u0275\u0275directiveInject(CommonService), i02.\u0275\u0275directiveInject(AutoLogoutService), i02.\u0275\u0275directiveInject(i6.ToastrService), i02.\u0275\u0275directiveInject(i7.ReCaptchaV3Service));
};
_LoginComponent.\u0275cmp = /* @__PURE__ */ i02.\u0275\u0275defineComponent({ type: _LoginComponent, selectors: [["app-login"]], decls: 17, vars: 5, consts: [[1, "row", "w-100", "mx-0", "auth-page"], [1, "col-md-8", "col-xl-6", "mx-auto"], [1, "card"], [1, "row"], [1, "col-md-4", "pe-md-0"], [1, "auth-side-wrapper", 3, "ngStyle"], [1, "col-md-8", "ps-md-0"], [1, "auth-form-wrapper", "px-4", "py-5"], ["routerLink", ".", 1, "nobleui-logo", "logo-light", "d-block", "mb-2"], [1, "text-muted", "fw-normal", "mb-4"], [4, "ngIf"], [1, "login-form", 3, "formGroup"], [1, "mb-3"], [1, "form-label", 3, "for"], [1, "text-danger"], ["formControlName", "emailId", "id", "emailId", "placeholder", "Enter Email-ID", "type", "email", 1, "form-control"], ["class", "text-danger", 4, "ngIf"], ["formControlName", "password", "id", "password", "placeholder", "Enter password", "type", "password", "minlength", "12", 1, "form-control"], [1, "form-check", "mb-3"], ["type", "checkbox", "id", "authCheck", 1, "form-check-input"], ["for", "authCheck", 1, "form-check-label"], ["type", "submit", 1, "btn", "btn-primary", "btn-sm", "me-2", "mb-2", "mb-md-0", 3, "click", "disabled"], ["class", "spinner-grow spinner-grow-sm", "role", "status", "aria-hidden", "true", 4, "ngIf"], [1, "d-block", "mt-3", "text-muted", 3, "click"], [1, "d-flex"], [1, "d-block", "mt-3", 3, "click"], ["role", "status", "aria-hidden", "true", 1, "spinner-grow", "spinner-grow-sm"], ["for", "newPassword", 1, "form-label"], [1, "input-group"], ["id", "newPassword", "name", "newPassword", "placeholder", "New password", "type", "password", "minlength", "12", "formControlName", "newPassword", 1, "form-control"], ["for", "confirmPassword", 1, "form-label"], ["type", "password", "id", "confirmPassword", "name", "confirmPassword", "placeholder", "Confirm password", "formControlName", "confirm", 1, "form-control"], ["type", "text", "placeholder", "Enter your verification code", 1, "form-control", 3, "ngModelChange", "keydown.enter", "ngModel"], [1, "textCenter"], [1, "d-inline-block", 3, "ngClass"], ["type", "button", 1, "btn", "btn-outline-primary", "btn-sm", "mb-1", "mb-md-0", 3, "click", "disabled"]], template: function LoginComponent_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 0)(1, "div", 1)(2, "div", 2)(3, "div", 3)(4, "div", 4);
    i02.\u0275\u0275element(5, "div", 5);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(6, "div", 6)(7, "div", 7)(8, "a", 8);
    i02.\u0275\u0275text(9, "Brute");
    i02.\u0275\u0275elementStart(10, "span");
    i02.\u0275\u0275text(11, "GOAT");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(12, "h5", 9);
    i02.\u0275\u0275text(13, "Welcome back! Log in to your account.");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(14, LoginComponent_div_14_Template, 36, 7, "div", 10)(15, LoginComponent_div_15_Template, 21, 4, "div", 10)(16, LoginComponent_div_16_Template, 26, 11, "div", 10);
    i02.\u0275\u0275elementEnd()()()()()();
  }
  if (rf & 2) {
    i02.\u0275\u0275advance(5);
    i02.\u0275\u0275property("ngStyle", i02.\u0275\u0275pureFunction0(4, _c0));
    i02.\u0275\u0275advance(9);
    i02.\u0275\u0275property("ngIf", !ctx.isSecondTime && !ctx.isFirstTime);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx.isFirstTime);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx.isSecondTime);
  }
}, dependencies: [i8.NgClass, i8.NgIf, i8.NgStyle, i2.\u0275NgNoValidate, i2.DefaultValueAccessor, i2.NgControlStatus, i2.NgControlStatusGroup, i2.MinLengthValidator, i2.NgModel, i2.FormGroupDirective, i2.FormControlName, i12.RouterLink], styles: ["\n\n[_nghost-%COMP%] {\n  height: 100vh;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n.auth-side-wrapper[_ngcontent-%COMP%] {\n  width: 100%;\n  height: 100%;\n  background-size: cover;\n}\n.text-muted[_ngcontent-%COMP%], .dropzone.dz-clickable[_ngcontent-%COMP%]   .dz-message[_ngcontent-%COMP%]   *[_ngcontent-%COMP%] {\n  --bs-text-opacity: 1;\n  color: #7987a1 !important;\n}\n.fw-normal[_ngcontent-%COMP%] {\n  font-weight: 400 !important;\n}\n.mb-4[_ngcontent-%COMP%] {\n  margin-bottom: 1.5rem !important;\n}\n.h[_ngcontent-%COMP%] {\n  height: 45vh;\n}\n.block-cursor[_ngcontent-%COMP%] {\n  cursor: not-allowed !important;\n}\n.no-pointer[_ngcontent-%COMP%] {\n  pointer-events: none;\n}\n.d-inline-block[_ngcontent-%COMP%] {\n  display: inline-block !important;\n}\n/*# sourceMappingURL=login.component.css.map */"] });
var LoginComponent = _LoginComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i02.\u0275setClassDebugInfo(LoginComponent, { className: "LoginComponent", filePath: "src/app/auth/login/login.component.ts", lineNumber: 16 });
})();

// src/app/auth/register/register.component.ts
import { Component as Component2 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i03 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i13 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i22 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
import * as i32 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
var _c02 = () => ({ "background-image": "url(https://via.placeholder.com/219x452)" });
var _RegisterComponent = class _RegisterComponent {
  constructor(router) {
    this.router = router;
  }
  ngOnInit() {
  }
  onRegister(e) {
    e.preventDefault();
    localStorage.setItem("isLoggedin", "true");
    if (localStorage.getItem("isLoggedin")) {
      this.router.navigate(["/"]);
    }
  }
};
_RegisterComponent.\u0275fac = function RegisterComponent_Factory(t) {
  return new (t || _RegisterComponent)(i03.\u0275\u0275directiveInject(i13.Router));
};
_RegisterComponent.\u0275cmp = /* @__PURE__ */ i03.\u0275\u0275defineComponent({ type: _RegisterComponent, selectors: [["app-register"]], decls: 39, vars: 2, consts: [[1, "row", "w-100", "mx-0", "auth-page"], [1, "col-md-8", "col-xl-6", "mx-auto"], [1, "card"], [1, "row"], [1, "col-md-4", "pe-md-0"], [1, "auth-side-wrapper", 3, "ngStyle"], [1, "col-md-8", "ps-md-0"], [1, "auth-form-wrapper", "px-4", "py-5"], ["routerLink", ".", 1, "nobleui-logo", "logo-light", "d-block", "mb-2"], [1, "text-muted", "fw-normal", "mb-4"], [1, "forms-sample"], [1, "mb-3"], ["for", "exampleInputUsername1", 1, "form-label"], ["type", "text", "id", "exampleInputUsername1", "autocomplete", "Username", "placeholder", "Username", 1, "form-control"], ["for", "exampleInputEmail1", 1, "form-label"], ["type", "email", "id", "exampleInputEmail1", "placeholder", "Email", 1, "form-control"], ["for", "exampleInputPassword1", 1, "form-label"], ["type", "password", "id", "exampleInputPassword1", "autocomplete", "current-password", "placeholder", "Password", 1, "form-control"], [1, "form-check", "mb-3"], ["type", "checkbox", "id", "authCheck", 1, "form-check-input"], ["for", "authCheck", 1, "form-check-label"], ["type", "submit", 1, "btn", "btn-primary", "btn-sm", "m-1", 3, "click"], ["type", "button", 1, "btn", "btn-outline-primary", "btn-sm", "m-1"], [1, "feather", "icon-twitter", "btn-icon-prepend"], ["routerLink", "/auth/login", 1, "d-block", "mt-3", "text-muted"]], template: function RegisterComponent_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 0)(1, "div", 1)(2, "div", 2)(3, "div", 3)(4, "div", 4);
    i03.\u0275\u0275element(5, "div", 5);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(6, "div", 6)(7, "div", 7)(8, "a", 8);
    i03.\u0275\u0275text(9, "Noble");
    i03.\u0275\u0275elementStart(10, "span");
    i03.\u0275\u0275text(11, "UI");
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275elementStart(12, "h5", 9);
    i03.\u0275\u0275text(13, "Create a free account.");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(14, "form", 10)(15, "div", 11)(16, "label", 12);
    i03.\u0275\u0275text(17, "Username");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275element(18, "input", 13);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(19, "div", 11)(20, "label", 14);
    i03.\u0275\u0275text(21, "Email address");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275element(22, "input", 15);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(23, "div", 11)(24, "label", 16);
    i03.\u0275\u0275text(25, "Password");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275element(26, "input", 17);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(27, "div", 18);
    i03.\u0275\u0275element(28, "input", 19);
    i03.\u0275\u0275elementStart(29, "label", 20);
    i03.\u0275\u0275text(30, " Remember me ");
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275elementStart(31, "div")(32, "button", 21);
    i03.\u0275\u0275listener("click", function RegisterComponent_Template_button_click_32_listener($event) {
      return ctx.onRegister($event);
    });
    i03.\u0275\u0275text(33, "Sign up");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(34, "button", 22);
    i03.\u0275\u0275element(35, "i", 23);
    i03.\u0275\u0275text(36, " Sign up with twitter ");
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275elementStart(37, "a", 24);
    i03.\u0275\u0275text(38, "Already a user? Sign in");
    i03.\u0275\u0275elementEnd()()()()()()()();
  }
  if (rf & 2) {
    i03.\u0275\u0275advance(5);
    i03.\u0275\u0275property("ngStyle", i03.\u0275\u0275pureFunction0(1, _c02));
  }
}, dependencies: [i22.NgStyle, i32.\u0275NgNoValidate, i32.NgControlStatusGroup, i32.NgForm, i13.RouterLink], styles: ["\n\n[_nghost-%COMP%] {\n  height: 100vh;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n/*# sourceMappingURL=register.component.css.map */"] });
var RegisterComponent = _RegisterComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i03.\u0275setClassDebugInfo(RegisterComponent, { className: "RegisterComponent", filePath: "src/app/auth/register/register.component.ts", lineNumber: 9 });
})();

// src/app/auth/auth.module.ts
import { RouterModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";

// src/app/auth/auth.component.ts
import { Component as Component3 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i04 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i14 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
var _AuthComponent = class _AuthComponent {
  constructor() {
  }
  ngOnInit() {
  }
};
_AuthComponent.\u0275fac = function AuthComponent_Factory(t) {
  return new (t || _AuthComponent)();
};
_AuthComponent.\u0275cmp = /* @__PURE__ */ i04.\u0275\u0275defineComponent({ type: _AuthComponent, selectors: [["app-auth"]], decls: 1, vars: 0, template: function AuthComponent_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275element(0, "router-outlet");
  }
}, dependencies: [i14.RouterOutlet], encapsulation: 2 });
var AuthComponent = _AuthComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i04.\u0275setClassDebugInfo(AuthComponent, { className: "AuthComponent", filePath: "src/app/auth/auth.component.ts", lineNumber: 8 });
})();

// src/app/auth/auth.module.ts
import * as i05 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
var routes = [
  {
    path: "",
    component: AuthComponent,
    children: [
      {
        path: "",
        redirectTo: "login",
        pathMatch: "full"
      },
      {
        path: "login",
        component: LoginComponent
      },
      {
        path: "register",
        component: RegisterComponent
      }
    ]
  }
];
var _AuthModule = class _AuthModule {
};
_AuthModule.\u0275fac = function AuthModule_Factory(t) {
  return new (t || _AuthModule)();
};
_AuthModule.\u0275mod = /* @__PURE__ */ i05.\u0275\u0275defineNgModule({ type: _AuthModule });
_AuthModule.\u0275inj = /* @__PURE__ */ i05.\u0275\u0275defineInjector({ imports: [
  CommonModule,
  SharedModule,
  RouterModule.forChild(routes)
] });
var AuthModule = _AuthModule;
export {
  AuthModule
};
