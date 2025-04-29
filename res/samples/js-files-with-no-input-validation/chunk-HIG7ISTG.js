import {
  ReportTemplateService
} from "/chunk-O7PHE4WN.js";
import {
  FindingService
} from "/chunk-DHXJS5ZC.js";
import {
  TestService
} from "/chunk-YT2CUWVY.js";
import {
  UserService
} from "/chunk-5YCVMAC5.js";
import {
  LoadingService
} from "/chunk-DDGOKMT7.js";
import {
  AuthGuard
} from "/chunk-WGCVQTUY.js";
import {
  CommonService
} from "/chunk-RTM3KQT4.js";
import {
  FeatherIconDirective,
  SharedModule,
  __async,
  __spreadProps,
  __spreadValues
} from "/chunk-2CBLJUUC.js";

// src/app/modules/test/test.module.ts
import { NgModule as NgModule2 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { CommonModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";

// src/app/modules/test/test-routing.module.ts
import { NgModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { RouterModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";

// src/app/modules/test/test-management/test-management.component.ts
import { Component, ViewChild } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { moveItemInArray, transferArrayItem } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_cdk_drag-drop.js?v=ca23e844";
import * as i0 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i1 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i2 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";
import * as i5 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@ng-bootstrap_ng-bootstrap.js?v=ca23e844";
import * as i7 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
import * as i9 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i10 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_button.js?v=ca23e844";
import * as i11 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_core_transition-patch.js?v=ca23e844";
import * as i12 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_core_wave.js?v=ca23e844";
import * as i13 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_icon.js?v=ca23e844";
import * as i14 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_grid.js?v=ca23e844";
import * as i15 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_dropdown.js?v=ca23e844";
import * as i16 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_checkbox.js?v=ca23e844";
import * as i17 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_input.js?v=ca23e844";
import * as i18 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_popover.js?v=ca23e844";
import * as i19 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_table.js?v=ca23e844";
import * as i20 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_tooltip.js?v=ca23e844";
import * as i21 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_popconfirm.js?v=ca23e844";
import * as i23 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_cdk_drag-drop.js?v=ca23e844";
var _c0 = ["chartCanvas"];
var _c1 = ["isCloneModal"];
var _c2 = (a0, a1, a2) => ({ "bg-warning": a0, "bg-success": a1, "bg-danger": a2 });
var _c3 = (a0) => [a0];
function TestManagementComponent_button_7_Template(rf, ctx) {
  if (rf & 1) {
    const _r2 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "button", 73);
    i0.\u0275\u0275listener("click", function TestManagementComponent_button_7_Template_button_click_0_listener() {
      i0.\u0275\u0275restoreView(_r2);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.addRow());
    });
    i0.\u0275\u0275element(1, "i", 74);
    i0.\u0275\u0275text(2, " Add Test ");
    i0.\u0275\u0275elementEnd();
  }
}
function TestManagementComponent_a_26_Template(rf, ctx) {
  if (rf & 1) {
    const _r4 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "a", 75);
    i0.\u0275\u0275listener("nzOnConfirm", function TestManagementComponent_a_26_Template_a_nzOnConfirm_0_listener() {
      i0.\u0275\u0275restoreView(_r4);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.deleteRow());
    });
    i0.\u0275\u0275elementStart(1, "button", 76);
    i0.\u0275\u0275element(2, "span", 77);
    i0.\u0275\u0275elementEnd()();
  }
}
function TestManagementComponent_th_34_Template(rf, ctx) {
  if (rf & 1) {
    const _r6 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "th", 78);
    i0.\u0275\u0275listener("nzCheckedChange", function TestManagementComponent_th_34_Template_th_nzCheckedChange_0_listener($event) {
      i0.\u0275\u0275restoreView(_r6);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.onAllChecked($event));
    });
    i0.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275property("nzChecked", ctx_r2.listOfTestData.length ? ctx_r2.checked : false)("nzIndeterminate", ctx_r2.indeterminate);
  }
}
function TestManagementComponent_tr_66_td_1_Template(rf, ctx) {
  if (rf & 1) {
    const _r9 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "td", 96);
    i0.\u0275\u0275listener("nzCheckedChange", function TestManagementComponent_tr_66_td_1_Template_td_nzCheckedChange_0_listener($event) {
      i0.\u0275\u0275restoreView(_r9);
      const data_r8 = i0.\u0275\u0275nextContext().$implicit;
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.onItemChecked(data_r8._id, $event));
    });
    i0.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const data_r8 = i0.\u0275\u0275nextContext().$implicit;
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275property("nzChecked", ctx_r2.setOfCheckedId.has(data_r8._id))("nzLabel", data_r8._id);
  }
}
function TestManagementComponent_tr_66_span_8_Template(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275elementStart(0, "span");
    i0.\u0275\u0275text(1);
    i0.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const data_r8 = i0.\u0275\u0275nextContext().$implicit;
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1("(", data_r8.timeFrame, ")");
  }
}
function TestManagementComponent_tr_66_Template(rf, ctx) {
  if (rf & 1) {
    const _r7 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "tr", 79);
    i0.\u0275\u0275listener("click", function TestManagementComponent_tr_66_Template_tr_click_0_listener() {
      const data_r8 = i0.\u0275\u0275restoreView(_r7).$implicit;
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView((ctx_r2.canManageTest || ctx_r2.isAdmin) && ctx_r2.editRow(data_r8._id));
    });
    i0.\u0275\u0275template(1, TestManagementComponent_tr_66_td_1_Template, 1, 2, "td", 80);
    i0.\u0275\u0275elementStart(2, "td", 81);
    i0.\u0275\u0275text(3);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(4, "td", 82);
    i0.\u0275\u0275text(5);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(6, "td", 83);
    i0.\u0275\u0275text(7);
    i0.\u0275\u0275template(8, TestManagementComponent_tr_66_span_8_Template, 2, 1, "span", 84);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(9, "td", 85)(10, "span", 86);
    i0.\u0275\u0275text(11);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(12, "td", 87);
    i0.\u0275\u0275text(13);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(14, "td", 88)(15, "div", 89)(16, "span", 90);
    i0.\u0275\u0275listener("click", function TestManagementComponent_tr_66_Template_span_click_16_listener() {
      const data_r8 = i0.\u0275\u0275restoreView(_r7).$implicit;
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.goToMasterData(data_r8._id));
    });
    i0.\u0275\u0275text(17);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275text(18, " \xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(19, "span", 91);
    i0.\u0275\u0275twoWayListener("nzPopoverVisibleChange", function TestManagementComponent_tr_66_Template_span_nzPopoverVisibleChange_19_listener($event) {
      const data_r8 = i0.\u0275\u0275restoreView(_r7).$implicit;
      const ctx_r2 = i0.\u0275\u0275nextContext();
      i0.\u0275\u0275twoWayBindingSet(ctx_r2.popoverVisibility[data_r8._id], $event) || (ctx_r2.popoverVisibility[data_r8._id] = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("click", function TestManagementComponent_tr_66_Template_span_click_19_listener($event) {
      const data_r8 = i0.\u0275\u0275restoreView(_r7).$implicit;
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.onReportButtonClick($event, data_r8));
    });
    i0.\u0275\u0275element(20, "i", 92);
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275elementStart(21, "td", 93);
    i0.\u0275\u0275text(22);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(23, "td", 94);
    i0.\u0275\u0275text(24);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(25, "td", 95);
    i0.\u0275\u0275text(26);
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const data_r8 = ctx.$implicit;
    const ctx_r2 = i0.\u0275\u0275nextContext();
    const contentTemplate_r10 = i0.\u0275\u0275reference(181);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("ngIf", ctx_r2.canManageTest || ctx_r2.isAdmin);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipTitle", data_r8.testTitle + " (" + data_r8.projectName + ")")("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate2(" ", data_r8.testTitle, "(", data_r8.projectName, ") ");
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipTitle", data_r8.testName)("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", data_r8.testName, " ");
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipTitle", data_r8.closureDate && data_r8.timeFrame ? data_r8.closureDate + " - " + data_r8.timeFrame : null)("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1("", data_r8.closureDate, " ");
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("ngIf", data_r8.dateDifference !== null);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipTitle", data_r8 == null ? null : data_r8.testStatus)("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("ngClass", i0.\u0275\u0275pureFunction3(29, _c2, (data_r8 == null ? null : data_r8.testStatus == null ? null : data_r8.testStatus.toLowerCase()) === "in progress", (data_r8 == null ? null : data_r8.testStatus == null ? null : data_r8.testStatus.toLowerCase()) === "completed", (data_r8 == null ? null : data_r8.testStatus == null ? null : data_r8.testStatus.toLowerCase()) === "not started"));
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", data_r8.testStatus, " ");
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275textInterpolate(data_r8.testScope);
    i0.\u0275\u0275advance(4);
    i0.\u0275\u0275textInterpolate1(" ", data_r8.totalFindings, " ");
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzPopoverVisible", ctx_r2.popoverVisibility[data_r8._id]);
    i0.\u0275\u0275property("nzPopoverContent", contentTemplate_r10);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzTooltipTitle", data_r8.updatedOn)("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", data_r8.updatedOn, " ");
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipTitle", data_r8.updatedBy)("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", data_r8.updatedBy, " ");
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipTitle", data_r8.createdBy)("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", data_r8.createdBy, " ");
  }
}
function TestManagementComponent_div_67_ng_template_6_Template(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275text(0, "Prev");
  }
}
function TestManagementComponent_div_67_ng_template_7_Template(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275text(0, "Next");
  }
}
function TestManagementComponent_div_67_Template(rf, ctx) {
  if (rf & 1) {
    const _r11 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 20)(1, "div", 97)(2, "div", 98);
    i0.\u0275\u0275text(3);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(4, "div", 99)(5, "ngb-pagination", 100);
    i0.\u0275\u0275twoWayListener("pageChange", function TestManagementComponent_div_67_Template_ngb_pagination_pageChange_5_listener($event) {
      i0.\u0275\u0275restoreView(_r11);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      i0.\u0275\u0275twoWayBindingSet(ctx_r2.pageIndex, $event) || (ctx_r2.pageIndex = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275template(6, TestManagementComponent_div_67_ng_template_6_Template, 1, 0, "ng-template", 101)(7, TestManagementComponent_div_67_ng_template_7_Template, 1, 0, "ng-template", 102);
    i0.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275advance(3);
    i0.\u0275\u0275textInterpolate1(" ", ctx_r2.currentPageRange, " ");
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("collectionSize", ctx_r2.totalRecords);
    i0.\u0275\u0275twoWayProperty("page", ctx_r2.pageIndex);
    i0.\u0275\u0275property("maxSize", 5)("rotate", true)("ellipses", false)("boundaryLinks", false);
  }
}
function TestManagementComponent_div_68_Template(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275elementStart(0, "div", 103)(1, "div", 104);
    i0.\u0275\u0275element(2, "ngb-progressbar", 105);
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("value", ctx_r2.progress)("striped", true)("showValue", true)("animated", true);
  }
}
function TestManagementComponent_ng_template_178_div_10_Template(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275elementStart(0, "div", 119);
    i0.\u0275\u0275text(1);
    i0.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const item_r14 = ctx.$implicit;
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", item_r14.name, " ");
  }
}
function TestManagementComponent_ng_template_178_div_13_Template(rf, ctx) {
  if (rf & 1) {
    const _r15 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 120);
    i0.\u0275\u0275text(1);
    i0.\u0275\u0275elementStart(2, "span", 121);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_178_div_13_Template_span_click_2_listener() {
      const ctx_r15 = i0.\u0275\u0275restoreView(_r15);
      const item_r17 = ctx_r15.$implicit;
      const i_r18 = ctx_r15.index;
      const ctx_r2 = i0.\u0275\u0275nextContext(2);
      return i0.\u0275\u0275resetView(ctx_r2.deleteCustom(item_r17, i_r18));
    });
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const item_r17 = ctx.$implicit;
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", item_r17.name, " ");
  }
}
function TestManagementComponent_ng_template_178_div_14_Template(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275elementStart(0, "div", 119);
    i0.\u0275\u0275text(1);
    i0.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const item_r19 = ctx.$implicit;
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", item_r19.name, " ");
  }
}
function TestManagementComponent_ng_template_178_div_21_Template(rf, ctx) {
  if (rf & 1) {
    const _r20 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 120);
    i0.\u0275\u0275text(1);
    i0.\u0275\u0275elementStart(2, "span", 122);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_178_div_21_Template_span_click_2_listener() {
      const ctx_r20 = i0.\u0275\u0275restoreView(_r20);
      const item_r22 = ctx_r20.$implicit;
      const i_r23 = ctx_r20.index;
      const ctx_r2 = i0.\u0275\u0275nextContext(2);
      return i0.\u0275\u0275resetView(ctx_r2.addCustom(item_r22, i_r23));
    });
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const item_r22 = ctx.$implicit;
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", item_r22.name, " ");
  }
}
function TestManagementComponent_ng_template_178_Template(rf, ctx) {
  if (rf & 1) {
    const _r12 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 106)(1, "h5", 107);
    i0.\u0275\u0275text(2, "Custom Test Column");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(3, "button", 108);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_178_Template_button_click_3_listener() {
      const modal_r13 = i0.\u0275\u0275restoreView(_r12).$implicit;
      return i0.\u0275\u0275resetView(modal_r13.close("by: close icon"));
    });
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(4, "div", 109)(5, "div", 110)(6, "div", 111)(7, "div", 112)(8, "p");
    i0.\u0275\u0275text(9, "Displayed (drag and drop to sort)");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275template(10, TestManagementComponent_ng_template_178_div_10_Template, 2, 1, "div", 113);
    i0.\u0275\u0275elementStart(11, "div", 114, 12);
    i0.\u0275\u0275listener("cdkDropListDropped", function TestManagementComponent_ng_template_178_Template_div_cdkDropListDropped_11_listener($event) {
      i0.\u0275\u0275restoreView(_r12);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.drop($event));
    });
    i0.\u0275\u0275template(13, TestManagementComponent_ng_template_178_div_13_Template, 3, 1, "div", 115);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275template(14, TestManagementComponent_ng_template_178_div_14_Template, 2, 1, "div", 113);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(15, "div", 111)(16, "div", 112)(17, "p");
    i0.\u0275\u0275text(18, "Not Shown");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(19, "div", 114, 13);
    i0.\u0275\u0275listener("cdkDropListDropped", function TestManagementComponent_ng_template_178_Template_div_cdkDropListDropped_19_listener($event) {
      i0.\u0275\u0275restoreView(_r12);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.drop($event));
    });
    i0.\u0275\u0275template(21, TestManagementComponent_ng_template_178_div_21_Template, 3, 1, "div", 115);
    i0.\u0275\u0275elementEnd()()()()();
    i0.\u0275\u0275elementStart(22, "div", 116)(23, "button", 117);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_178_Template_button_click_23_listener() {
      i0.\u0275\u0275restoreView(_r12);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.closeModal());
    });
    i0.\u0275\u0275text(24, " Close ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(25, "button", 118);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_178_Template_button_click_25_listener() {
      i0.\u0275\u0275restoreView(_r12);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.handleOk());
    });
    i0.\u0275\u0275text(26, " Save changes ");
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const todoList_r24 = i0.\u0275\u0275reference(12);
    const doneList_r25 = i0.\u0275\u0275reference(20);
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275advance(5);
    i0.\u0275\u0275property("nzGutter", 24);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzSpan", 12);
    i0.\u0275\u0275advance(4);
    i0.\u0275\u0275property("ngForOf", ctx_r2.title);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("cdkDropListData", ctx_r2.fix)("cdkDropListConnectedTo", i0.\u0275\u0275pureFunction1(11, _c3, doneList_r25));
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("ngForOf", ctx_r2.fix);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("ngForOf", ctx_r2.footer);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzSpan", 12);
    i0.\u0275\u0275advance(4);
    i0.\u0275\u0275property("cdkDropListData", ctx_r2.notFix)("cdkDropListConnectedTo", i0.\u0275\u0275pureFunction1(13, _c3, todoList_r24));
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("ngForOf", ctx_r2.notFix);
  }
}
function TestManagementComponent_ng_template_180_Template(rf, ctx) {
  if (rf & 1) {
    const _r26 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 123)(1, "div", 124);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_180_Template_div_click_1_listener() {
      i0.\u0275\u0275restoreView(_r26);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      const openDocx_r27 = i0.\u0275\u0275reference(187);
      return i0.\u0275\u0275resetView(ctx_r2.openDocsModal(openDocx_r27));
    });
    i0.\u0275\u0275element(2, "i", 125);
    i0.\u0275\u0275elementStart(3, "span", 126);
    i0.\u0275\u0275text(4, "Word");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(5, "div", 124);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_180_Template_div_click_5_listener() {
      i0.\u0275\u0275restoreView(_r26);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      const selectPPTColumn_r28 = i0.\u0275\u0275reference(183);
      return i0.\u0275\u0275resetView(ctx_r2.openPPTModal(selectPPTColumn_r28));
    });
    i0.\u0275\u0275element(6, "i", 127);
    i0.\u0275\u0275elementStart(7, "span", 126);
    i0.\u0275\u0275text(8, "PPT");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(9, "div", 124);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_180_Template_div_click_9_listener() {
      i0.\u0275\u0275restoreView(_r26);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      const selectCsvColumn_r29 = i0.\u0275\u0275reference(185);
      return i0.\u0275\u0275resetView(ctx_r2.openBasicModal(selectCsvColumn_r29, "XML"));
    });
    i0.\u0275\u0275element(10, "i", 128);
    i0.\u0275\u0275elementStart(11, "span", 126);
    i0.\u0275\u0275text(12, "XML");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(13, "div", 124);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_180_Template_div_click_13_listener() {
      i0.\u0275\u0275restoreView(_r26);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      const selectCsvColumn_r29 = i0.\u0275\u0275reference(185);
      return i0.\u0275\u0275resetView(ctx_r2.openBasicModal(selectCsvColumn_r29, "CSV"));
    });
    i0.\u0275\u0275element(14, "i", 129);
    i0.\u0275\u0275elementStart(15, "span", 126);
    i0.\u0275\u0275text(16, "CSV");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(17, "div", 124);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_180_Template_div_click_17_listener() {
      i0.\u0275\u0275restoreView(_r26);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.downloadJSON());
    });
    i0.\u0275\u0275element(18, "i", 130);
    i0.\u0275\u0275elementStart(19, "span", 126);
    i0.\u0275\u0275text(20, "JSON");
    i0.\u0275\u0275elementEnd()()();
  }
}
function TestManagementComponent_ng_template_182_div_5_Template(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275elementStart(0, "div", 142);
    i0.\u0275\u0275element(1, "div", 143);
    i0.\u0275\u0275elementStart(2, "p");
    i0.\u0275\u0275text(3, "Loading...");
    i0.\u0275\u0275elementEnd()();
  }
}
function TestManagementComponent_ng_template_182_div_16_Template(rf, ctx) {
  if (rf & 1) {
    const _r32 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 144)(1, "div", 135);
    i0.\u0275\u0275element(2, "i", 145);
    i0.\u0275\u0275elementStart(3, "input", 146);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_ng_template_182_div_16_Template_input_ngModelChange_3_listener($event) {
      const item_r33 = i0.\u0275\u0275restoreView(_r32).$implicit;
      i0.\u0275\u0275twoWayBindingSet(item_r33.checked, $event) || (item_r33.checked = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("change", function TestManagementComponent_ng_template_182_div_16_Template_input_change_3_listener() {
      i0.\u0275\u0275restoreView(_r32);
      const ctx_r2 = i0.\u0275\u0275nextContext(2);
      return i0.\u0275\u0275resetView(ctx_r2.updateSingleCheckedPPT());
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(4, "label", 147);
    i0.\u0275\u0275text(5);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(6, "div", 138)(7, "label", 147);
    i0.\u0275\u0275text(8);
    i0.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const item_r33 = ctx.$implicit;
    i0.\u0275\u0275advance(3);
    i0.\u0275\u0275property("id", item_r33.value);
    i0.\u0275\u0275twoWayProperty("ngModel", item_r33.checked);
    i0.\u0275\u0275property("value", item_r33.value);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("for", item_r33.value);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", item_r33.findingSeqId, "");
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("for", item_r33.value);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate(item_r33.findingTitle);
  }
}
function TestManagementComponent_ng_template_182_Template(rf, ctx) {
  if (rf & 1) {
    const _r30 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 106)(1, "h5", 107);
    i0.\u0275\u0275text(2, "Generate Report");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(3, "button", 108);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_182_Template_button_click_3_listener() {
      const modal_r31 = i0.\u0275\u0275restoreView(_r30).$implicit;
      return i0.\u0275\u0275resetView(modal_r31.close("by: close icon"));
    });
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(4, "div", 131);
    i0.\u0275\u0275template(5, TestManagementComponent_ng_template_182_div_5_Template, 4, 0, "div", 132);
    i0.\u0275\u0275elementStart(6, "div", 133);
    i0.\u0275\u0275listener("cdkDropListDropped", function TestManagementComponent_ng_template_182_Template_div_cdkDropListDropped_6_listener($event) {
      i0.\u0275\u0275restoreView(_r30);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.dropForPPT($event));
    });
    i0.\u0275\u0275elementStart(7, "div", 134)(8, "div", 135);
    i0.\u0275\u0275element(9, "i", 136);
    i0.\u0275\u0275text(10, "\xA0\xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(11, "label", 137);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_ng_template_182_Template_label_ngModelChange_11_listener($event) {
      i0.\u0275\u0275restoreView(_r30);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      i0.\u0275\u0275twoWayBindingSet(ctx_r2.allCheckedPPT, $event) || (ctx_r2.allCheckedPPT = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("ngModelChange", function TestManagementComponent_ng_template_182_Template_label_ngModelChange_11_listener() {
      i0.\u0275\u0275restoreView(_r30);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.updateAllCheckedPPT());
    });
    i0.\u0275\u0275text(12, " Finding IDs ");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(13, "div", 138)(14, "label", 139);
    i0.\u0275\u0275text(15, "Finding Title");
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275template(16, TestManagementComponent_ng_template_182_div_16_Template, 9, 7, "div", 140);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(17, "div", 116)(18, "button", 141);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_182_Template_button_click_18_listener() {
      const modal_r31 = i0.\u0275\u0275restoreView(_r30).$implicit;
      return i0.\u0275\u0275resetView(modal_r31.close("by: close button"));
    });
    i0.\u0275\u0275text(19, " Cancel ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(20, "button", 118);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_182_Template_button_click_20_listener() {
      i0.\u0275\u0275restoreView(_r30);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.downloadPPT());
    });
    i0.\u0275\u0275text(21, " Generate ");
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275advance(5);
    i0.\u0275\u0275property("ngIf", ctx_r2.isLoading);
    i0.\u0275\u0275advance(6);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx_r2.allCheckedPPT);
    i0.\u0275\u0275property("nzIndeterminate", ctx_r2.csvCheckBoxPPT);
    i0.\u0275\u0275advance(5);
    i0.\u0275\u0275property("ngForOf", ctx_r2.observationList);
  }
}
function TestManagementComponent_ng_template_184_div_12_Template(rf, ctx) {
  if (rf & 1) {
    const _r36 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 152)(1, "div", 148);
    i0.\u0275\u0275element(2, "i", 145);
    i0.\u0275\u0275elementStart(3, "input", 146);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_ng_template_184_div_12_Template_input_ngModelChange_3_listener($event) {
      const item_r37 = i0.\u0275\u0275restoreView(_r36).$implicit;
      i0.\u0275\u0275twoWayBindingSet(item_r37.checked, $event) || (item_r37.checked = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("change", function TestManagementComponent_ng_template_184_div_12_Template_input_change_3_listener() {
      i0.\u0275\u0275restoreView(_r36);
      const ctx_r2 = i0.\u0275\u0275nextContext(2);
      return i0.\u0275\u0275resetView(ctx_r2.updateSingleChecked());
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(4, "label", 147);
    i0.\u0275\u0275text(5);
    i0.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const item_r37 = ctx.$implicit;
    i0.\u0275\u0275advance(3);
    i0.\u0275\u0275property("id", item_r37.id);
    i0.\u0275\u0275twoWayProperty("ngModel", item_r37.checked);
    i0.\u0275\u0275property("value", item_r37.value);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("for", item_r37.id);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate(item_r37.label);
  }
}
function TestManagementComponent_ng_template_184_Template(rf, ctx) {
  if (rf & 1) {
    const _r34 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 106)(1, "h5", 107);
    i0.\u0275\u0275text(2, "Generate Report");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(3, "button", 108);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_184_Template_button_click_3_listener() {
      const modal_r35 = i0.\u0275\u0275restoreView(_r34).$implicit;
      return i0.\u0275\u0275resetView(modal_r35.close("by: close icon"));
    });
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(4, "div", 109)(5, "div", 133);
    i0.\u0275\u0275listener("cdkDropListDropped", function TestManagementComponent_ng_template_184_Template_div_cdkDropListDropped_5_listener($event) {
      i0.\u0275\u0275restoreView(_r34);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.dropForCSV($event));
    });
    i0.\u0275\u0275elementStart(6, "div", 134)(7, "div", 148);
    i0.\u0275\u0275element(8, "i", 136);
    i0.\u0275\u0275text(9, "\xA0\xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(10, "label", 149);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_ng_template_184_Template_label_ngModelChange_10_listener($event) {
      i0.\u0275\u0275restoreView(_r34);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      i0.\u0275\u0275twoWayBindingSet(ctx_r2.allChecked, $event) || (ctx_r2.allChecked = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("ngModelChange", function TestManagementComponent_ng_template_184_Template_label_ngModelChange_10_listener() {
      i0.\u0275\u0275restoreView(_r34);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.updateAllChecked());
    });
    i0.\u0275\u0275text(11, " Select All ");
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275template(12, TestManagementComponent_ng_template_184_div_12_Template, 6, 5, "div", 150);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(13, "div", 116)(14, "button", 141);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_184_Template_button_click_14_listener() {
      const modal_r35 = i0.\u0275\u0275restoreView(_r34).$implicit;
      return i0.\u0275\u0275resetView(modal_r35.close("by: close button"));
    });
    i0.\u0275\u0275text(15, " Cancel ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(16, "button", 151);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_184_Template_button_click_16_listener() {
      i0.\u0275\u0275restoreView(_r34);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.downloadReport());
    });
    i0.\u0275\u0275text(17, " Generate ");
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275advance(10);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx_r2.allChecked);
    i0.\u0275\u0275property("nzIndeterminate", ctx_r2.csvCheckBox);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("ngForOf", ctx_r2.items);
    i0.\u0275\u0275advance(4);
    i0.\u0275\u0275property("disabled", !ctx_r2.isAnyChecked());
  }
}
function TestManagementComponent_ng_template_186_tr_15_Template(rf, ctx) {
  if (rf & 1) {
    const _r40 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "tr")(1, "td", 158);
    i0.\u0275\u0275text(2);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(3, "td", 158);
    i0.\u0275\u0275text(4);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(5, "td", 159)(6, "button", 160);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_186_tr_15_Template_button_click_6_listener() {
      i0.\u0275\u0275restoreView(_r40);
      const ctx_r2 = i0.\u0275\u0275nextContext(2);
      return i0.\u0275\u0275resetView(ctx_r2.downloadDocxReport());
    });
    i0.\u0275\u0275element(7, "span", 161);
    i0.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const item_r41 = ctx.$implicit;
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275textInterpolate(item_r41.reportTemplateName);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275textInterpolate(item_r41.isDefaultTemplate ? "Default" : item_r41.reportType);
  }
}
function TestManagementComponent_ng_template_186_Template(rf, ctx) {
  if (rf & 1) {
    const _r38 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 106)(1, "h5", 107);
    i0.\u0275\u0275text(2, "Docx report template");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(3, "button", 108);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_186_Template_button_click_3_listener() {
      const modal_r39 = i0.\u0275\u0275restoreView(_r38).$implicit;
      return i0.\u0275\u0275resetView(modal_r39.close("by: close icon"));
    });
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(4, "div", 109)(5, "nz-table", 153)(6, "thead")(7, "tr")(8, "th", 154);
    i0.\u0275\u0275text(9, " Template name ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(10, "th", 155);
    i0.\u0275\u0275text(11, " report type ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(12, "th", 156);
    i0.\u0275\u0275text(13, "Action");
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275elementStart(14, "tbody");
    i0.\u0275\u0275template(15, TestManagementComponent_ng_template_186_tr_15_Template, 8, 2, "tr", 157);
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275elementStart(16, "div", 116)(17, "button", 141);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_186_Template_button_click_17_listener() {
      const modal_r39 = i0.\u0275\u0275restoreView(_r38).$implicit;
      return i0.\u0275\u0275resetView(modal_r39.close("by: close button"));
    });
    i0.\u0275\u0275text(18, " Cancel ");
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275advance(5);
    i0.\u0275\u0275property("nzShowPagination", false)("nzData", ctx_r2.listOfTemplates)("nzLoading", ctx_r2.loading);
    i0.\u0275\u0275advance(10);
    i0.\u0275\u0275property("ngForOf", ctx_r2.listOfTemplates);
  }
}
function TestManagementComponent_ng_template_188_Template(rf, ctx) {
  if (rf & 1) {
    const _r42 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 106)(1, "h5", 107);
    i0.\u0275\u0275text(2, " Select Template ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(3, "button", 108);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_188_Template_button_click_3_listener() {
      const modal_r43 = i0.\u0275\u0275restoreView(_r42).$implicit;
      return i0.\u0275\u0275resetView(modal_r43.close("by: close icon"));
    });
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(4, "div", 116)(5, "button", 73);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_188_Template_button_click_5_listener() {
      const modal_r43 = i0.\u0275\u0275restoreView(_r42).$implicit;
      return i0.\u0275\u0275resetView(modal_r43.close(true));
    });
    i0.\u0275\u0275text(6, " Template with POC ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(7, "button", 73);
    i0.\u0275\u0275listener("click", function TestManagementComponent_ng_template_188_Template_button_click_7_listener() {
      const modal_r43 = i0.\u0275\u0275restoreView(_r42).$implicit;
      return i0.\u0275\u0275resetView(modal_r43.close(false));
    });
    i0.\u0275\u0275text(8, " Template without POC ");
    i0.\u0275\u0275elementEnd()();
  }
}
var _TestManagementComponent = class _TestManagementComponent {
  constructor(router, toastr, testService, findingService, cdr, modalService, userService, location, reportService) {
    this.router = router;
    this.toastr = toastr;
    this.testService = testService;
    this.findingService = findingService;
    this.cdr = cdr;
    this.modalService = modalService;
    this.userService = userService;
    this.location = location;
    this.reportService = reportService;
    this.color = "black";
    this.totalRecords = 0;
    this.totalPages = 1;
    this.loading = false;
    this.pageSize = 10;
    this.pageIndex = 1;
    this.currentPageRange = "";
    this.listOfTestData = [];
    this.getTestType = [];
    this.getTestStatus = [];
    this.getTestScope = [];
    this.isTestTitleValue = "";
    this.isTestTitleVisible = false;
    this.isClosureDateValue = "";
    this.isclosureDateVisible = false;
    this.isTotalFindingValue = "";
    this.isTotalFindingVisible = false;
    this.isLastUpdatedValue = "";
    this.isLastUpdatedVisible = false;
    this.isFirstCreatedValue = "";
    this.isFirstCreatedVisible = false;
    this.checked = false;
    this.indeterminate = false;
    this.customColumn = [
      {
        name: "",
        value: "_id",
        default: true,
        required: true,
        position: "left",
        width: 50,
        fixWidth: true
      },
      {
        name: "Test Title",
        value: "testTitle",
        default: true,
        required: true,
        position: "left",
        width: 180,
        fixWidth: true
      },
      {
        name: "Test Name",
        value: "testName",
        default: true,
        required: true,
        position: "left",
        width: 130,
        fixWidth: true
      },
      {
        name: "Closure date",
        value: "closureDate",
        default: true,
        width: 140,
        fixWidth: true
      },
      {
        name: "Test scope",
        value: "testScope",
        default: true,
        width: 100,
        fixWidth: true
      },
      {
        name: "Last activity test",
        value: "updatedOn",
        default: false,
        width: 100,
        fixWidth: true
      },
      {
        name: "Last updated by",
        value: "updatedBy",
        default: true,
        width: 130,
        fixWidth: true
      },
      {
        name: "First created by",
        value: "createdBy",
        default: false,
        width: 150,
        fixWidth: true
      },
      {
        name: "Test status",
        value: "testStatus",
        default: true,
        required: true,
        position: "right",
        width: 130,
        fixWidth: true
      },
      {
        name: "Total findings",
        value: "totalFindings",
        default: true,
        required: true,
        position: "right",
        width: 150,
        fixWidth: true
      }
    ];
    this.title = [];
    this.footer = [];
    this.fix = [];
    this.notFix = [];
    this.isVisible = false;
    this.state = this.location.getState();
    this.startDate = "";
    this.endDate = "";
    this.isupdatedOnValue = "";
    this.isupdatedOnVisible = false;
    this.canManageTest = false;
    this.isAdmin = false;
    this.isFindingVisible = false;
    this.isLoading = false;
    this.progress = 0;
    this.popoverVisibility = {};
    this.openCsvSelectColumn = "";
    this.items = [
      { id: "findingIdCheck", value: "findingSeqId", label: "Finding Id", checked: false },
      { id: "findingTitleCheck", value: "findingTitle", label: "Finding Title", checked: false },
      { id: "testCheck", value: "testTitle", label: "Test Title", checked: false },
      { id: "cveCweCheck", value: "vulnerabilityCodes", label: "CVE/CWE", checked: false },
      //
      { id: "vulnerabilityCategoryCheck", value: "vulnerabilityCategoryIds", label: "Vulnerability Category", checked: false },
      //
      { id: "observationCheck", value: "observation", label: "Observation", checked: false },
      { id: "identificationValidationCheck", value: "identificationValidationMethod", label: "Identification Method", checked: false },
      { id: "resourcesAffectedCheck", value: "resourceAffected", label: "Resources Affected", checked: false },
      { id: "parameterAffectedCheck", value: "parameterAffected", label: "Parameter Affected", checked: false },
      { id: "throughoutProjectCheck", value: "throughoutApplication", label: "Throughout Project", checked: false },
      { id: "fixedOrOpenedCheck", value: "fixedOrOpenFinding", label: "Fixed or Opened", checked: false },
      { id: "technicalImpactCheck", value: "threatImpact", label: "Technical Impact", checked: false },
      { id: "businessImpactCheck", value: "businessImpact", label: "Business Impact", checked: false },
      { id: "stepsCheck", value: "evidence", label: "Steps", checked: false },
      { id: "appendixCheck", value: "appendix", label: "Appendix", checked: false },
      { id: "cvssV4VectorCheck", value: "cvssVector", label: "CVSS V4 vector", checked: false },
      { id: "cvssScoreCheck", value: "cvssScore", label: "CVSS Score", checked: false },
      { id: "severityCheck", value: "cvssSeverity", label: "Severity", checked: false },
      { id: "riskVectorCheck", value: "riskVector", label: "Risk Vector", checked: false },
      { id: "riskCheck", value: "riskSeverity", label: "Risk Severity", checked: false },
      { id: "riskScoreCheck", value: "riskImpactScore", label: "Risk Score", checked: false },
      { id: "recommendationCheck", value: "recommendation", label: "Recommendation", checked: false },
      { id: "referencesCheck", value: "references", label: "References", checked: false }
      //
    ];
    this.listOfTemplates = [];
    this.convertTestTypeData = (data) => {
      return data.map((item) => {
        return {
          text: item.testName,
          value: item.testName
        };
      });
    };
    this.convertTestStatusData = (data) => {
      return data.map((item) => {
        return {
          text: item.testStatus,
          value: item.testStatus
        };
      });
    };
    this.convertTestScopeData = (data) => {
      return data.map((item) => {
        return {
          text: item.testScope,
          value: item.testScope
        };
      });
    };
    this.convertData = (data) => {
      const convertedData = [];
      data.forEach((item) => {
        if (Array.isArray(item.value)) {
          item.value.forEach((value) => {
            convertedData.push({
              type: "search",
              key: item.key,
              value
            });
          });
        } else {
          convertedData.push({
            type: "search",
            key: item.key,
            value: item.value
          });
        }
      });
      return convertedData;
    };
    this.listOfCurrentPageData = [];
    this.setOfCheckedId = /* @__PURE__ */ new Set();
    this.observationList = [];
    this.allCheckedPPT = false;
    this.csvCheckBoxPPT = false;
    this.allChecked = false;
    this.csvCheckBox = false;
    const today = /* @__PURE__ */ new Date();
    this.startDate = this.formatDate(today);
    this.endDate = this.formatDate(today);
  }
  ngOnInit() {
    this.projectId = this.state?.projectId;
    this.accessData();
    this.getTestTypeScopeStatusData();
    this.title = this.customColumn.filter((item) => item.position === "left" && item.required);
    this.footer = this.customColumn.filter((item) => item.position === "right" && item.required);
    this.fix = this.customColumn.filter((item) => item.default && !item.required);
    this.notFix = this.customColumn.filter((item) => !item.default && !item.required);
  }
  accessData() {
    const getUserAccessData = this.userService.getUserAccessData();
    this.canManageTest = getUserAccessData[0]?.canManageTest;
  }
  loadDataFromServer(id, pageIndex, pageSize, sortField, sortOrder, search) {
    this.loading = true;
    this.testService.GetTestList(this.projectId, pageIndex, pageSize, search, sortOrder).subscribe({
      next: (response) => {
        if (response.status === true) {
          if (!response.data.length) {
            this.listOfTestData = [];
            this.loading = false;
            return;
          }
          const data = response.data;
          this.listOfTestData = data;
          data.forEach((item) => {
            const { dateDifference } = item;
            if (dateDifference > 0) {
              const months = Math.floor(dateDifference / 30);
              const days = dateDifference % 30;
              item.timeFrame = months ? `${months}m${months > 1 ? "s" : ""}${days ? ` ${days}d` : ""}` : `${dateDifference}d`;
            } else {
              item.timeFrame = `${dateDifference}d`;
            }
          });
          this.totalRecords = response.totalRecords;
          this.isAdmin = response.isAdmin;
          this.onCurrentPageDataChange(this.listOfTestData);
          this.calculatePageRange();
          this.loading = false;
        }
      },
      error: (err) => {
        this.loading = false;
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  onQueryParamsChange(params) {
    const { pageSize, pageIndex, sort, filter } = params;
    const currentSort = sort.find((item) => item.value !== null);
    const sortField = currentSort && currentSort.key || null;
    const sortOrder = currentSort && currentSort.value || null;
    const filterData = this.convertData(filter);
    const sortingData = { type: "sort", key: sortField, value: sortOrder };
    this.loadDataFromServer(this.projectId, pageIndex, pageSize, sortField, sortingData, filterData);
  }
  getTestTypeScopeStatusData() {
    this.testService.GetTestTypeScopeStatus().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.getTestType = this.convertTestTypeData(response.data[0]?.testName);
          this.getTestStatus = this.convertTestStatusData(response.data[0]?.testStatus);
          this.getTestScope = this.convertTestScopeData(response.data[0]?.testScope);
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  deleteRow() {
    const deletIdsArray = [...this.setOfCheckedId];
    this.testService.GetTestDelete({ testIds: deletIdsArray }).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, []);
          this.setOfCheckedId = new Set([...this.setOfCheckedId].filter((id) => !deletIdsArray.includes(id)));
          this.toastr.success(response.message, "Test Management");
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  reset() {
    this.isTestTitleValue = "";
    this.startDate = "";
    this.endDate = "";
    this.isTotalFindingValue = "";
    this.isLastUpdatedValue = "";
    this.isFirstCreatedValue = "";
    this.isTestTitleVisible = false;
    this.isclosureDateVisible = false;
    this.isTotalFindingVisible = false;
    this.isupdatedOnVisible = false;
    this.isLastUpdatedVisible = false;
    this.isFirstCreatedVisible = false;
    this.isFindingVisible = false;
    this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, []);
  }
  search(columName, onKeyString) {
    if (columName === "testTitle") {
      this.isTestTitleVisible = false;
      const searchData = {
        type: "search",
        key: columName,
        value: this.isTestTitleValue
      };
      this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "closureDate") {
      this.isclosureDateVisible = false;
      this.isClosureDateValue = this.startDate;
      const searchData = {
        type: "search",
        key: columName,
        value: `${this.startDate}to${this.endDate}`
      };
      this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "totalFindings") {
      this.isTotalFindingVisible = false;
      const searchData = {
        type: "search",
        key: columName,
        value: this.isTotalFindingValue
      };
      this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "updatedOn") {
      this.isupdatedOnVisible = false;
      this.isupdatedOnValue = this.startDate;
      const searchData = {
        type: "search",
        key: columName,
        value: `${this.startDate}to${this.endDate}`
      };
      this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "updatedBy") {
      this.isLastUpdatedVisible = false;
      const searchData = {
        type: "search",
        key: columName,
        value: this.isLastUpdatedValue
      };
      this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "createdBy") {
      this.isFirstCreatedVisible = false;
      const searchData = {
        type: "search",
        key: columName,
        value: this.isFirstCreatedValue
      };
      this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
    } else {
      this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, []);
    }
  }
  onEnter(columName) {
    this.search(columName);
  }
  resetPageIndex() {
    this.pageIndex = 1;
  }
  onKeydown(columName) {
    if (this.debounceTimeout) {
      clearTimeout(this.debounceTimeout);
    }
    this.debounceTimeout = setTimeout(() => {
      if (columName === "testTitle") {
        const searchData = {
          type: "search",
          key: columName,
          value: this.isTestTitleValue
        };
        this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
      } else if (columName === "totalFindings") {
        const searchData = {
          type: "search",
          key: columName,
          value: this.isTotalFindingValue
        };
        this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
      } else if (columName === "updatedBy") {
        const searchData = {
          type: "search",
          key: columName,
          value: this.isLastUpdatedValue
        };
        this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
      } else if (columName === "createdBy") {
        const searchData = {
          type: "search",
          key: columName,
          value: this.isFirstCreatedValue
        };
        this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, searchData);
      } else {
        this.loadDataFromServer(this.projectId, this.pageIndex, this.pageSize, null, null, []);
      }
    }, 2e3);
  }
  formatDate(date) {
    const day = this.addLeadingZero(date.getDate());
    const month = this.addLeadingZero(date.getMonth() + 1);
    const year = date.getFullYear();
    return `${year}-${month}-${day}`;
  }
  addLeadingZero(value) {
    return value < 10 ? `0${value}` : `${value}`;
  }
  selectDateRange(range, columName) {
    const today = /* @__PURE__ */ new Date();
    switch (range) {
      case "Today":
        this.startDate = this.formatDate(today);
        this.endDate = this.formatDate(today);
        break;
      case "Yesterday":
        const yesterday = new Date(today);
        yesterday.setDate(today.getDate() - 1);
        this.startDate = this.formatDate(yesterday);
        this.endDate = this.formatDate(yesterday);
        break;
      case "Last 7 Days":
        const last7Days = new Date(today);
        last7Days.setDate(today.getDate() - 6);
        this.startDate = this.formatDate(last7Days);
        this.endDate = this.formatDate(today);
        break;
      case "Last 30 Days":
        const last30Days = new Date(today);
        last30Days.setDate(today.getDate() - 29);
        this.startDate = this.formatDate(last30Days);
        this.endDate = this.formatDate(today);
        break;
      case "This Month":
        const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
        this.startDate = this.formatDate(firstDayOfMonth);
        this.endDate = this.formatDate(today);
        break;
      case "Last Month":
        const firstDayOfLastMonth = new Date(today.getFullYear(), today.getMonth() - 1, 1);
        const lastDayOfLastMonth = new Date(today.getFullYear(), today.getMonth(), 0);
        this.startDate = this.formatDate(firstDayOfLastMonth);
        this.endDate = this.formatDate(today);
        break;
      case "Last Year":
        const firstDayOfLastYear = new Date(today.getFullYear() - 1, 0, 1);
        const lastDayOfLastYear = new Date(today.getFullYear() - 1, 11, 31);
        this.startDate = this.formatDate(firstDayOfLastYear);
        this.endDate = this.formatDate(today);
        break;
      default:
        break;
    }
    this.search(columName);
  }
  updateHoveredDate(range) {
    const today = /* @__PURE__ */ new Date();
    switch (range) {
      case "Today":
        this.startDate = this.formatDate(today);
        this.endDate = this.formatDate(today);
        break;
      case "Yesterday":
        const yesterday = new Date(today);
        yesterday.setDate(today.getDate() - 1);
        this.startDate = this.formatDate(yesterday);
        this.endDate = this.formatDate(yesterday);
        break;
      case "Last 7 Days":
        const last7Days = new Date(today);
        last7Days.setDate(today.getDate() - 6);
        this.startDate = this.formatDate(last7Days);
        this.endDate = this.formatDate(today);
        break;
      case "Last 30 Days":
        const last30Days = new Date(today);
        last30Days.setDate(today.getDate() - 29);
        this.startDate = this.formatDate(last30Days);
        this.endDate = this.formatDate(today);
        break;
      case "This Month":
        const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
        this.startDate = this.formatDate(firstDayOfMonth);
        this.endDate = this.formatDate(today);
        break;
      case "Last Month":
        const firstDayOfLastMonth = new Date(today.getFullYear(), today.getMonth() - 1, 1);
        const lastDayOfLastMonth = new Date(today.getFullYear(), today.getMonth(), 0);
        this.startDate = this.formatDate(firstDayOfLastMonth);
        this.endDate = this.formatDate(today);
        break;
      case "Last Year":
        const firstDayOfLastYear = new Date(today.getFullYear() - 1, 0, 1);
        const lastDayOfLastYear = new Date(today.getFullYear() - 1, 11, 31);
        this.startDate = this.formatDate(firstDayOfLastYear);
        this.endDate = this.formatDate(today);
        break;
      default:
        break;
    }
  }
  addRow() {
    this.router.navigate(["/main/tests_management/test_update"], {
      state: { projectId: this.projectId }
    });
  }
  editRow(id) {
    if (this.canManageTest || this.isAdmin) {
      this.router.navigate(["/main/tests_management/test_update"], {
        state: { testId: id }
      });
    }
  }
  goToMasterData(id) {
    this.router.navigate(["/main/tests_management/master_test_data"], {
      state: { testId: id }
    });
  }
  updateCheckedSet(id, checked) {
    if (checked) {
      this.setOfCheckedId.add(id);
    } else {
      this.setOfCheckedId.delete(id);
    }
  }
  onCurrentPageDataChange(listOfCurrentPageData) {
    this.listOfCurrentPageData = listOfCurrentPageData;
    this.refreshCheckedStatus();
  }
  refreshCheckedStatus() {
    const listOfEnabledData = this.listOfCurrentPageData.filter(({ disabled }) => !disabled);
    this.checked = listOfEnabledData.every(({ _id }) => this.setOfCheckedId.has(_id));
    this.indeterminate = listOfEnabledData.some(({ _id }) => this.setOfCheckedId.has(_id)) && !this.checked;
  }
  onItemChecked(id, checked) {
    this.updateCheckedSet(id, checked);
    this.refreshCheckedStatus();
  }
  onAllChecked(checked) {
    this.listOfCurrentPageData.filter(({ disabled }) => !disabled).forEach(({ _id }) => this.updateCheckedSet(_id, checked));
    this.refreshCheckedStatus();
  }
  // Modal custom table
  drop(event) {
    if (event.previousContainer === event.container) {
      moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
    } else {
      transferArrayItem(event.previousContainer.data, event.container.data, event.previousIndex, event.currentIndex);
    }
    this.fix = this.fix.map((item) => {
      item.default = true;
      return item;
    });
    this.notFix = this.notFix.map((item) => {
      item.default = false;
      return item;
    });
    this.cdr.markForCheck();
  }
  deleteCustom(value, index) {
    value.default = false;
    this.notFix = [...this.notFix, value];
    this.fix.splice(index, 1);
    this.cdr.markForCheck();
  }
  addCustom(value, index) {
    value.default = true;
    this.fix = [...this.fix, value];
    this.notFix.splice(index, 1);
    this.cdr.markForCheck();
  }
  handleOk() {
    this.customColumn = [
      ...this.title,
      ...this.fix,
      ...this.notFix,
      ...this.footer
    ];
    this.isVisible = false;
    this.cdr.markForCheck();
    this.closeModal();
  }
  openVerticalCenteredModal(content) {
    this.modalService.open(content, { centered: true }).result.then((result) => {
    }).catch((res) => {
    });
  }
  closeModal() {
    this.modalService.dismissAll();
  }
  calculatePageRange() {
    const startItem = (this.pageIndex - 1) * this.pageSize + 1;
    const endItem = Math.min(this.pageIndex * this.pageSize, this.totalRecords);
    this.totalPages = Math.ceil(this.totalRecords / this.pageSize);
    this.currentPageRange = `Showing ${startItem} to ${endItem} of ${this.totalRecords} entries`;
  }
  // Report Generate
  downloadReport() {
    if (this.forWhichReport == "CSV") {
      this.downloadCsv();
    } else if (this.forWhichReport == "XML") {
      this.downloadXml();
    }
  }
  updateProgress(progress) {
    this.progress = progress;
  }
  downloadDocxReport() {
    if (!this.selectedRowData.canGenerateReport) {
      this.toastr.info("There are no findings or all findings are In Progress.Sorry! Report can not be generated. Please ensure that atleast one finding is not In Progress.", "Report Download");
      return;
    }
    if (this.selectedRowData.canGenerateReport && this.selectedRowData.testScope === "Reval") {
      const modalRef = this.modalService.open(this.isCloneModal, { ariaLabelledBy: "modal-basic-title" });
      modalRef.result.then((result) => {
        this.docsReportDownload(result);
      }).catch((error) => {
        console.log("Modal dismissed with error:", error);
      });
    } else {
      this.docsReportDownload();
    }
  }
  docsReportDownload(condition) {
    this.isLoading = true;
    this.popoverVisibility[this.selectedRowData._id] = false;
    const payload = {
      testId: this.selectedRowData._id,
      poc: condition
    };
    this.testService.GenerateDocReport(payload).subscribe({
      next: (response) => {
        this.reportService.DownloadProgressBar((progress) => this.updateProgress(progress), 100).then(() => {
          const url = window.URL.createObjectURL(response);
          const link = document.createElement("a");
          link.href = url;
          link.download = `${this.reportService.convertDate()}.docx`;
          link.click();
          window.URL.revokeObjectURL(url);
          this.updateProgress(0);
          this.isLoading = false;
          this.toastr.info("DOCX File is generated successfully.", "Test Management");
        });
      },
      error: (err) => {
        this.isLoading = false;
        this.updateProgress(0);
        this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  downloadCsv() {
    this.popoverVisibility[this.selectedRowData._id] = false;
    const checkedItems = this.items.filter((item) => item.checked);
    if (checkedItems.length) {
      this.progress = 0;
      this.isLoading = true;
      const progressCallback = (progress) => {
        this.progress = progress;
      };
      this.modalService.dismissAll();
      this.testService.GenerateCSVReport(this.selectedRowData._id, checkedItems).subscribe({
        next: (response) => __async(this, null, function* () {
          if (response.status === true) {
            this.reportDataForWord = response.data[0];
            try {
              yield this.reportService.generateAndDownloadCsv(response.data[0], checkedItems, progressCallback);
              this.isLoading = false;
              this.toastr.success("File is generated successfully.", "Test Management");
            } catch (error) {
              console.error("Error generating or downloading XML:", error);
              this.isLoading = false;
            } finally {
              this.isLoading = false;
            }
          }
        }),
        error: (err) => {
          this.isLoading = false;
          return this.toastr.error(err.error.message, "Test Management");
        }
      });
    } else {
      this.toastr.error("Please select at least one option.", "Test Report");
    }
  }
  downloadXml() {
    this.popoverVisibility[this.selectedRowData._id] = false;
    this.progress = 0;
    this.isLoading = true;
    const checkedItems = this.items.filter((item) => item.checked);
    if (checkedItems.length) {
      const progressCallback = (progress) => {
        this.progress = progress;
      };
      this.modalService.dismissAll();
      this.testService.GenerateXMLReport(this.selectedRowData._id, checkedItems).subscribe({
        next: (response) => __async(this, null, function* () {
          if (response.status === true) {
            this.reportDataForWord = response.data[0];
            try {
              yield this.reportService.generateXml(response.data[0], progressCallback);
              this.isLoading = false;
              this.toastr.info("XML File is generated successfully.", "Test Management");
            } catch (error) {
              console.error("Error generating or downloading XML:", error);
              this.loading = false;
            } finally {
              this.isLoading = false;
            }
          }
        }),
        error: (err) => {
          this.isLoading = false;
          return this.toastr.error(err.error.message, "Test Management");
        }
      });
    }
  }
  onReportButtonClick(event, data) {
    this.selectedRowData = data;
    event.stopPropagation();
    this.togglePopoverVisibility(data._id);
  }
  togglePopoverVisibility(id) {
    for (let key in this.popoverVisibility) {
      if (this.popoverVisibility.hasOwnProperty(key)) {
        this.popoverVisibility[key] = false;
      }
    }
    this.popoverVisibility[id] = !this.popoverVisibility[id];
  }
  openPPTModal(content) {
    this.csvCheckBox = false;
    this.allChecked = false;
    this.getObservationData();
    this.modalService.open(content, { scrollable: true }).result.then((result) => {
      this.openCsvSelectColumn = "Modal closed" + result;
    }).catch((res) => {
    });
    return this.items.filter((item) => item.checked = false);
  }
  getObservationData() {
    this.isLoading = true;
    this.findingService.getFindingList(this.selectedRowData._id, 0, 500, null, null).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.observationList = response.data;
          this.isLoading = false;
        }
      },
      error: (err) => {
        this.isLoading = false;
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  downloadPPT() {
    const findingIds = this.observationList.filter((item) => item.checked).map((item) => item._id);
    if (findingIds.length === 0) {
      this.toastr.error("Please select at least one option.", "Test Management");
      return;
    }
    const payload = {
      testId: this.observationList[0]?.testId,
      findingIds
    };
    this.isLoading = true;
    this.modalService.dismissAll();
    this.updateProgress(0);
    this.testService.GeneratePPTReport(payload).subscribe({
      next: (response) => __async(this, null, function* () {
        if (response) {
          yield this.reportService.DownloadProgressBar((progress) => this.updateProgress(progress), 100);
          const url = window.URL.createObjectURL(response);
          const link = document.createElement("a");
          link.href = url;
          link.download = `${this.reportService.convertDate()}.pptx`;
          link.click();
          window.URL.revokeObjectURL(url);
          this.updateProgress(0);
          this.isLoading = false;
          this.allCheckedPPT = false;
          this.csvCheckBoxPPT = false;
          this.toastr.info("PPT File is generated successfully.", "Test Management");
        }
      }),
      error: (err) => {
        this.isLoading = false;
        this.updateProgress(0);
        this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  openBasicModal(content, forWhichReport) {
    this.csvCheckBox = false;
    this.allChecked = false;
    this.modalService.open(content, { scrollable: true, size: "sm" }).result.then((result) => {
      this.openCsvSelectColumn = "Modal closed" + result;
    }).catch((res) => {
    });
    this.forWhichReport = forWhichReport;
    return this.items.filter((item) => item.checked = false);
  }
  openDocsModal(content) {
    this.csvCheckBox = false;
    this.allChecked = false;
    this.docxReportTemplateList(this.selectedRowData._id);
    this.modalService.open(content, { scrollable: true, size: "sm" }).result.then((result) => {
      this.openCsvSelectColumn = "Modal closed" + result;
    }).catch((res) => {
    });
  }
  docxReportTemplateList(testId) {
    this.testService.DocxList(testId).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.listOfTemplates = response.data;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  downloadJSON() {
    const payload = {
      testId: this.selectedRowData._id
    };
    this.isLoading = true;
    this.modalService.dismissAll();
    this.updateProgress(0);
    this.testService.GenerateJSONReport(payload).subscribe({
      next: (response) => __async(this, null, function* () {
        if (response) {
          yield this.reportService.DownloadProgressBar((progress) => this.updateProgress(progress), 100);
          const jsonString = JSON.stringify(response);
          const blob = new Blob([jsonString], { type: "application/json" });
          const link = document.createElement("a");
          link.href = window.URL.createObjectURL(blob);
          link.download = `${this.reportService.convertDate()}.json`;
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          this.isLoading = false;
        }
      }),
      error: (err) => {
        this.isLoading = false;
        this.updateProgress(0);
        this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  dropForCSV(event) {
    moveItemInArray(this.items, event.previousIndex, event.currentIndex);
  }
  dropForPPT(event) {
    moveItemInArray(this.observationList, event.previousIndex, event.currentIndex);
  }
  updateAllCheckedPPT() {
    this.csvCheckBoxPPT = false;
    if (this.allCheckedPPT) {
      this.observationList = this.observationList.map((item) => __spreadProps(__spreadValues({}, item), {
        checked: true
      }));
    } else {
      this.observationList = this.observationList.map((item) => __spreadProps(__spreadValues({}, item), {
        checked: false
      }));
    }
  }
  updateSingleCheckedPPT() {
    if (this.observationList.every((item) => !item.checked)) {
      this.allCheckedPPT = false;
      this.csvCheckBoxPPT = false;
    } else if (this.observationList.every((item) => item.checked)) {
      this.allCheckedPPT = true;
      this.csvCheckBoxPPT = false;
    } else {
      this.csvCheckBoxPPT = true;
    }
  }
  updateAllChecked() {
    this.csvCheckBox = false;
    if (this.allChecked) {
      this.items = this.items.map((item) => __spreadProps(__spreadValues({}, item), {
        checked: true
      }));
    } else {
      this.items = this.items.map((item) => __spreadProps(__spreadValues({}, item), {
        checked: false
      }));
    }
  }
  isAnyChecked() {
    return this.items.some((item) => item.checked);
  }
  updateSingleChecked() {
    const stepsChecked = this.items.find((item) => item.value === "evidence")?.checked || false;
    const appendixChecked = this.items.find((item) => item.value === "appendix")?.checked || false;
    const findingTitleItem = this.items.find((item) => item.value === "findingTitle");
    if (stepsChecked || appendixChecked) {
      if (findingTitleItem && !findingTitleItem.checked) {
        findingTitleItem.checked = true;
      }
    }
    if (this.items.every((item) => !item.checked)) {
      this.allChecked = false;
      this.csvCheckBox = false;
    } else if (this.items.every((item) => item.checked)) {
      this.allChecked = true;
      this.csvCheckBox = false;
    } else {
      this.csvCheckBox = true;
    }
  }
};
_TestManagementComponent.\u0275fac = function TestManagementComponent_Factory(t) {
  return new (t || _TestManagementComponent)(i0.\u0275\u0275directiveInject(i1.Router), i0.\u0275\u0275directiveInject(i2.ToastrService), i0.\u0275\u0275directiveInject(TestService), i0.\u0275\u0275directiveInject(FindingService), i0.\u0275\u0275directiveInject(i0.ChangeDetectorRef), i0.\u0275\u0275directiveInject(i5.NgbModal), i0.\u0275\u0275directiveInject(UserService), i0.\u0275\u0275directiveInject(i7.Location), i0.\u0275\u0275directiveInject(ReportTemplateService));
};
_TestManagementComponent.\u0275cmp = /* @__PURE__ */ i0.\u0275\u0275defineComponent({ type: _TestManagementComponent, selectors: [["app-test-management"]], viewQuery: function TestManagementComponent_Query(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275viewQuery(_c0, 5);
    i0.\u0275\u0275viewQuery(_c1, 5);
  }
  if (rf & 2) {
    let _t;
    i0.\u0275\u0275queryRefresh(_t = i0.\u0275\u0275loadQuery()) && (ctx.chartCanvas = _t.first);
    i0.\u0275\u0275queryRefresh(_t = i0.\u0275\u0275loadQuery()) && (ctx.isCloneModal = _t.first);
  }
}, decls: 190, vars: 69, consts: [["testTitle", "nzDropdownMenu"], ["closureDate", "nzDropdownMenu"], ["totalFindings", "nzDropdownMenu"], ["updatedOn", "nzDropdownMenu"], ["updatedBy", "nzDropdownMenu"], ["createdBy", "nzDropdownMenu"], ["verticalCenteredModal", ""], ["contentTemplate", ""], ["selectPPTColumn", ""], ["selectCsvColumn", ""], ["openDocx", ""], ["isCloneModal", ""], ["todoList", "cdkDropList"], ["doneList", "cdkDropList"], [1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "mb-3", "mb-md-0"], [1, "d-flex", "align-items-center", "flex-wrap", "text-nowrap"], ["type", "button", "class", "btn btn-primary btn-icon-text mb-2 mb-md-0", 3, "click", 4, "ngIf"], [1, "row"], [1, "col-md-12", "stretch-card"], [1, "card"], [1, "card-body"], [1, "dataTable-top"], [1, "dataTable-dropdown"], [1, "dataTable-selector", 3, "ngModelChange", "change", "ngModel"], ["value", "10", "selected", ""], ["value", "15"], ["value", "20"], ["value", "25"], [1, "dataTable-search"], ["nz-popconfirm", "", "nzPopconfirmTitle", "Sure to delete?", 3, "nzOnConfirm", 4, "ngIf"], ["nz-button", "", "nzType", "primary", "nzSize", "large", 3, "click"], ["nz-icon", "", "nzType", "setting", "nzTheme", "outline"], [1, "table-container", "dataTable"], ["nzShowSizeChanger", "", 3, "nzQueryParams", "nzCurrentPageDataChange", "nzData", "nzShowPagination", "nzLoading", "nzTotal", "nzPageSize", "nzPageIndex", "nzCustomColumn"], ["id", "", "nzCellControl", "_id", "nzLabel", "Select all", 3, "nzChecked", "nzIndeterminate", "nzCheckedChange", 4, "ngIf"], ["id", "", "nzCellControl", "testTitle", "nzColumnKey", "testTitle", "nzCustomFilter", "", 3, "nzSortPriority", "nzSortFn"], [3, "nzVisibleChange", "nzVisible", "nzActive", "nzDropdownMenu"], ["nz-icon", "", "nzType", "search"], ["id", "", "nzCellControl", "testName", "nzColumnKey", "testName", 3, "nzFilters", "nzFilterFn", "nzFilterMultiple", "nzSortFn"], ["id", "", "nzCellControl", "closureDate", "nzColumnKey", "closureDate", "nzCustomFilter", "", 3, "nzSortFn"], ["id", "", "nzCellControl", "testStatus", "nzColumnKey", "testStatus", 3, "nzFilters", "nzFilterFn", "nzFilterMultiple", "nzSortFn"], ["id", "", "nzCellControl", "testScope", "nzColumnKey", "testScope", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzFilters", "nzFilterFn", "nzFilterMultiple", "nzSortFn", "nzTooltipTitle", "nzTooltipColor"], ["id", "", "nzCellControl", "totalFindings", "nzColumnKey", "totalFindings", "nzCustomFilter", "", 3, "nzSortFn"], ["id", "", "nzCellControl", "updatedOn", "nzColumnKey", "updatedOn", "nzCustomFilter", "", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzSortFn", "nzTooltipTitle", "nzTooltipColor"], ["id", "", "nzCellControl", "updatedBy", "nzColumnKey", "updatedBy", "nzCustomFilter", "", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzSortFn", "nzTooltipTitle", "nzTooltipColor"], ["id", "", "nzCellControl", "createdBy", "nzColumnKey", "createdBy", "nzCustomFilter", "", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzSortFn", "nzTooltipTitle", "nzTooltipColor"], [3, "click", 4, "ngFor", "ngForOf"], ["class", "row", 4, "ngIf"], ["class", "loader-overlay", 4, "ngIf"], [1, "ant-table-filter-dropdown"], [1, "search-box"], ["type", "text", "nz-input", "", "placeholder", "Search test title", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "button", 1, "btn", "searchbtn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["type", "button", 1, "btn", "searchbtn", "btn-outline-primary", "btn-icon-text", "me-2", "mb-2", "mb-md-0", 3, "click"], [1, "col-md-12"], ["type", "text", "nz-input", "", "placeholder", "Search Closure date", 1, "clsInput", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], [1, "list-group"], ["type", "button", 1, "list-group-item", "list-group-item-action", "dayBtn", 3, "mouseenter", "click"], [1, "my-2", "d-flex"], [1, "col"], [1, "form-label"], ["mask", "d0/M0/yyyy", "placeholder", "dd/mm/yyyy", "readonly", "", 1, "form-control", "mb-4", "me-2", "mb-md-0", "dateSearch", 3, "ngModelChange", "ngModel"], ["mask", "d0/M0/yyyy", "placeholder", "dd/mm/yyyy", "readonly", "", 1, "form-control", "mb-4", "mb-md-0", "dateSearch", 3, "ngModelChange", "ngModel"], [1, "col", "d-flex", "justify-content-end"], ["type", "button", 1, "btn", "searchbtn", "colsureButton", "btn-outline-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["type", "text", "nz-input", "", "placeholder", "Search total finding", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "text", "nz-input", "", "placeholder", "Search last activity test", 1, "clsInput", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "text", "nz-input", "", "placeholder", "Search last updated by", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "text", "nz-input", "", "placeholder", "Search first crated by", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], [1, "example"], ["type", "button", 1, "btn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["data-feather", "plus", "appFeatherIcon", "", 1, "btn-icon-prepend"], ["nz-popconfirm", "", "nzPopconfirmTitle", "Sure to delete?", 3, "nzOnConfirm"], ["nz-button", "", "nzType", "primary", "nzSize", "large"], ["nz-icon", "", "nzType", "delete", "nzTheme", "outline"], ["id", "", "nzCellControl", "_id", "nzLabel", "Select all", 3, "nzCheckedChange", "nzChecked", "nzIndeterminate"], [3, "click"], ["nzCellControl", "_id", 3, "nzChecked", "nzLabel", "nzCheckedChange", 4, "ngIf"], ["nzCellControl", "testTitle", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzTooltipTitle", "nzTooltipColor"], ["nzCellControl", "testName", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzTooltipTitle", "nzTooltipColor"], ["nzCellControl", "closureDate", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzTooltipTitle", "nzTooltipColor"], [4, "ngIf"], ["nzCellControl", "testStatus", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzTooltipTitle", "nzTooltipColor"], [1, "badge", 3, "ngClass"], ["nzCellControl", "testScope"], ["nzCellControl", "totalFindings", 1, "d-flex", "align-items-center"], [1, "d-flex", "align-items-center"], [1, "textRight", 2, "min-width", "50px", 3, "click"], ["nz-button", "", "nzType", "primary", "nz-popover", "", "nzPopoverTrigger", "click", "nzPopoverPlacement", "right", 3, "nzPopoverVisibleChange", "click", "nzPopoverVisible", "nzPopoverContent"], ["data-feather", "download", "appFeatherIcon", "", 1, "btn-icon-prepend", "hover-icon", "btn_icon"], ["nzCellControl", "updatedOn", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzTooltipTitle", "nzTooltipColor"], ["nzCellControl", "updatedBy", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzTooltipTitle", "nzTooltipColor"], ["nzCellControl", "createdBy", "nzEllipsis", "", "nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzTooltipTitle", "nzTooltipColor"], ["nzCellControl", "_id", 3, "nzCheckedChange", "nzChecked", "nzLabel"], [1, "col-sm-6", "col-md-5"], ["id", "dataTableExample_info", "role", "status", "aria-live", "polite", 1, "dataTables_info"], [1, "col-sm-6", "col-md-7"], [1, "d-flex", "justify-content-end", 3, "pageChange", "collectionSize", "page", "maxSize", "rotate", "ellipses", "boundaryLinks"], ["ngbPaginationPrevious", ""], ["ngbPaginationNext", ""], [1, "loader-overlay"], [1, "loader-container"], ["type", "primary", 3, "value", "striped", "showValue", "animated"], [1, "modal-header"], ["id", "exampleModalLabel", 1, "modal-title"], ["type", "button", "aria-label", "Close", 1, "btn-close", 3, "click"], [1, "modal-body"], ["nz-row", "", 3, "nzGutter"], ["nz-col", "", 1, "gutter-row", 3, "nzSpan"], [1, "example-container"], ["class", "example-box", 4, "ngFor", "ngForOf"], ["cdkDropList", "", 1, "example-list", 3, "cdkDropListDropped", "cdkDropListData", "cdkDropListConnectedTo"], ["class", "example-box", "cdkDrag", "", 4, "ngFor", "ngForOf"], [1, "modal-footer"], ["type", "button", "data-bs-dismiss", "modal", 1, "btn", "btn-secondary", "btn-sm", "m-1", 3, "click"], ["type", "button", 1, "btn", "btn-primary", "btn-sm", "m-1", 3, "click"], [1, "example-box"], ["cdkDrag", "", 1, "example-box"], ["nz-icon", "", "nzType", "minus-circle", "nzTheme", "outline", 3, "click"], ["nz-icon", "", "nzType", "plus-circle", "nzTheme", "outline", 3, "click"], [1, "d-flex", "flex-column", "report-Icon"], ["role", "button", 1, "d-flex", "align-items-center", 3, "click"], [1, "mdi", "mdi-file-word", "mx-1", "fs-4", "word"], [1, "ml-2"], [1, "mdi", "mdi-file-powerpoint", "mx-1", "fs-4", "ppt"], [1, "mdi", "mdi-file-document", "mx-1", "fs-4", "xml"], [1, "mdi", "mdi-file-excel", "mx-1", "fs-4", "csv"], [1, "mdi", "mdi-file", "mx-1", "fs-4", "csv"], [1, "modal-body", "position-relative"], ["class", "spinner-overlay", 4, "ngIf"], ["id", "sortable", "cdkDropList", "", 3, "cdkDropListDropped"], [1, "row", "selectAll-box"], [1, "col-sm-4", "form-check"], [1, "mdi", "mdi-border-end", "icon"], ["nz-checkbox", "", 1, "fs-6", "fw-semibold", 3, "ngModelChange", "ngModel", "nzIndeterminate"], [1, "col-sm-8"], [1, "fs-6", "fw-semibold"], ["class", "row PPTCheckbox-box", "cdkDrag", "", 4, "ngFor", "ngForOf"], ["type", "button", 1, "btn", "btn-secondary", "btn-sm", "m-1", 3, "click"], [1, "spinner-overlay"], [1, "spinner"], ["cdkDrag", "", 1, "row", "PPTCheckbox-box"], [1, "mdi", "mdi-swap-vertical", "icon"], ["name", "FindingIds", "type", "checkbox", 1, "form-check-input", 3, "ngModelChange", "change", "id", "ngModel", "value"], [1, "form-check-label", "ml-2", 3, "for"], [1, "col-sm-12", "form-check"], ["nz-checkbox", "", 3, "ngModelChange", "ngModel", "nzIndeterminate"], ["class", "row CsvCheckbox-box", "cdkDrag", "", 4, "ngFor", "ngForOf"], ["type", "button", 1, "btn", "btn-primary", "btn-sm", "m-1", 3, "click", "disabled"], ["cdkDrag", "", 1, "row", "CsvCheckbox-box"], ["nzShowSizeChanger", "", 3, "nzShowPagination", "nzData", "nzLoading"], ["id", "1", "nzColumnKey", "reportTemplateName"], ["id", "3", "nzColumnKey", "reportType"], ["id", "5", 1, "text-center"], [4, "ngFor", "ngForOf"], [1, "ellipsis"], [1, "text-center", "action"], ["nz-button", "", "nzType", "primary", "nzShape", "circle", 3, "click"], ["nz-icon", "", "nzType", "download", "nzTheme", "outline"]], template: function TestManagementComponent_Template(rf, ctx) {
  if (rf & 1) {
    const _r1 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 14)(1, "div", 15)(2, "div", 16)(3, "div")(4, "h4", 17);
    i0.\u0275\u0275text(5, "Tests Management");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(6, "div", 18);
    i0.\u0275\u0275template(7, TestManagementComponent_button_7_Template, 3, 0, "button", 19);
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(8, "div", 20)(9, "div", 21)(10, "div", 22)(11, "div", 23)(12, "div", 24)(13, "div", 25)(14, "label")(15, "select", 26);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_select_ngModelChange_15_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.pageSize, $event) || (ctx.pageSize = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("change", function TestManagementComponent_Template_select_change_15_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.resetPageIndex());
    });
    i0.\u0275\u0275elementStart(16, "option", 27);
    i0.\u0275\u0275text(17, "10");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(18, "option", 28);
    i0.\u0275\u0275text(19, "15");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(20, "option", 29);
    i0.\u0275\u0275text(21, "20");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(22, "option", 30);
    i0.\u0275\u0275text(23, "25");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275text(24, " entries per page");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(25, "div", 31);
    i0.\u0275\u0275template(26, TestManagementComponent_a_26_Template, 3, 0, "a", 32);
    i0.\u0275\u0275text(27, " \xA0\xA0 ");
    i0.\u0275\u0275elementStart(28, "button", 33);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_28_listener() {
      i0.\u0275\u0275restoreView(_r1);
      const verticalCenteredModal_r5 = i0.\u0275\u0275reference(179);
      return i0.\u0275\u0275resetView(ctx.openVerticalCenteredModal(verticalCenteredModal_r5));
    });
    i0.\u0275\u0275element(29, "span", 34);
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275elementStart(30, "div", 35)(31, "nz-table", 36);
    i0.\u0275\u0275listener("nzQueryParams", function TestManagementComponent_Template_nz_table_nzQueryParams_31_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onQueryParamsChange($event));
    })("nzCurrentPageDataChange", function TestManagementComponent_Template_nz_table_nzCurrentPageDataChange_31_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onCurrentPageDataChange($event));
    });
    i0.\u0275\u0275elementStart(32, "thead")(33, "tr");
    i0.\u0275\u0275template(34, TestManagementComponent_th_34_Template, 1, 2, "th", 37);
    i0.\u0275\u0275elementStart(35, "th", 38);
    i0.\u0275\u0275text(36, " Test Title ");
    i0.\u0275\u0275elementStart(37, "nz-filter-trigger", 39);
    i0.\u0275\u0275twoWayListener("nzVisibleChange", function TestManagementComponent_Template_nz_filter_trigger_nzVisibleChange_37_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isTestTitleVisible, $event) || (ctx.isTestTitleVisible = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275element(38, "span", 40);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(39, "th", 41);
    i0.\u0275\u0275text(40, " Test Name ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(41, "th", 42);
    i0.\u0275\u0275text(42, " Closure date ");
    i0.\u0275\u0275elementStart(43, "nz-filter-trigger", 39);
    i0.\u0275\u0275twoWayListener("nzVisibleChange", function TestManagementComponent_Template_nz_filter_trigger_nzVisibleChange_43_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isclosureDateVisible, $event) || (ctx.isclosureDateVisible = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275element(44, "span", 40);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(45, "th", 43);
    i0.\u0275\u0275text(46, " Test status ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(47, "th", 44);
    i0.\u0275\u0275text(48, " Test scope ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(49, "th", 45);
    i0.\u0275\u0275text(50, " Total findings ");
    i0.\u0275\u0275elementStart(51, "nz-filter-trigger", 39);
    i0.\u0275\u0275twoWayListener("nzVisibleChange", function TestManagementComponent_Template_nz_filter_trigger_nzVisibleChange_51_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isTotalFindingVisible, $event) || (ctx.isTotalFindingVisible = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275element(52, "span", 40);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(53, "th", 46);
    i0.\u0275\u0275text(54, " Last activity test ");
    i0.\u0275\u0275elementStart(55, "nz-filter-trigger", 39);
    i0.\u0275\u0275twoWayListener("nzVisibleChange", function TestManagementComponent_Template_nz_filter_trigger_nzVisibleChange_55_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isupdatedOnVisible, $event) || (ctx.isupdatedOnVisible = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275element(56, "span", 40);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(57, "th", 47);
    i0.\u0275\u0275text(58, " Last updated by ");
    i0.\u0275\u0275elementStart(59, "nz-filter-trigger", 39);
    i0.\u0275\u0275twoWayListener("nzVisibleChange", function TestManagementComponent_Template_nz_filter_trigger_nzVisibleChange_59_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isLastUpdatedVisible, $event) || (ctx.isLastUpdatedVisible = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275element(60, "span", 40);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(61, "th", 48);
    i0.\u0275\u0275text(62, " First created by ");
    i0.\u0275\u0275elementStart(63, "nz-filter-trigger", 39);
    i0.\u0275\u0275twoWayListener("nzVisibleChange", function TestManagementComponent_Template_nz_filter_trigger_nzVisibleChange_63_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isFirstCreatedVisible, $event) || (ctx.isFirstCreatedVisible = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275element(64, "span", 40);
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(65, "tbody");
    i0.\u0275\u0275template(66, TestManagementComponent_tr_66_Template, 27, 33, "tr", 49);
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275template(67, TestManagementComponent_div_67_Template, 8, 7, "div", 50);
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275template(68, TestManagementComponent_div_68_Template, 3, 4, "div", 51);
    i0.\u0275\u0275elementStart(69, "nz-dropdown-menu", null, 0)(71, "div", 52)(72, "div", 53)(73, "input", 54);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_73_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isTestTitleValue, $event) || (ctx.isTestTitleValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("keydown", function TestManagementComponent_Template_input_keydown_73_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onKeydown("testTitle"));
    })("keydown.enter", function TestManagementComponent_Template_input_keydown_enter_73_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onEnter("testTitle"));
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(74, "button", 55);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_74_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.search("testTitle"));
    });
    i0.\u0275\u0275text(75, " Search");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275text(76, "\xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(77, "button", 56);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_77_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.reset());
    });
    i0.\u0275\u0275text(78, " Reset ");
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(79, "nz-dropdown-menu", null, 1)(81, "div", 52)(82, "div", 53)(83, "div", 20)(84, "div", 57)(85, "input", 58);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_85_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.startDate, $event) || (ctx.startDate = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("keydown", function TestManagementComponent_Template_input_keydown_85_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onKeydown("closureDate"));
    })("keydown.enter", function TestManagementComponent_Template_input_keydown_enter_85_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onEnter("closureDate"));
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(86, "div", 59)(87, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_87_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Today"));
    })("click", function TestManagementComponent_Template_button_click_87_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Today", "closureDate"));
    });
    i0.\u0275\u0275text(88, " Today ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(89, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_89_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Yesterday"));
    })("click", function TestManagementComponent_Template_button_click_89_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Yesterday", "closureDate"));
    });
    i0.\u0275\u0275text(90, " Yesterday ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(91, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_91_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Last 7 Days"));
    })("click", function TestManagementComponent_Template_button_click_91_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Last 7 Days", "closureDate"));
    });
    i0.\u0275\u0275text(92, " Last 7 Days ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(93, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_93_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Last 30 Days"));
    })("click", function TestManagementComponent_Template_button_click_93_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Last 30 Days", "closureDate"));
    });
    i0.\u0275\u0275text(94, " Last 30 Days ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(95, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_95_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("This Month"));
    })("click", function TestManagementComponent_Template_button_click_95_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("This Month", "closureDate"));
    });
    i0.\u0275\u0275text(96, " This Month ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(97, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_97_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Last Month"));
    })("click", function TestManagementComponent_Template_button_click_97_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Last Month", "closureDate"));
    });
    i0.\u0275\u0275text(98, " Last Month ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(99, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_99_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Last Year"));
    })("click", function TestManagementComponent_Template_button_click_99_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Last Year", "closureDate"));
    });
    i0.\u0275\u0275text(100, " Last Year ");
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(101, "div", 61)(102, "div", 62)(103, "label", 63);
    i0.\u0275\u0275text(104, "From");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(105, "input", 64);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_105_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.startDate, $event) || (ctx.startDate = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(106, "div", 62)(107, "label", 63);
    i0.\u0275\u0275text(108, "To");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(109, "input", 65);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_109_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.endDate, $event) || (ctx.endDate = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275elementStart(110, "div", 66)(111, "button", 67);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_111_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.reset());
    });
    i0.\u0275\u0275text(112, " Reset ");
    i0.\u0275\u0275elementEnd()()()()();
    i0.\u0275\u0275elementStart(113, "nz-dropdown-menu", null, 2)(115, "div", 52)(116, "div", 53)(117, "input", 68);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_117_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isTotalFindingValue, $event) || (ctx.isTotalFindingValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("keydown", function TestManagementComponent_Template_input_keydown_117_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onKeydown("totalFindings"));
    })("keydown.enter", function TestManagementComponent_Template_input_keydown_enter_117_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onEnter("totalFindings"));
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(118, "button", 55);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_118_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.search("totalFindings"));
    });
    i0.\u0275\u0275text(119, " Search");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275text(120, "\xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(121, "button", 56);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_121_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.reset());
    });
    i0.\u0275\u0275text(122, " Reset ");
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(123, "nz-dropdown-menu", null, 3)(125, "div", 52)(126, "div", 53)(127, "div", 20)(128, "div", 57)(129, "input", 69);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_129_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.startDate, $event) || (ctx.startDate = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("keydown", function TestManagementComponent_Template_input_keydown_129_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onKeydown("updatedOn"));
    })("keydown.enter", function TestManagementComponent_Template_input_keydown_enter_129_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onEnter("updatedOn"));
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(130, "div", 59)(131, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_131_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Today"));
    })("click", function TestManagementComponent_Template_button_click_131_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Today", "updatedOn"));
    });
    i0.\u0275\u0275text(132, " Today ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(133, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_133_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Yesterday"));
    })("click", function TestManagementComponent_Template_button_click_133_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Yesterday", "updatedOn"));
    });
    i0.\u0275\u0275text(134, " Yesterday ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(135, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_135_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Last 7 Days"));
    })("click", function TestManagementComponent_Template_button_click_135_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Last 7 Days", "updatedOn"));
    });
    i0.\u0275\u0275text(136, " Last 7 Days ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(137, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_137_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Last 30 Days"));
    })("click", function TestManagementComponent_Template_button_click_137_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Last 30 Days", "updatedOn"));
    });
    i0.\u0275\u0275text(138, " Last 30 Days ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(139, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_139_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("This Month"));
    })("click", function TestManagementComponent_Template_button_click_139_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("This Month", "updatedOn"));
    });
    i0.\u0275\u0275text(140, " This Month ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(141, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_141_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Last Month"));
    })("click", function TestManagementComponent_Template_button_click_141_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Last Month", "updatedOn"));
    });
    i0.\u0275\u0275text(142, " Last Month ");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(143, "button", 60);
    i0.\u0275\u0275listener("mouseenter", function TestManagementComponent_Template_button_mouseenter_143_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.updateHoveredDate("Last Year"));
    })("click", function TestManagementComponent_Template_button_click_143_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.selectDateRange("Last Year", "updatedOn"));
    });
    i0.\u0275\u0275text(144, " Last Year ");
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(145, "div", 61)(146, "div", 62)(147, "label", 63);
    i0.\u0275\u0275text(148, "From");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(149, "input", 64);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_149_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.startDate, $event) || (ctx.startDate = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(150, "div", 62)(151, "label", 63);
    i0.\u0275\u0275text(152, "To");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(153, "input", 65);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_153_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.endDate, $event) || (ctx.endDate = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275elementStart(154, "div", 66)(155, "button", 67);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_155_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.reset());
    });
    i0.\u0275\u0275text(156, " Reset ");
    i0.\u0275\u0275elementEnd()()()()();
    i0.\u0275\u0275elementStart(157, "nz-dropdown-menu", null, 4)(159, "div", 52)(160, "div", 53)(161, "input", 70);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_161_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isLastUpdatedValue, $event) || (ctx.isLastUpdatedValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("keydown", function TestManagementComponent_Template_input_keydown_161_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onKeydown("updatedBy"));
    })("keydown.enter", function TestManagementComponent_Template_input_keydown_enter_161_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onEnter("updatedBy"));
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(162, "button", 55);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_162_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.search("updatedBy"));
    });
    i0.\u0275\u0275text(163, " Search");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275text(164, "\xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(165, "button", 56);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_165_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.reset());
    });
    i0.\u0275\u0275text(166, " Reset ");
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(167, "nz-dropdown-menu", null, 5)(169, "div", 52)(170, "div", 53)(171, "input", 71);
    i0.\u0275\u0275twoWayListener("ngModelChange", function TestManagementComponent_Template_input_ngModelChange_171_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isFirstCreatedValue, $event) || (ctx.isFirstCreatedValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("keydown", function TestManagementComponent_Template_input_keydown_171_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onKeydown("createdBy"));
    })("keydown.enter", function TestManagementComponent_Template_input_keydown_enter_171_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onEnter("createdBy"));
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(172, "button", 55);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_172_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.search("createdBy"));
    });
    i0.\u0275\u0275text(173, " Search");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275text(174, "\xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(175, "button", 56);
    i0.\u0275\u0275listener("click", function TestManagementComponent_Template_button_click_175_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.reset());
    });
    i0.\u0275\u0275text(176, " Reset ");
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(177, "div", 72);
    i0.\u0275\u0275template(178, TestManagementComponent_ng_template_178_Template, 27, 15, "ng-template", null, 6, i0.\u0275\u0275templateRefExtractor);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275template(180, TestManagementComponent_ng_template_180_Template, 21, 0, "ng-template", null, 7, i0.\u0275\u0275templateRefExtractor)(182, TestManagementComponent_ng_template_182_Template, 22, 4, "ng-template", null, 8, i0.\u0275\u0275templateRefExtractor)(184, TestManagementComponent_ng_template_184_Template, 18, 4, "ng-template", null, 9, i0.\u0275\u0275templateRefExtractor)(186, TestManagementComponent_ng_template_186_Template, 19, 4, "ng-template", null, 10, i0.\u0275\u0275templateRefExtractor)(188, TestManagementComponent_ng_template_188_Template, 9, 0, "ng-template", null, 11, i0.\u0275\u0275templateRefExtractor);
  }
  if (rf & 2) {
    const testTitle_r44 = i0.\u0275\u0275reference(70);
    const closureDate_r45 = i0.\u0275\u0275reference(80);
    const totalFindings_r46 = i0.\u0275\u0275reference(114);
    const updatedOn_r47 = i0.\u0275\u0275reference(124);
    const updatedBy_r48 = i0.\u0275\u0275reference(158);
    const createdBy_r49 = i0.\u0275\u0275reference(168);
    i0.\u0275\u0275advance(7);
    i0.\u0275\u0275property("ngIf", ctx.canManageTest || ctx.isAdmin);
    i0.\u0275\u0275advance(8);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.pageSize);
    i0.\u0275\u0275advance(11);
    i0.\u0275\u0275property("ngIf", ctx.canManageTest && ctx.setOfCheckedId.size > 0 || ctx.isAdmin && ctx.setOfCheckedId.size > 0);
    i0.\u0275\u0275advance(5);
    i0.\u0275\u0275property("nzData", ctx.listOfTestData)("nzShowPagination", false)("nzLoading", ctx.loading)("nzTotal", ctx.totalRecords)("nzPageSize", ctx.pageSize)("nzPageIndex", ctx.pageIndex)("nzCustomColumn", ctx.customColumn);
    i0.\u0275\u0275advance(3);
    i0.\u0275\u0275property("ngIf", ctx.canManageTest || ctx.isAdmin);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzSortPriority", true)("nzSortFn", true);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzVisible", ctx.isTestTitleVisible);
    i0.\u0275\u0275property("nzActive", ctx.isTestTitleValue.length > 0)("nzDropdownMenu", testTitle_r44);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzFilters", ctx.getTestType)("nzFilterFn", true)("nzFilterMultiple", false)("nzSortFn", true);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzSortFn", true);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzVisible", ctx.isclosureDateVisible);
    i0.\u0275\u0275property("nzActive", ctx.isClosureDateValue.length > 0)("nzDropdownMenu", closureDate_r45);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzFilters", ctx.getTestStatus)("nzFilterFn", true)("nzFilterMultiple", false)("nzSortFn", true);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzFilters", ctx.getTestScope)("nzFilterFn", true)("nzFilterMultiple", false)("nzSortFn", true)("nzTooltipTitle", "Test scope")("nzTooltipColor", ctx.color);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzSortFn", true);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzVisible", ctx.isTotalFindingVisible);
    i0.\u0275\u0275property("nzActive", ctx.isTotalFindingValue.length > 0)("nzDropdownMenu", totalFindings_r46);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzSortFn", true)("nzTooltipTitle", "Last activity test")("nzTooltipColor", ctx.color);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzVisible", ctx.isupdatedOnVisible);
    i0.\u0275\u0275property("nzActive", ctx.isupdatedOnValue.length > 0)("nzDropdownMenu", updatedOn_r47);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzSortFn", true)("nzTooltipTitle", "Last updated by")("nzTooltipColor", ctx.color);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzVisible", ctx.isLastUpdatedVisible);
    i0.\u0275\u0275property("nzActive", ctx.isLastUpdatedValue.length > 0)("nzDropdownMenu", updatedBy_r48);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzSortFn", true)("nzTooltipTitle", "First created by")("nzTooltipColor", ctx.color);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzVisible", ctx.isFirstCreatedVisible);
    i0.\u0275\u0275property("nzActive", ctx.isFirstCreatedValue.length > 0)("nzDropdownMenu", createdBy_r49);
    i0.\u0275\u0275advance(3);
    i0.\u0275\u0275property("ngForOf", ctx.listOfTestData);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("ngIf", ctx.listOfTestData.length);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("ngIf", ctx.isLoading);
    i0.\u0275\u0275advance(5);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.isTestTitleValue);
    i0.\u0275\u0275advance(12);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.startDate);
    i0.\u0275\u0275advance(20);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.startDate);
    i0.\u0275\u0275advance(4);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.endDate);
    i0.\u0275\u0275advance(8);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.isTotalFindingValue);
    i0.\u0275\u0275advance(12);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.startDate);
    i0.\u0275\u0275advance(20);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.startDate);
    i0.\u0275\u0275advance(4);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.endDate);
    i0.\u0275\u0275advance(8);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.isLastUpdatedValue);
    i0.\u0275\u0275advance(10);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.isFirstCreatedValue);
  }
}, dependencies: [i7.NgClass, i7.NgForOf, i7.NgIf, i9.NgSelectOption, i9.\u0275NgSelectMultipleOption, i9.DefaultValueAccessor, i9.CheckboxControlValueAccessor, i9.SelectControlValueAccessor, i9.NgControlStatus, i9.NgModel, i10.NzButtonComponent, i11.\u0275NzTransitionPatchDirective, i12.NzWaveDirective, i13.NzIconDirective, i14.NzColDirective, i14.NzRowDirective, i15.NzDropdownMenuComponent, i16.NzCheckboxComponent, i17.NzInputDirective, i18.NzPopoverDirective, i19.NzTableComponent, i19.NzThAddOnComponent, i19.NzTableCellDirective, i19.NzThMeasureDirective, i19.NzTdAddOnComponent, i19.NzTheadComponent, i19.NzTbodyComponent, i19.NzTrDirective, i19.NzCustomColumnDirective, i19.NzFilterTriggerComponent, i19.NzCellEllipsisDirective, i19.NzThSelectionComponent, i20.NzTooltipDirective, i21.NzPopconfirmDirective, FeatherIconDirective, i5.NgbPagination, i5.NgbPaginationNext, i5.NgbPaginationPrevious, i5.NgbProgressbar, i23.CdkDropList, i23.CdkDrag], styles: [`

.dataTable-top[_ngcontent-%COMP%]   .dataTable-dropdown[_ngcontent-%COMP%]   label[_ngcontent-%COMP%] {
  display: flex;
  align-items: center;
}
.dataTable-top[_ngcontent-%COMP%]   .dataTable-dropdown[_ngcontent-%COMP%]   label[_ngcontent-%COMP%]   select[_ngcontent-%COMP%] {
  display: block;
  width: auto;
  margin-right: 0.5rem;
  padding: 0.469rem 2.4rem 0.469rem 0.8rem;
  -moz-padding-start: calc(0.8rem - 3px);
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5;
  color: #000;
  background-color: #fff;
  background-repeat: no-repeat;
  background-position: right 0.8rem center;
  background-size: 16px 12px;
  border: 1px solid #e9ecef;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  -webkit-appearance: none;
  appearance: none;
  outline: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath fill='none' stroke='%237987a1' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/%3E%3C/svg%3E");
}
th[_ngcontent-%COMP%] {
  width: 100px;
}
.example-container[_ngcontent-%COMP%] {
  height: 350px;
  display: flex;
  flex-direction: column;
}
.example-list[_ngcontent-%COMP%] {
  min-height: 60px;
  border-radius: 4px;
  overflow-x: hidden;
  overflow-y: auto;
  display: block;
  border: 1px dashed #ccc;
  flex: 1 1 auto;
}
.example-list[_ngcontent-%COMP%]    > .example-box[_ngcontent-%COMP%] {
  cursor: move;
}
.CsvCheckbox-box[_ngcontent-%COMP%]   label[_ngcontent-%COMP%] {
  cursor: move;
}
.icon[_ngcontent-%COMP%] {
  pointer-events: none;
}
.cdk-drag-preview[_ngcontent-%COMP%] {
  box-sizing: border-box;
  border-radius: 4px;
  box-shadow:
    0 5px 5px -3px rgba(0, 0, 0, 0.2),
    0 8px 10px 1px rgba(0, 0, 0, 0.14),
    0 3px 14px 2px rgba(0, 0, 0, 0.12);
}
.cdk-drag-placeholder[_ngcontent-%COMP%] {
  opacity: 0;
}
.cdk-drag-animating[_ngcontent-%COMP%] {
  transition: transform 250ms cubic-bezier(0, 0, 0.2, 1);
}
.example-list.cdk-drop-list-dragging[_ngcontent-%COMP%]   .example-box[_ngcontent-%COMP%]:not(.cdk-drag-placeholder) {
  transition: transform 250ms cubic-bezier(0, 0, 0.2, 1);
}
.example-box[_ngcontent-%COMP%] {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  margin: 4px;
  padding: 4px 8px;
  background-color: rgba(0, 112, 204, 0.15);
}
.CsvCheckbox-box[_ngcontent-%COMP%] {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  margin: 4px;
  padding: 4px 8px;
  background-color: #e4e6f9;
  cursor: move;
}
.CsvCheckbox-box[_ngcontent-%COMP%]   input[_ngcontent-%COMP%] {
  cursor: pointer;
}
.selectAll-box[_ngcontent-%COMP%] {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  margin: 4px;
  padding: 4px 8px;
}
.example-box[_ngcontent-%COMP%]   span[_ngcontent-%COMP%] {
  cursor: pointer;
}
.dateSearch[_ngcontent-%COMP%] {
  height: 30px;
  width: 100px;
  font-size: 12px;
  font-weight: 400;
}
.searchbtn[_ngcontent-%COMP%] {
  --bs-btn-padding-y: -0px;
}
.search-box[_ngcontent-%COMP%]   .colsureButton[_ngcontent-%COMP%] {
  width: 100px;
}
.list-group-item[_ngcontent-%COMP%]:hover, .list-group-item.active[_ngcontent-%COMP%] {
  background-color: #5660d9;
  color: #fff;
  cursor: pointer;
}
.list-group[_ngcontent-%COMP%] {
  --bs-list-group-border-color: none;
  --bs-list-group-item-padding-y: 5px;
}
.dayBtn[_ngcontent-%COMP%] {
  width: 200px;
}
.clsInput[_ngcontent-%COMP%] {
  width: 200px;
}
.loader-overlay[_ngcontent-%COMP%] {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.8);
  z-index: 1000;
}
.loader-container[_ngcontent-%COMP%] {
  width: 50%;
}
.icon[_ngcontent-%COMP%] {
  margin-right: 2px;
}
.form-check[_ngcontent-%COMP%] {
  display: flex;
  align-items: center;
  padding: 0px !important;
}
.form-check-input[_ngcontent-%COMP%] {
  margin: 0px;
}
.ml-2[_ngcontent-%COMP%] {
  margin-left: 8px;
}
.PPTCheckbox-box[_ngcontent-%COMP%] {
  margin: 4px;
  padding: 4px 8px;
  cursor: move;
}
.PPTCheckbox-box[_ngcontent-%COMP%]   label[_ngcontent-%COMP%] {
  cursor: move;
}
.report-Icon[_ngcontent-%COMP%]   .word[_ngcontent-%COMP%] {
  color: rgb(55, 141, 211);
}
.report-Icon[_ngcontent-%COMP%]   .ppt[_ngcontent-%COMP%] {
  color: rgb(216, 92, 92);
}
.report-Icon[_ngcontent-%COMP%]   .xml[_ngcontent-%COMP%] {
  color: rgb(53, 134, 228);
}
.report-Icon[_ngcontent-%COMP%]   .csv[_ngcontent-%COMP%] {
  color: rgb(81, 170, 104);
}
.modal-body.position-relative[_ngcontent-%COMP%] {
  position: relative;
}
.spinner-overlay[_ngcontent-%COMP%] {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1050;
}
.spinner[_ngcontent-%COMP%] {
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-radius: 50%;
  border-top: 4px solid #3498db;
  width: 40px;
  height: 40px;
  animation: _ngcontent-%COMP%_spin 1s linear infinite;
}
@keyframes _ngcontent-%COMP%_spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.btn_icon[_ngcontent-%COMP%]:hover {
  transform: scale(1.2);
}
/*# sourceMappingURL=test-management.component.css.map */`] });
var TestManagementComponent = _TestManagementComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i0.\u0275setClassDebugInfo(TestManagementComponent, { className: "TestManagementComponent", filePath: "src/app/modules/test/test-management/test-management.component.ts", lineNumber: 37 });
})();

// src/app/modules/test/test-updates/test-updates.component.ts
import { Component as Component2 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { Validators } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i02 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i110 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";
import * as i22 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i3 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
import * as i4 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i8 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_core_transition-patch.js?v=ca23e844";
import * as i92 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_tooltip.js?v=ca23e844";
import * as i102 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@ng-select_ng-select.js?v=ca23e844";
import * as i122 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@ng-bootstrap_ng-bootstrap.js?v=ca23e844";
import * as i132 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-multiselect-dropdown.js?v=ca23e844";
import * as i142 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-quill.js?v=ca23e844";
var _c02 = () => ({ standalone: true });
function TestUpdatesComponent_div_12_Template(rf, ctx) {
  if (rf & 1) {
    const _r2 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 79)(1, "input", 96);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_div_12_Template_input_change_1_listener() {
      i02.\u0275\u0275restoreView(_r2);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.onReviewChange("isInProgress", true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(2, "label", 97);
    i02.\u0275\u0275text(3, " In Progress ");
    i02.\u0275\u0275elementEnd()();
  }
}
function TestUpdatesComponent_div_13_div_1_Template(rf, ctx) {
  if (rf & 1) {
    const _r4 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div")(1, "div", 79)(2, "label", 98);
    i02.\u0275\u0275text(3, "I Review ");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(4, "div", 79)(5, "input", 99);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_div_13_div_1_Template_input_change_5_listener() {
      i02.\u0275\u0275restoreView(_r4);
      const ctx_r2 = i02.\u0275\u0275nextContext(2);
      return i02.\u0275\u0275resetView(ctx_r2.onReviewChange("iReviewed", true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(6, "label", 100);
    i02.\u0275\u0275text(7, "Pass ");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(8, "div", 79)(9, "input", 101);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_div_13_div_1_Template_input_change_9_listener() {
      i02.\u0275\u0275restoreView(_r4);
      const ctx_r2 = i02.\u0275\u0275nextContext(2);
      return i02.\u0275\u0275resetView(ctx_r2.onReviewChange("iReviewed", false));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(10, "label", 102);
    i02.\u0275\u0275text(11, "Fail");
    i02.\u0275\u0275elementEnd()()();
  }
}
function TestUpdatesComponent_div_13_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_13_div_1_Template, 12, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", !(ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("isInProgress")) == null ? null : tmp_8_0.value) && !(ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("iReviewed")) == null ? null : tmp_8_0.value));
  }
}
function TestUpdatesComponent_div_14_div_1_Template(rf, ctx) {
  if (rf & 1) {
    const _r5 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div")(1, "div", 79)(2, "label", 103);
    i02.\u0275\u0275text(3, "II Review ");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(4, "div", 79)(5, "input", 104);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_div_14_div_1_Template_input_change_5_listener() {
      i02.\u0275\u0275restoreView(_r5);
      const ctx_r2 = i02.\u0275\u0275nextContext(2);
      return i02.\u0275\u0275resetView(ctx_r2.onReviewChange("iiReviewed", true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(6, "label", 105);
    i02.\u0275\u0275text(7, "Pass ");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(8, "div", 79)(9, "input", 106);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_div_14_div_1_Template_input_change_9_listener() {
      i02.\u0275\u0275restoreView(_r5);
      const ctx_r2 = i02.\u0275\u0275nextContext(2);
      return i02.\u0275\u0275resetView(ctx_r2.onReviewChange("iiReviewed", false));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(10, "label", 107);
    i02.\u0275\u0275text(11, "Fail");
    i02.\u0275\u0275elementEnd()()();
  }
}
function TestUpdatesComponent_div_14_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_14_div_1_Template, 12, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("iReviewed")) == null ? null : tmp_8_0.value) && !(ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("iiReviewed")) == null ? null : tmp_8_0.value));
  }
}
function TestUpdatesComponent_div_15_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 18);
    i02.\u0275\u0275element(1, "input", 108);
    i02.\u0275\u0275elementStart(2, "label", 109);
    i02.\u0275\u0275text(3, "Test Completed");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275text(4, " \xA0\xA0\xA0 ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_25_span_6_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "span");
    i02.\u0275\u0275text(1);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_9_0;
    const ctx_r2 = i02.\u0275\u0275nextContext(2);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275textInterpolate1(" [ First Created by ", (tmp_9_0 = ctx_r2.testForm.get("createdBy")) == null ? null : tmp_9_0.value, " ] ");
  }
}
function TestUpdatesComponent_div_25_span_7_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "span");
    i02.\u0275\u0275text(1);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_9_0;
    const ctx_r2 = i02.\u0275\u0275nextContext(2);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275textInterpolate1(" [ I Reviewed by ", (tmp_9_0 = ctx_r2.testForm.get("iReviewedBy")) == null ? null : tmp_9_0.value, " ] ");
  }
}
function TestUpdatesComponent_div_25_span_8_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "span");
    i02.\u0275\u0275text(1);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_9_0;
    const ctx_r2 = i02.\u0275\u0275nextContext(2);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275textInterpolate1(" [ II Reviewed by ", (tmp_9_0 = ctx_r2.testForm.get("iiReviewedBy")) == null ? null : tmp_9_0.value, " ] ");
  }
}
function TestUpdatesComponent_div_25_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 25)(1, "div", 72)(2, "div", 27)(3, "div", 28)(4, "div", 30)(5, "h6", 110);
    i02.\u0275\u0275template(6, TestUpdatesComponent_div_25_span_6_Template, 2, 1, "span", 16)(7, TestUpdatesComponent_div_25_span_7_Template, 2, 1, "span", 16)(8, TestUpdatesComponent_div_25_span_8_Template, 2, 1, "span", 16);
    i02.\u0275\u0275elementEnd()()()()()();
  }
  if (rf & 2) {
    let tmp_8_0;
    let tmp_9_0;
    let tmp_10_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("ngIf", (ctx_r2 == null ? null : ctx_r2.testId) && ((tmp_8_0 = ctx_r2.testForm.get("createdBy")) == null ? null : tmp_8_0.value));
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_9_0 = ctx_r2.testForm.get("iReviewed")) == null ? null : tmp_9_0.value);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_10_0 = ctx_r2.testForm.get("iiReviewed")) == null ? null : tmp_10_0.value);
  }
}
function TestUpdatesComponent_div_37_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please select Project! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_37_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_37_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("projectId")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_42_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please select Test! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_42_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_42_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("revalTestId")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_49_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please enter Test Name! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_49_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_49_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("testTitle")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_56_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please enter Test Description! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_56_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_56_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("testDesc")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_79_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please enter Contact Person! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_79_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_79_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("contactPerson")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_86_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Mobile number is required. ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_86_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Invalid mobile number format. ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_86_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_86_div_1_Template, 2, 0, "div", 16)(2, TestUpdatesComponent_div_86_div_2_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    let tmp_9_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_8_0 = ctx_r2.testForm.get("contactNumber")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_9_0 = ctx_r2.testForm.get("contactNumber")) == null ? null : tmp_9_0.errors == null ? null : tmp_9_0.errors["pattern"]);
  }
}
function TestUpdatesComponent_div_93_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Please enter your valid email-ID!");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_93_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_93_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("emailId")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]) || (ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("emailId")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["email"]));
  }
}
function TestUpdatesComponent_div_104_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please select Test Scope! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_104_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_104_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("testScopeId")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_span_108_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "span", 32);
    i02.\u0275\u0275text(1, " *");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_110_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please select Test Type! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_110_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_110_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("testNameId")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_115_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please select Test Status! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_115_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_115_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("testStatusId")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_122_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Enter report title! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_122_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_122_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("reportTitle")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_133_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please select Scheduled Start Date! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_133_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Assign Date must be on or before Closure Date! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_133_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_133_div_1_Template, 2, 0, "div", 16)(2, TestUpdatesComponent_div_133_div_2_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("assignDate")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : ctx_r2.testForm.errors == null ? null : ctx_r2.testForm.errors["assignDateGreaterThanClosureDate"]);
  }
}
function TestUpdatesComponent_div_144_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please select Scheduled End Date! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_144_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_144_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("closureDate")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_151_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please enter Hours Allocated! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_151_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Hours Allocated cannot be negative! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_151_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_151_div_1_Template, 2, 0, "div", 16)(2, TestUpdatesComponent_div_151_div_2_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    let tmp_9_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("hoursAllocated")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_9_0 = ctx_r2.testForm.get("hoursAllocated")) == null ? null : tmp_9_0.errors == null ? null : tmp_9_0.errors["min"]);
  }
}
function TestUpdatesComponent_div_162_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please enter Credentials! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_162_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_162_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("credential")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_173_Template(rf, ctx) {
  if (rf & 1) {
    const _r10 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 30)(1, "div", 65)(2, "input", 111);
    i02.\u0275\u0275twoWayListener("ngModelChange", function TestUpdatesComponent_div_173_Template_input_ngModelChange_2_listener($event) {
      i02.\u0275\u0275restoreView(_r10);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      i02.\u0275\u0275twoWayBindingSet(ctx_r2.complianceRequirement, $event) || (ctx_r2.complianceRequirement = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(3, "button", 67);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_div_173_Template_button_click_3_listener() {
      i02.\u0275\u0275restoreView(_r10);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.complianceRequirementAdd());
    });
    i02.\u0275\u0275element(4, "i", 68);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(5, "button", 112);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_div_173_Template_button_click_5_listener() {
      i02.\u0275\u0275restoreView(_r10);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.toggleInputBox());
    });
    i02.\u0275\u0275element(6, "i", 113);
    i02.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx_r2.complianceRequirement);
    i02.\u0275\u0275property("ngModelOptions", i02.\u0275\u0275pureFunction0(2, _c02));
  }
}
function TestUpdatesComponent_span_181_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "span", 32);
    i02.\u0275\u0275text(1, " *");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_182_Template(rf, ctx) {
  if (rf & 1) {
    const _r11 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 114)(1, "div", 115)(2, "div", 116)(3, "div", 117)(4, "div");
    i02.\u0275\u0275text(5);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(6, "div")(7, "span", 118);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_div_182_Template_span_click_7_listener() {
      const i_r12 = i02.\u0275\u0275restoreView(_r11).index;
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.removeAppendix(i_r12));
    });
    i02.\u0275\u0275element(8, "i", 119);
    i02.\u0275\u0275elementEnd()()()()();
    i02.\u0275\u0275elementStart(9, "div", 115)(10, "label", 49);
    i02.\u0275\u0275text(11, "Asset Description");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(12, "textarea", 120);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_div_182_Template_textarea_keydown_12_listener() {
      i02.\u0275\u0275restoreView(_r11);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(13, "div", 115)(14, "label", 49);
    i02.\u0275\u0275text(15, "Criticality of Asset");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(16, "ng-select", 121);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(17, "div", 115)(18, "label", 49);
    i02.\u0275\u0275text(19, "Internal IP Address");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(20, "input", 122);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_div_182_Template_input_keydown_20_listener() {
      i02.\u0275\u0275restoreView(_r11);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(21, "div", 115)(22, "label", 49);
    i02.\u0275\u0275text(23, "Public IP Address");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(24, "input", 123);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_div_182_Template_input_keydown_24_listener() {
      i02.\u0275\u0275restoreView(_r11);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(25, "div", 115)(26, "label", 49);
    i02.\u0275\u0275text(27, "URL");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(28, "input", 124);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_div_182_Template_input_keydown_28_listener() {
      i02.\u0275\u0275restoreView(_r11);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(29, "div", 115)(30, "label", 49);
    i02.\u0275\u0275text(31, "Version");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(32, "input", 125);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_div_182_Template_input_keydown_32_listener() {
      i02.\u0275\u0275restoreView(_r11);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const i_r12 = ctx.index;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275property("formGroupName", i_r12);
    i02.\u0275\u0275advance(5);
    i02.\u0275\u0275textInterpolate1("Scope : ", i_r12 + 1, "");
    i02.\u0275\u0275advance(11);
    i02.\u0275\u0275property("items", ctx_r2.criticalityOfAssetData);
  }
}
function TestUpdatesComponent_div_186_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275text(1, " Please fill in some fields before adding. ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_197_Template(rf, ctx) {
  if (rf & 1) {
    const _r13 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 30)(1, "textarea", 126);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_div_197_Template_textarea_keydown_1_listener() {
      i02.\u0275\u0275restoreView(_r13);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd()();
  }
}
function TestUpdatesComponent_div_216_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please enter Assets page! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_216_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Assets page cannot be negative! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_216_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_216_div_1_Template, 2, 0, "div", 16)(2, TestUpdatesComponent_div_216_div_2_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    let tmp_9_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("totalPages")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_9_0 = ctx_r2.testForm.get("totalPages")) == null ? null : tmp_9_0.errors == null ? null : tmp_9_0.errors["min"]);
  }
}
function TestUpdatesComponent_div_223_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please select Team Leader! ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_223_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275template(1, TestUpdatesComponent_div_223_div_1_Template, 2, 0, "div", 16);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_8_0;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.testForm == null ? null : (tmp_8_0 = ctx_r2.testForm.get("teamLeaderId")) == null ? null : tmp_8_0.errors == null ? null : tmp_8_0.errors["required"]);
  }
}
function TestUpdatesComponent_div_231_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275text(1, " Please select II Reviewer ");
    i02.\u0275\u0275elementEnd();
  }
}
function TestUpdatesComponent_div_239_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 32);
    i02.\u0275\u0275text(1, " Please select Assign Analyst ");
    i02.\u0275\u0275elementEnd();
  }
}
var _TestUpdatesComponent = class _TestUpdatesComponent {
  constructor(toastr, router, location, fb, testService, CommonService2, loaderService) {
    this.toastr = toastr;
    this.router = router;
    this.location = location;
    this.fb = fb;
    this.testService = testService;
    this.CommonService = CommonService2;
    this.loaderService = loaderService;
    this.state = this.location.getState();
    this.listOfProjects = [];
    this.testName = [];
    this.getTestStatus = [];
    this.getTestScope = [];
    this.testTypeWeb = false;
    this.testTypeMobile = false;
    this.startDate = /* @__PURE__ */ new Date();
    this.todayDate = /* @__PURE__ */ new Date();
    this.assignDate = /* @__PURE__ */ new Date();
    this.color = "black";
    this.isDisabled = true;
    this.testList = [];
    this.testSeqId = null;
    this.complianceRequirementList = [];
    this.testDetails = [];
    this.testScopeIdForReval = null;
    this.revalTestId = null;
    this.hasUnsavedChanges = false;
    this.preContentConfig = {
      toolbar: {
        container: [
          ["bold", "italic", "underline", "link"]
        ]
      }
    };
    this.criticalityOfAssetData = [
      { criticalityOfAsset: "Low (Level 1)" },
      { criticalityOfAsset: "High (Level 2)" },
      { criticalityOfAsset: "Critical (Level 3)" }
    ];
    this.isLoading = false;
    this.PHONE_NUMBER_REGEX = /^(?:\+\d{1,3}\s?)?\d{10}$/;
    this.canManageIReview = false;
    this.canManageIIReview = false;
    this.isEngagementScope = false;
    this.isLoadingProject = false;
    this.isLoadingTest = false;
    this.isLoadingTL = false;
    this.base64String = null;
    this.settingsReviewer = {
      singleSelection: false,
      idField: "_id",
      textField: "userName",
      enableCheckAll: true,
      selectAllText: "Select all II Reviewer",
      unSelectAllText: "Unselect all II Reviewer",
      allowSearchFilter: true,
      limitSelection: -1,
      clearSearchFilter: true,
      maxHeight: 197,
      itemsShowLimit: 4,
      searchPlaceholderText: "Search II Reviewer",
      noDataAvailablePlaceholderText: "Empty II Reviewer",
      closeDropDownOnSelection: false,
      showSelectedItemsAtTop: false,
      defaultOpen: false
    };
    this.settingsAssignAnalyst = {
      singleSelection: false,
      idField: "_id",
      textField: "userName",
      enableCheckAll: true,
      selectAllText: "Select all Assign Analyst",
      unSelectAllText: "Unselect all Assign Analyst",
      allowSearchFilter: true,
      limitSelection: -1,
      clearSearchFilter: true,
      maxHeight: 197,
      itemsShowLimit: 4,
      searchPlaceholderText: "Search Assign Analyst",
      noDataAvailablePlaceholderText: "Empty Assign Analyst",
      closeDropDownOnSelection: false,
      showSelectedItemsAtTop: false,
      defaultOpen: false
    };
    this.assignedIIReviewers = [];
    this.assignedAnalysts = [];
    this.showInputBox = false;
    this.CRsettings = {
      singleSelection: false,
      idField: "complianceRequirementId",
      textField: "complianceRequirement",
      enableCheckAll: true,
      selectAllText: "Select Compliance Requirement",
      unSelectAllText: "Unselect Compliance Requirement",
      allowSearchFilter: true,
      limitSelection: -1,
      clearSearchFilter: true,
      maxHeight: 197,
      itemsShowLimit: 4,
      searchPlaceholderText: "Search Compliance Requirement",
      noDataAvailablePlaceholderText: "Empty Compliance Requirement",
      closeDropDownOnSelection: false,
      showSelectedItemsAtTop: false,
      defaultOpen: false
    };
    this.complianceRequirement = "";
    this.complianceRequirementIds = [];
    this.assignDate = this.CommonService.convertDate(this.todayDate);
    this.closureDate = this.CommonService.convertDate(this.todayDate);
  }
  ngOnInit() {
    this.testId = this.state?.testId;
    this.init();
    this.allDropDownCall();
    this.convertDate(this.assignDate, "assignDate");
    this.convertDate(this.closureDate, "closureDate");
    if (this.state?.projectId) {
      this.testForm.get("projectId")?.setValue(this.state?.projectId);
      this.getAnalystData(this.state?.projectId);
    }
    if (this.testId) {
      this.getTestDetails(this.testId);
    }
  }
  allDropDownCall() {
    this.testListData(true);
    this.getProjectList();
    this.getTestTypeScopeStatusData();
    this.complianceRequirementLists();
    this.getTeamLeaderData();
  }
  init() {
    this.testForm = this.fb.group({
      isActive: [true],
      zeroKnowledge: [false],
      testCompleted: [false],
      isFirstReview: [false],
      projectId: [""],
      revalTestId: [Validators.required],
      testTitle: [{ value: "", disabled: false }, Validators.required],
      reportTitle: ["", Validators.required],
      testDesc: ["", Validators.required],
      startDate: [null],
      endDate: [null],
      contactPerson: ["", Validators.required],
      contactNumber: ["", [Validators.required, Validators.pattern(this.PHONE_NUMBER_REGEX)]],
      emailId: ["", [Validators.required, Validators.email]],
      testScopeId: [null, Validators.required],
      testNameId: [null, Validators.required],
      testStatusId: [null],
      assignDate: [this.assignDate, Validators.required],
      closureDate: [this.closureDate, Validators.required],
      hoursAllocated: [null, Validators.required],
      actualHours: [0],
      codePath: [""],
      credential: ["", Validators.required],
      complianceRequirementIds: [[]],
      isOutOfScope: [false],
      outOfScopeDesc: [""],
      totalPages: ["", Validators.required],
      teamLeaderId: [null, Validators.required],
      isInProgress: [true],
      isInProgressPass: [true],
      isInProgressFail: [false],
      iReviewedPass: [false],
      iReviewedFail: [false],
      iiReviewedPass: [false],
      iiReviewedFail: [false],
      iReviewed: [false],
      iiReviewed: [false],
      iReviewedBy: "",
      iiReviewedBy: "",
      createdBy: "",
      engagementScope: this.fb.array([this.createEngagementScopeGroup()])
    }, { validators: this.dateValidator });
  }
  dateValidator(control) {
    const assignDate = control.get("assignDate")?.value;
    const closureDate = control.get("closureDate")?.value;
    if (assignDate && closureDate && assignDate > closureDate) {
      return { assignDateGreaterThanClosureDate: true };
    }
    return null;
  }
  createEngagementScopeGroup() {
    return this.fb.group({
      assetDesc: [""],
      criticalityOfAsset: [null],
      internalIP: [""],
      publicIP: [""],
      url: [""],
      version: [""]
    });
  }
  get contactNumber() {
    return this.testForm.get("contactNumber");
  }
  updateValidators() {
    const control = this.testForm.get("testNameId");
    if (this.testName && this.testName.length > 0) {
      control.setValidators(Validators.required);
    } else {
      control.clearValidators();
    }
    control.updateValueAndValidity();
  }
  getTestDetails(id, isChange) {
    this.loaderService.show();
    this.testService.GetTestDetails(id).subscribe({
      next: (response) => {
        if (response.status === true) {
          const data = response.data[0];
          this.testDetails = data;
          this.testSeqId = data?.testSeqId;
          this.testForm.patchValue(__spreadValues({}, data));
          this.testForm.get("isInProgressPass")?.setValue(data.isInProgress);
          this.testForm.get("testScopeId")?.setValue(data.testScopeId);
          this.assignedIIReviewers = data?.assignedIIReviewers;
          this.assignedAnalysts = data?.assignedAnalysts;
          this.getIIReviverData(data?.teamLeaderId);
          this.getAnalystData(data?.projectId);
          this.assignDate = this.CommonService.convertDate(data?.assignDate);
          this.closureDate = this.CommonService.convertDate(data?.closureDate);
          this.startDate = this.CommonService.convertDate(data?.startDate ?? "");
          this.endDate = this.CommonService.convertDate(data?.endDate ?? "");
          if (isChange) {
            this.testForm.get("testScopeId")?.setValue(this.testScopeIdForReval);
            this.testForm.get("revalTestId")?.setValue(this.revalTestId);
            this.testForm.get("testStatusId")?.setValue("666192d8740fc56380d9f482");
            this.testForm.get("isInProgress")?.setValue(true);
            this.testForm.get("isInProgressPass")?.setValue(true);
            this.testForm.get("iReviewed")?.setValue(false);
            this.testForm.get("iiReviewed")?.setValue(false);
            this.testForm.get("testCompleted")?.setValue(false);
            this.testForm.get("actualHours")?.setValue(0);
            this.assignDate = this.CommonService.convertDate(this.todayDate);
            this.closureDate = this.CommonService.convertDate(this.todayDate);
            this.startDate = null;
            this.endDate = null;
          }
          this.permissionForReview(id);
          this.loaderService.hide();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  permissionForReview(testId) {
    this.loaderService.show();
    this.testService.PermissionForReview(testId).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.canManageIReview = response.data?.canManageIReview;
          this.canManageIIReview = response.data?.canManageIIReview;
          this.loaderService.hide();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return;
      }
    });
  }
  formatDate(dateString) {
    const date = new Date(dateString);
    return `${date.getFullYear()}-${("0" + (date.getMonth() + 1)).slice(-2)}-${("0" + date.getDate()).slice(-2)}`;
  }
  onReviewChange(reviewType, isPass) {
    if (reviewType === "iReviewed") {
      if (isPass) {
        this.testForm.get("iReviewedFail")?.setValue(false);
      } else {
        this.testForm.get("iReviewedPass")?.setValue(false);
      }
    } else if (reviewType === "iiReviewed") {
      if (isPass) {
        this.testForm.get("iiReviewedFail")?.setValue(false);
      } else {
        this.testForm.get("iiReviewedPass")?.setValue(false);
      }
    } else if (reviewType === "isInProgress") {
      if (isPass) {
        this.testForm.get("isInProgressFail")?.setValue(false);
        this.testForm.get("iReviewedFail")?.setValue(false);
      } else {
        this.testForm.get("isInProgressPass")?.setValue(false);
      }
    }
  }
  removePTags(str) {
    if (typeof str === "string") {
      return str.replace(/<\/?p>/g, "");
    }
    return str;
  }
  onKeyPressInputChange(hasUnsavedChanges) {
    this.hasUnsavedChanges = hasUnsavedChanges;
  }
  // Appendix
  get engagementScope() {
    return this.testForm.get("engagementScope");
  }
  addEngagement() {
    const lastEngagementScope = this.engagementScope.at(this.engagementScope.length - 1);
    if (lastEngagementScope) {
      if (this.isScopeValid(lastEngagementScope)) {
        this.engagementScope.push(this.createEngagementScopeGroup());
        this.isEngagementScope = false;
      } else {
        this.isEngagementScope = true;
        this.toastr.warning("Please fill in some fields before adding.", "Test Checklist Management");
      }
    } else {
      const lastEngagementScope2 = this.fb.group({
        assetDesc: [""],
        criticalityOfAsset: [null],
        internalIP: [""],
        publicIP: [""],
        url: [""],
        version: [""]
      });
      this.engagementScope.push(lastEngagementScope2);
    }
  }
  isScopeValid(scope) {
    const assetDesc = scope.get("assetDesc")?.value?.trim();
    const criticalityOfAsset = scope.get("criticalityOfAsset")?.value;
    const internalIP = scope.get("internalIP")?.value?.trim();
    const publicIP = scope.get("publicIP")?.value?.trim();
    const url = scope.get("url")?.value?.trim();
    const version = scope.get("version")?.value?.trim();
    return assetDesc || criticalityOfAsset || internalIP || publicIP || url || version;
  }
  removeAppendix(index) {
    if (index >= 0 && index < this.engagementScope.length) {
      this.engagementScope.removeAt(index);
      this.reIndexAppendix();
    }
  }
  reIndexAppendix() {
    this.engagementScope.controls.forEach((step, index) => {
      step.get("orderId")?.setValue(index + 1);
    });
  }
  isEngagementScopeEmpty(engagementScope) {
    if (!Array.isArray(engagementScope) || engagementScope.length === 0) {
      return true;
    }
    return engagementScope.every((item) => !item.assetDesc && item.criticalityOfAsset === null && !item.internalIP && !item.publicIP && !item.url && !item.version);
  }
  onSubmit() {
    let hasErrors = false;
    if (this.testForm.get("testScopeId")?.value === "666192a1740fc56380d9f44c") {
      this.testForm.get("revalTestId")?.clearValidators();
      this.testForm.get("revalTestId")?.updateValueAndValidity();
    } else {
      this.testForm.get("revalTestId")?.setValidators([Validators.required]);
      this.testForm.get("revalTestId")?.updateValueAndValidity();
    }
    //if (this.testForm.valid) {
      const formData = this.testForm.value;
      formData.assignDate = this.formatDate(formData.assignDate);
      formData.closureDate = this.formatDate(formData.closureDate);
      this.testForm.get("isInProgress")?.setValue(formData.isInProgressPass);
      if (formData.iReviewedPass) {
        this.testForm.get("iReviewed")?.setValue(true);
      } else if (formData.iReviewedFail) {
        this.testForm.get("iReviewed")?.setValue(false);
        this.testForm.get("isInProgress")?.setValue(true);
      }
      if (formData.iiReviewedPass) {
        this.testForm.get("iiReviewed")?.setValue(true);
      } else if (formData.iiReviewedFail) {
        this.testForm.get("iiReviewed")?.setValue(false);
        this.testForm.get("iReviewed")?.setValue(false);
      }
      if (this.isEngagementScopeEmpty(formData.engagementScope)) {
        this.testForm.value.engagementScope = [];
      }
      if (this.testId) {
        this.editTestData(this.testForm.value);
      } else if (this.testScopeIdForReval) {
        this.saveRevalData(this.testForm.value);
      } else {
        this.saveTestData(this.testForm.value);
      }
   // } else {
 //     Object.values(this.testForm.controls).forEach((control) => {
//        if (control.invalid) {
  //        control.markAsDirty();
    //      control.updateValueAndValidity({ onlySelf: true });
      //    hasErrors = true;
       // }
     // });
      //if (hasErrors) {
        //this.toastr.warning("Please verify all required fields", "Test Checklist Management");
      //}
    //}
  }
  saveRevalData(data) {
    const idsToAdd = this.assignedIIReviewers.filter((item) => item && typeof item === "object").map((item) => item._id);
    const uniqueIds = new Set(idsToAdd);
    const uniqueIdsArray = [...uniqueIds];
    uniqueIdsArray.forEach((id) => {
      if (!this.assignedIIReviewers.includes(id)) {
        this.assignedIIReviewers.push(id);
      }
    });
    const assignedIIReviewers = this.assignedIIReviewers.filter((x) => !x._id);
    const idsToAddassignedAnalysts = this.assignedAnalysts.filter((item) => item && typeof item === "object").map((item) => item._id);
    const uniqueIdsAssignedAnalysts = new Set(idsToAddassignedAnalysts);
    const uniqueIdsArrayAssignedAnalysts = [...uniqueIdsAssignedAnalysts];
    uniqueIdsArrayAssignedAnalysts.forEach((id) => {
      if (!this.assignedAnalysts.includes(id)) {
        this.assignedAnalysts.push(id);
      }
    });
    const assignedAnalysts = this.assignedAnalysts.filter((x) => !x._id);
    const payLoad = __spreadProps(__spreadValues({}, data), {
      testStatusId: "666192d8740fc56380d9f482",
      assignedIIReviewers,
      assignedAnalysts,
      kickoffDoc: this.kickoffDoc,
      isInProgress: true
    });
    delete payLoad.testSeqId;
    delete payLoad.iReviewed;
    delete payLoad.iiReviewed;
    delete payLoad.iReviewedBy;
    delete payLoad.iiReviewedBy;
    delete payLoad.iReviewedById;
    delete payLoad.iiReviewedById;
    delete payLoad.testCompleted;
    this.loaderService.show();
    this.testService.GetTestAdd(payLoad).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Test Management");
          this.loaderService.hide();
          this.goBack();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  saveTestData(data) {
    const idsToAdd = this.assignedIIReviewers.filter((item) => item && typeof item === "object").map((item) => item._id);
    const uniqueIds = new Set(idsToAdd);
    const uniqueIdsArray = [...uniqueIds];
    uniqueIdsArray.forEach((id) => {
      if (!this.assignedIIReviewers.includes(id)) {
        this.assignedIIReviewers.push(id);
      }
    });
    const assignedIIReviewers = this.assignedIIReviewers.filter((x) => !x._id);
    const idsToAddassignedAnalysts = this.assignedAnalysts.filter((item) => item && typeof item === "object").map((item) => item._id);
    const uniqueIdsAssignedAnalysts = new Set(idsToAddassignedAnalysts);
    const uniqueIdsArrayAssignedAnalysts = [...uniqueIdsAssignedAnalysts];
    uniqueIdsArrayAssignedAnalysts.forEach((id) => {
      if (!this.assignedAnalysts.includes(id)) {
        this.assignedAnalysts.push(id);
      }
    });
    const assignedAnalysts = this.assignedAnalysts.filter((x) => !x._id);
    const payLoad = __spreadProps(__spreadValues({}, data), {
      assignedIIReviewers,
      assignedAnalysts,
      kickoffDoc: this.kickoffDoc
    });
    this.loaderService.show();
    this.testService.GetTestAdd(payLoad).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Test Management");
          this.loaderService.hide();
          this.goBack();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  editTestData(data) {
    const idsToAdd = this.assignedIIReviewers.filter((item) => item && typeof item === "object").map((item) => item._id);
    const uniqueIds = new Set(idsToAdd);
    const uniqueIdsArray = [...uniqueIds];
    uniqueIdsArray.forEach((id) => {
      if (!this.assignedIIReviewers.includes(id)) {
        this.assignedIIReviewers.push(id);
      }
    });
    const assignedIIReviewers = this.assignedIIReviewers.filter((x) => !x._id);
    const idsToAddassignedAnalysts = this.assignedAnalysts.filter((item) => item && typeof item === "object").map((item) => item._id);
    const uniqueIdsAssignedAnalysts = new Set(idsToAddassignedAnalysts);
    const uniqueIdsArrayAssignedAnalysts = [...uniqueIdsAssignedAnalysts];
    uniqueIdsArrayAssignedAnalysts.forEach((id) => {
      if (!this.assignedAnalysts.includes(id)) {
        this.assignedAnalysts.push(id);
      }
    });
    const assignedAnalysts = this.assignedAnalysts.filter((x) => !x._id);
    const isReviewOnlyReset = {
      isInProgress: true,
      iReviewed: false,
      iiReviewed: false
    };
    if (this.hasUnsavedChanges) {
      this.testForm.get("iReviewed")?.setValue(false);
      this.testForm.get("iReviewedPass")?.setValue(false);
      this.testForm.get("iiReviewed")?.setValue(false);
      this.testForm.get("iiReviewedPass")?.setValue(false);
    }
    const payLoad = __spreadValues(__spreadProps(__spreadValues({
      testId: this.testId
    }, data), {
      assignedIIReviewers,
      assignedAnalysts,
      kickoffDoc: this.kickoffDoc
    }), this.hasUnsavedChanges ? isReviewOnlyReset : {});
    this.loaderService.show();
    this.testService.GetTestEdit(payLoad).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Test Management");
          this.hasUnsavedChanges = false;
          this.loaderService.hide();
          this.getTestDetails(this.testId);
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  getProjectList() {
    this.isLoadingProject = true;
    this.testService.GetProjectList().subscribe({
      next: (response) => {
        if (response.status === true) {
          const data = response.data;
          this.listOfProjects = data;
          this.isLoadingProject = false;
        }
      },
      error: (err) => {
        this.isLoadingProject = false;
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  getProjectSelect(projectId) {
    this.getAnalystData(projectId._id);
    this.hasUnsavedChanges = true;
  }
  testListData(isTestCompleted) {
    this.isLoading = true;
    this.testService.TestListData(isTestCompleted).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.testList = response.data;
          this.isLoading = false;
        }
      },
      error: (err) => {
        return;
      }
    });
  }
  onTestScopeChange(value) {
    this.testScopeIdForReval = value._id;
    this.testForm.get("testScopeId")?.setValue(value._id);
    this.testId = null;
    this.hasUnsavedChanges = true;
    if (value.name === "New") {
      this.testForm.get("revalTestId")?.clearValidators();
      this.testForm.get("revalTestId")?.updateValueAndValidity();
    } else {
      this.testForm.get("revalTestId")?.setValidators([Validators.required]);
      this.testForm.get("revalTestId")?.updateValueAndValidity();
    }
  }
  onTestNameChange(value) {
    this.hasUnsavedChanges = true;
  }
  onTestChange(value) {
    this.revalTestId = value.revalTestId;
    this.getTestDetails(value.revalTestId, true);
    this.testForm.get("revalTestId")?.setValue(value.revalTestId);
    this.hasUnsavedChanges = true;
  }
  getTestTypeScopeStatusData() {
    this.isLoading = true;
    this.testService.GetTestTypeScopeStatus().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.testName = response.data[0]?.testName;
          this.updateValidators();
          this.getTestStatus = response.data[0]?.testStatus;
          if (!this.testId) {
            this.testForm.get("testStatusId")?.setValue(this.getTestStatus[0]._id);
          }
          this.getTestScope = response.data[0]?.testScope;
          this.testForm.get("testScopeId")?.setValue(this.getTestScope[0]._id);
          this.isLoading = false;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  getTeamLeaderData() {
    this.isLoading = true;
    this.testService.GetTeamLead().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.teamLeadList = response.data;
          this.isLoading = false;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  getTeamLeadSelect(id) {
    const idData = this.testForm?.get("teamLeaderId")?.value;
    this.assignedIIReviewers = [];
    this.getIIReviverData(idData);
  }
  getIIReviverData(selectedTeamLeadId) {
    this.loaderService.show();
    this.testService.GetIIReviewer().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.IIReviewerList = response.data;
          this.IIReviewerList = this.IIReviewerList?.filter((user) => user._id !== selectedTeamLeadId);
          this.loaderService.hide();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  getAnalystData(projectId) {
    this.testService.GetAnalyst(projectId).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.analystList = response.data;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  onChange(result, dateType) {
    if (result && result.year && result.month && result.day) {
      this.convertDate(result, dateType);
      this.testForm.get(dateType)?.markAsDirty();
      this.hasUnsavedChanges = true;
    }
  }
  convertDate(date, dateType) {
    const year = date.year;
    const month = String(date.month).padStart(2, "0");
    const day = String(date.day).padStart(2, "0");
    date = `${year}-${month}-${day}`;
    if (dateType == "startDate") {
      this.testForm.get("startDate")?.setValue(date);
    }
    if (dateType == "endDate") {
      this.testForm.get("endDate")?.setValue(date);
    }
    if (dateType == "assignDate") {
      this.testForm.get("assignDate")?.setValue(date);
    }
    if (dateType == "closureDate") {
      this.testForm.get("closureDate")?.setValue(date);
    }
  }
  onFileChange(event) {
    const fileInput = event.target;
    const file = event.target.files[0];
    const allowedExtensions = /(\.docx|\.doc)$/i;
    if (!allowedExtensions.exec(file.name)) {
      fileInput.value = "";
      this.toastr.warning("Invalid file type. Only .docx and .doc files are allowed.", "Template upload");
      return;
    }
    this.hasUnsavedChanges = true;
    const reader = new FileReader();
    reader.onload = this._handleReaderLoaded.bind(this);
    reader.readAsDataURL(file);
  }
  _handleReaderLoaded(event) {
    const reader = event.target;
    this.base64String = reader.result;
    this.kickoffDoc = this.base64String;
  }
  onItemSelect(item, dropdownType) {
    this.hasUnsavedChanges = true;
    const id = item._id;
    if (dropdownType === "assignedIIReviewers") {
      if (!this.assignedIIReviewers.includes(id)) {
        this.assignedIIReviewers.push(id);
      }
    }
    if (dropdownType === "assignedAnalysts") {
      if (!this.assignedAnalysts.includes(id)) {
        this.assignedAnalysts.push(id);
      }
    }
  }
  onDeSelect(item, dropdownType) {
    this.hasUnsavedChanges = true;
    if (dropdownType == "assignedIIReviewers") {
      const data = this.assignedIIReviewers.filter((x) => x !== item._id);
      this.assignedIIReviewers = data;
    }
    if (dropdownType == "assignedAnalysts") {
      const data = this.assignedAnalysts.filter((x) => x !== item._id);
      this.assignedAnalysts = data;
    }
  }
  onSelectAll(items, dropdownType) {
    this.hasUnsavedChanges = true;
    const idsToAdd = items.map((item) => item._id);
    if (dropdownType === "assignedIIReviewers") {
      idsToAdd.forEach((id) => {
        if (!this.assignedIIReviewers.includes(id)) {
          this.assignedIIReviewers.push(id);
        }
      });
    }
    if (dropdownType === "assignedAnalysts") {
      idsToAdd.forEach((id) => {
        if (!this.assignedAnalysts.includes(id)) {
          this.assignedAnalysts.push(id);
        }
      });
    }
  }
  onDeSelectAll(items, dropdownType) {
    if (dropdownType == "assignedIIReviewers") {
      this.assignedIIReviewers = [];
    }
    if (dropdownType == "assignedAnalysts") {
      this.assignedAnalysts = [];
    }
    this.hasUnsavedChanges = true;
  }
  goBack() {
    this.location.back();
  }
  toggleInputBox() {
    this.showInputBox = !this.showInputBox;
  }
  onItemSelectCR(item) {
    this.complianceRequirementIds.push(item.complianceRequirementId);
    this.hasUnsavedChanges = true;
  }
  onDeSelectCR(item) {
    const data = this.complianceRequirementIds.filter((x) => x.complianceRequirementId !== item.complianceRequirementId);
    this.complianceRequirementIds = data;
    this.hasUnsavedChanges = true;
  }
  onSelectAllCR(items) {
    this.complianceRequirementIds = items.complianceRequirementId;
    this.hasUnsavedChanges = true;
  }
  onDeSelectAllCR(items) {
    this.complianceRequirementIds = items.complianceRequirementId;
    this.hasUnsavedChanges = true;
  }
  complianceRequirementAdd() {
    this.isLoading = true;
    this.testService.GetCRAdd({ complianceRequirement: this.complianceRequirement }).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Tests Management");
          this.complianceRequirement = "";
          this.complianceRequirementLists();
          this.showInputBox = false;
          this.isLoading = false;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Tests Management");
      }
    });
  }
  complianceRequirementDelete() {
    this.testService.GetCRDelete({ complianceRequirementIds: this.complianceRequirementIds }).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Tests Management");
          this.testForm.get("complianceRequirementIds")?.setValue([]);
          this.complianceRequirementIds = [];
          this.complianceRequirementLists();
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Tests Management");
      }
    });
  }
  complianceRequirementLists() {
    this.testService.GetCRList().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.complianceRequirementList = response.data;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Tests Management");
      }
    });
  }
};
_TestUpdatesComponent.\u0275fac = function TestUpdatesComponent_Factory(t) {
  return new (t || _TestUpdatesComponent)(i02.\u0275\u0275directiveInject(i110.ToastrService), i02.\u0275\u0275directiveInject(i22.Router), i02.\u0275\u0275directiveInject(i3.Location), i02.\u0275\u0275directiveInject(i4.FormBuilder), i02.\u0275\u0275directiveInject(TestService), i02.\u0275\u0275directiveInject(CommonService), i02.\u0275\u0275directiveInject(LoadingService));
};
_TestUpdatesComponent.\u0275cmp = /* @__PURE__ */ i02.\u0275\u0275defineComponent({ type: _TestUpdatesComponent, selectors: [["app-test-updates"]], decls: 240, vars: 96, consts: [["asd", "ngbDatepicker"], ["esd", "ngbDatepicker"], ["ssd", "ngbDatepicker"], ["sed", "ngbDatepicker"], ["multiSelect", ""], [1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "page-breadcrumb", "m-0"], [1, "breadcrumb", "mb-0"], [1, "breadcrumb-item"], [1, "abc", 3, "click"], ["aria-current", "page", 1, "breadcrumb-item", "active"], [1, "d-flex", "align-items-center", "flex-wrap", "text-nowrap", "button-container"], [1, "forms-sample", "d-flex", "flex-wrap", "justify-content-center", 3, "ngSubmit", "formGroup"], ["class", "form-check form-check-inline", 4, "ngIf"], [4, "ngIf"], ["class", "form-check form-switch", 4, "ngIf"], [1, "form-check", "form-switch"], ["type", "checkbox", "formControlName", "isActive", "id", "Active", 1, "form-check-input"], ["for", "Active", 1, "form-check-label"], [1, "button-container"], [1, "btn", "btn-secondary", "btn-icon-text", "mmb-2", "mb-md-0", 3, "click"], [1, "btn", "btn-primary", "btn-icon-text", "mmb-2", "mb-md-0", 3, "click"], ["class", "row", 4, "ngIf"], [1, "row"], [1, "col-md-6", "grid-margin", "stretch-card"], [1, "card"], [1, "card-body"], [1, "forms-sample", 3, "formGroup"], [1, "mb-3"], ["for", "Project", 1, "form-label"], [1, "text-danger"], ["bindLabel", "projectName", "bindValue", "_id", "placeholder", "Select project name", "formControlName", "projectId", 3, "change", "items", "loading"], ["class", "text-danger", 4, "ngIf"], ["for", "Test", 1, "form-label"], ["bindLabel", "testTitle", "bindValue", "revalTestId", "placeholder", "Select test", "formControlName", "revalTestId", 3, "change", "items", "readonly", "loading"], ["for", "TestName", 1, "form-label"], ["type", "text", "id", "TestName", "autocomplete", "off", "placeholder", "Enter Test title", "formControlName", "testTitle", 1, "form-control", 3, "keydown"], ["for", "TestDescription", 1, "form-label"], ["placeholder", "Enter test description", "formControlName", "testDesc", 3, "keydown", "modules"], ["for", "exampleInputPassword1", 1, "form-label"], [1, "input-group"], ["placeholder", "yyyy-mm-dd", "name", "dp", "ngbDatepicker", "", "readonly", "", 1, "form-control", "ng-untouched", "ng-pristine", "ng-valid", "date", 3, "ngModelChange", "ngModel", "ngModelOptions"], ["type", "button", "disabled", "", 1, "input-group-text", 3, "click"], [1, "feather", "icon-calendar", "icon-md", "text-muted"], ["type", "text", "nzTooltipTitle", "Project Leader Contact Person", "nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", "id", "exampleInputPassword1", "autocomplete", "off", "placeholder", "Enter contact person", "formControlName", "contactPerson", 1, "form-control", 3, "keydown", "nzTooltipColor"], ["type", "text", "id", "exampleInputPassword1", "autocomplete", "off", "placeholder", "Enter contact number", "nzTooltipTitle", "Project Leader Contact No", "nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", "formControlName", "contactNumber", 1, "form-control", 3, "keydown", "nzTooltipColor"], ["type", "email", "id", "exampleInputPassword1", "autocomplete", "off", "placeholder", "Enter email-id", "nzTooltipTitle", "Project Leader Email ID", "nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", "formControlName", "emailId", 1, "form-control", 3, "keydown", "nzTooltipColor"], ["for", "TestScope", 1, "form-label"], ["bindLabel", "testScopeDesc", "bindValue", "_id", "formControlName", "testScopeId", "placeholder", "Select test scope", 3, "change", "items", "loading"], ["for", "TestType", 1, "form-label"], ["bindLabel", "testName", "bindValue", "_id", "placeholder", "Select test type", "formControlName", "testNameId", 3, "change", "items", "loading"], ["bindLabel", "testStatusDesc", "bindValue", "_id", "placeholder", "Select test status", "formControlName", "testStatusId", 3, "items", "loading"], ["type", "text", "id", "reportTitle", "autocomplete", "off", "placeholder", "Enter Report title", "formControlName", "reportTitle", 1, "form-control"], ["for", "assignDate", 1, "form-label"], ["placeholder", "yyyy-mm-dd", "name", "dp", "ngbDatepicker", "", 1, "form-control", 3, "ngModelChange", "ngModel", "ngModelOptions"], ["type", "button", 1, "input-group-text", 3, "click"], ["placeholder", "yyyy-mm-dd", "name", "dp", "ngbDatepicker", "", 1, "form-control", "ng-untouched", "ng-pristine", "ng-valid", "date", 3, "ngModelChange", "ngModel", "ngModelOptions"], ["for", "hoursAllocated", 1, "form-label"], ["type", "number", "nzTooltipTitle", "Hours Allocated", "nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", "id", "hoursAllocated", "autocomplete", "off", "placeholder", "Enter hours allocated", "min", "0", "formControlName", "hoursAllocated", 1, "form-control", 3, "keydown", "nzTooltipColor"], ["for", "actualHours", 1, "form-label"], ["nzTooltipTitle", "Actual Hours = (Actual End Date - Actual Start Date(No. of days) * 6 hours per day)", "nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", "type", "text", "id", "actualHours", "autocomplete", "off", "placeholder", "Enter hours spent", "formControlName", "actualHours", "readonly", "", 1, "form-control", 3, "nzTooltipColor"], ["nzTooltipTitle", "Authentication credentials to access the resources of the application", "nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", "id", "TestDescription", "rows", "3", "placeholder", "Enter credentials", "formControlName", "credential", 1, "form-control", 3, "keydown", "nzTooltipColor"], [1, "form-label"], [1, "d-flex", "align-items-center"], ["placeholder", "Select compliance requirement", "formControlName", "complianceRequirementIds", 1, "select-flex", 3, "onSelect", "onDeSelect", "onSelectAll", "onDeSelectAll", "data", "settings", "disabled"], [1, "btn", "btn-outline-primary", "me-1", 3, "click"], [1, "feather", "icon-plus"], [1, "btn", "btn-danger", 3, "click"], [1, "feather", "icon-trash"], ["class", "mb-3", 4, "ngIf"], [1, "col-md-12", "grid-margin", "stretch-card"], [3, "formGroup"], ["formArrayName", "engagementScope", 1, "card-body"], [1, "card-title"], ["class", "row", 3, "formGroupName", 4, "ngFor", "ngForOf"], [1, "textRight", 3, "ngClass"], [1, "btn", "btn-primary", "btn-sm", 3, "click"], [1, "form-check", "form-check-inline"], ["type", "checkbox", "id", "isOutOfScope", "formControlName", "isOutOfScope", 1, "form-check-input"], ["for", "isOutOfScope", 1, "form-check-label"], [1, "row", "mb-3"], [1, "col-md-10"], ["for", "formFile", 1, "form-label"], ["nzTooltipTitle", "The Project Definition Statement which contains required information and instructions to continue the test", "nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", "type", "file", "id", "formFile", 1, "form-control", 3, "change", "nzTooltipColor", "disabled"], [1, "col-md-2", "mt-4", "d-flex", "align-items-center"], [1, "form-check", "form-check-inline", "m-0", "w", "textRight"], ["type", "checkbox", "nzTooltipTitle", "Disable Kick off document", "nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", "id", "Zero", "formControlName", "zeroKnowledge", 1, "form-check-input", "float_none", 3, "nzTooltipColor"], ["for", "Zero", 1, "form-check-label"], ["for", "Assestspage", 1, "form-label"], ["type", "number", "id", "Assestspage", "autocomplete", "off", "placeholder", "Enter assets page", "formControlName", "totalPages", "min", "0", 1, "form-control", 3, "keydown"], ["bindLabel", "userName", "bindValue", "_id", "placeholder", "Select team leader", "formControlName", "teamLeaderId", 3, "change", "items", "loading"], ["required", "", "required", "", 1, "form-label"], ["placeholder", "Select II reviewer", 3, "onSelect", "onDeSelect", "onSelectAll", "onDeSelectAll", "ngModelChange", "data", "settings", "disabled", "ngModel", "ngModelOptions"], ["placeholder", "Select assign analyst", 3, "onSelect", "onDeSelect", "onSelectAll", "onDeSelectAll", "ngModelChange", "data", "settings", "disabled", "ngModel", "ngModelOptions"], ["type", "checkbox", "id", "inProgress", "formControlName", "isInProgressPass", 1, "form-check-input", 3, "change"], ["for", "inProgress", 1, "form-check-label"], ["for", "iReviewedLabel", 1, "form-check-label", "custom-bold"], ["type", "checkbox", "id", "passReview", "formControlName", "iReviewedPass", 1, "form-check-input", 3, "change"], ["for", "passReview", 1, "form-check-label"], ["type", "checkbox", "id", "failReview", "formControlName", "iReviewedFail", 1, "form-check-input", 3, "change"], ["for", "failReview", 1, "form-check-label"], ["for", "iiReviewedLabel", 1, "form-check-label", "custom-bold"], ["type", "checkbox", "id", "passIIReview", "formControlName", "iiReviewedPass", 1, "form-check-input", 3, "change"], ["for", "passIIReview", 1, "form-check-label"], ["type", "checkbox", "id", "failIIReview", "formControlName", "iiReviewedFail", 1, "form-check-input", 3, "change"], ["for", "failIIReview", 1, "form-check-label"], ["type", "checkbox", "id", "testCompleted", "formControlName", "testCompleted", 1, "form-check-input"], ["for", "testCompleted", 1, "form-check-label"], [1, "card-title", "me-3", "d-flex", "align-items-center", "gap-5", "justify-content-center"], ["placeholder", "Add new compliance requirement", 1, "form-control", "select-flex", 3, "ngModelChange", "ngModel", "ngModelOptions"], [1, "btn", "btn-secondary", 3, "click"], [1, "feather", "icon-x"], [1, "row", 3, "formGroupName"], [1, "col-md-12", "mb-3"], [1, "card", "fw-semibold", "bg-purple"], [1, "card-body", "d-flex", "justify-content-between", "p-0", "p-2"], [3, "click"], ["data-feather", "trash-2", "appFeatherIcon", "", 1, "btn-icon-prepend", "hover-icon", "btn_icon"], ["placeholder", "Enter assets description", "formControlName", "assetDesc", 1, "form-control", 3, "keydown"], ["bindLabel", "criticalityOfAsset", "bindValue", "criticalityOfAsset", "formControlName", "criticalityOfAsset", "placeholder", "Select criticality of asset", 3, "items"], ["placeholder", "Enter internal IP address", "formControlName", "internalIP", 1, "form-control", 3, "keydown"], ["placeholder", "Enter public IP address", "formControlName", "publicIP", 1, "form-control", 3, "keydown"], ["placeholder", "Enter URL", "formControlName", "url", 1, "form-control", 3, "keydown"], ["placeholder", "Enter version", "formControlName", "version", 1, "form-control", 3, "keydown"], ["placeholder", "Enter out of scope", "formControlName", "outOfScopeDesc", 1, "form-control", 3, "keydown"]], template: function TestUpdatesComponent_Template(rf, ctx) {
  if (rf & 1) {
    const _r1 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 5)(1, "div", 6)(2, "div", 7)(3, "nav", 8)(4, "ol", 9)(5, "li", 10)(6, "a", 11);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_a_click_6_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.goBack());
    });
    i02.\u0275\u0275text(7, "Test");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(8, "li", 12);
    i02.\u0275\u0275text(9);
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275elementStart(10, "div", 13)(11, "form", 14);
    i02.\u0275\u0275listener("ngSubmit", function TestUpdatesComponent_Template_form_ngSubmit_11_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onSubmit());
    });
    i02.\u0275\u0275template(12, TestUpdatesComponent_div_12_Template, 4, 0, "div", 15)(13, TestUpdatesComponent_div_13_Template, 2, 1, "div", 16)(14, TestUpdatesComponent_div_14_Template, 2, 1, "div", 16)(15, TestUpdatesComponent_div_15_Template, 5, 0, "div", 17);
    i02.\u0275\u0275elementStart(16, "div", 18);
    i02.\u0275\u0275element(17, "input", 19);
    i02.\u0275\u0275elementStart(18, "label", 20);
    i02.\u0275\u0275text(19, "Active");
    i02.\u0275\u0275elementEnd()()()();
    i02.\u0275\u0275elementStart(20, "div", 21)(21, "button", 22);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_button_click_21_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.goBack());
    });
    i02.\u0275\u0275text(22, "Back");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(23, "button", 23);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_button_click_23_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onSubmit());
    });
    i02.\u0275\u0275text(24, "Submit");
    i02.\u0275\u0275elementEnd()()()()();
    i02.\u0275\u0275template(25, TestUpdatesComponent_div_25_Template, 9, 3, "div", 24);
    i02.\u0275\u0275elementStart(26, "div", 25)(27, "div", 26)(28, "div", 27)(29, "div", 28)(30, "form", 29)(31, "div", 30)(32, "label", 31);
    i02.\u0275\u0275text(33, "Project");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(34, "span", 32);
    i02.\u0275\u0275text(35, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(36, "ng-select", 33);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_Template_ng_select_change_36_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.getProjectSelect($event));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(37, TestUpdatesComponent_div_37_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(38, "div", 30)(39, "label", 35);
    i02.\u0275\u0275text(40, "Test");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(41, "ng-select", 36);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_Template_ng_select_change_41_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onTestChange($event));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(42, TestUpdatesComponent_div_42_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(43, "div", 30)(44, "label", 37);
    i02.\u0275\u0275text(45, "Test Title");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(46, "span", 32);
    i02.\u0275\u0275text(47, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(48, "input", 38);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_Template_input_keydown_48_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(49, TestUpdatesComponent_div_49_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(50, "div", 30)(51, "label", 39);
    i02.\u0275\u0275text(52, "Test Description");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(53, "span", 32);
    i02.\u0275\u0275text(54, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(55, "quill-editor", 40);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_Template_quill_editor_keydown_55_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(56, TestUpdatesComponent_div_56_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(57, "div", 30)(58, "label", 41);
    i02.\u0275\u0275text(59, "Actual Start Date");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(60, "div", 42)(61, "input", 43, 0);
    i02.\u0275\u0275listener("ngModelChange", function TestUpdatesComponent_Template_input_ngModelChange_61_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onChange($event, "startDate"));
    });
    i02.\u0275\u0275twoWayListener("ngModelChange", function TestUpdatesComponent_Template_input_ngModelChange_61_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.startDate, $event) || (ctx.startDate = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(63, "button", 44);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_button_click_63_listener() {
      i02.\u0275\u0275restoreView(_r1);
      const asd_r6 = i02.\u0275\u0275reference(62);
      return i02.\u0275\u0275resetView(asd_r6.toggle());
    });
    i02.\u0275\u0275element(64, "i", 45);
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275elementStart(65, "div", 30)(66, "label", 41);
    i02.\u0275\u0275text(67, "Actual End Date");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(68, "div", 42)(69, "input", 43, 1);
    i02.\u0275\u0275listener("ngModelChange", function TestUpdatesComponent_Template_input_ngModelChange_69_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onChange($event, "endDate"));
    });
    i02.\u0275\u0275twoWayListener("ngModelChange", function TestUpdatesComponent_Template_input_ngModelChange_69_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.endDate, $event) || (ctx.endDate = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(71, "button", 44);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_button_click_71_listener() {
      i02.\u0275\u0275restoreView(_r1);
      const esd_r7 = i02.\u0275\u0275reference(70);
      return i02.\u0275\u0275resetView(esd_r7.toggle());
    });
    i02.\u0275\u0275element(72, "i", 45);
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275elementStart(73, "div", 30)(74, "label", 41);
    i02.\u0275\u0275text(75, "Contact Person");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(76, "span", 32);
    i02.\u0275\u0275text(77, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(78, "input", 46);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_Template_input_keydown_78_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(79, TestUpdatesComponent_div_79_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(80, "div", 30)(81, "label", 41);
    i02.\u0275\u0275text(82, "Contact Number");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(83, "span", 32);
    i02.\u0275\u0275text(84, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(85, "input", 47);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_Template_input_keydown_85_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(86, TestUpdatesComponent_div_86_Template, 3, 2, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(87, "div", 30)(88, "label", 41);
    i02.\u0275\u0275text(89, "Email-ID");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(90, "span", 32);
    i02.\u0275\u0275text(91, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(92, "input", 48);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_Template_input_keydown_92_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(93, TestUpdatesComponent_div_93_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd()()()()();
    i02.\u0275\u0275elementStart(94, "div", 26)(95, "div", 27)(96, "div", 28)(97, "form", 29)(98, "div", 30)(99, "label", 49);
    i02.\u0275\u0275text(100, "Test Scope");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(101, "span", 32);
    i02.\u0275\u0275text(102, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(103, "ng-select", 50);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_Template_ng_select_change_103_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onTestScopeChange($event));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(104, TestUpdatesComponent_div_104_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(105, "div", 30)(106, "label", 51);
    i02.\u0275\u0275text(107, "Test Name");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(108, TestUpdatesComponent_span_108_Template, 2, 0, "span", 34);
    i02.\u0275\u0275elementStart(109, "ng-select", 52);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_Template_ng_select_change_109_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onTestNameChange($event));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(110, TestUpdatesComponent_div_110_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(111, "div", 30)(112, "label", 41);
    i02.\u0275\u0275text(113, "Test Status");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(114, "ng-select", 53);
    i02.\u0275\u0275template(115, TestUpdatesComponent_div_115_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(116, "div", 30)(117, "label", 37);
    i02.\u0275\u0275text(118, "Report Title");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(119, "span", 32);
    i02.\u0275\u0275text(120, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(121, "input", 54);
    i02.\u0275\u0275template(122, TestUpdatesComponent_div_122_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(123, "div", 30)(124, "label", 55);
    i02.\u0275\u0275text(125, "Scheduled Start Date");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(126, "span", 32);
    i02.\u0275\u0275text(127, "*");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(128, "div", 42)(129, "input", 56, 2);
    i02.\u0275\u0275listener("ngModelChange", function TestUpdatesComponent_Template_input_ngModelChange_129_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onChange($event, "assignDate"));
    });
    i02.\u0275\u0275twoWayListener("ngModelChange", function TestUpdatesComponent_Template_input_ngModelChange_129_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.assignDate, $event) || (ctx.assignDate = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(131, "button", 57);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_button_click_131_listener() {
      i02.\u0275\u0275restoreView(_r1);
      const ssd_r8 = i02.\u0275\u0275reference(130);
      return i02.\u0275\u0275resetView(ssd_r8.toggle());
    });
    i02.\u0275\u0275element(132, "i", 45);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275template(133, TestUpdatesComponent_div_133_Template, 3, 2, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(134, "div", 30)(135, "label", 41);
    i02.\u0275\u0275text(136, "Scheduled End Date");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(137, "span", 32);
    i02.\u0275\u0275text(138, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(139, "div", 42)(140, "input", 58, 3);
    i02.\u0275\u0275listener("ngModelChange", function TestUpdatesComponent_Template_input_ngModelChange_140_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onChange($event, "closureDate"));
    });
    i02.\u0275\u0275twoWayListener("ngModelChange", function TestUpdatesComponent_Template_input_ngModelChange_140_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.closureDate, $event) || (ctx.closureDate = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(142, "button", 57);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_button_click_142_listener() {
      i02.\u0275\u0275restoreView(_r1);
      const sed_r9 = i02.\u0275\u0275reference(141);
      return i02.\u0275\u0275resetView(sed_r9.toggle());
    });
    i02.\u0275\u0275element(143, "i", 45);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275template(144, TestUpdatesComponent_div_144_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(145, "div", 30)(146, "label", 59);
    i02.\u0275\u0275text(147, "Hours Allocated");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(148, "span", 32);
    i02.\u0275\u0275text(149, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(150, "input", 60);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_Template_input_keydown_150_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(151, TestUpdatesComponent_div_151_Template, 3, 2, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(152, "div", 30)(153, "label", 61);
    i02.\u0275\u0275text(154, "Hours Spent");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(155, "input", 62);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(156, "div", 30)(157, "label", 39);
    i02.\u0275\u0275text(158, "Credentials");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(159, "span", 32);
    i02.\u0275\u0275text(160, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(161, "textarea", 63);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_Template_textarea_keydown_161_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(162, TestUpdatesComponent_div_162_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(163, "div", 30)(164, "label", 64);
    i02.\u0275\u0275text(165, "Compliance Requirement");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(166, "div", 65)(167, "ng-multiselect-dropdown", 66, 4);
    i02.\u0275\u0275listener("onSelect", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onSelect_167_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onItemSelectCR($event));
    })("onDeSelect", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onDeSelect_167_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onDeSelectCR($event));
    })("onSelectAll", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onSelectAll_167_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onSelectAllCR($event));
    })("onDeSelectAll", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onDeSelectAll_167_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onDeSelectAllCR($event));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(169, "button", 67);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_button_click_169_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.toggleInputBox());
    });
    i02.\u0275\u0275element(170, "i", 68);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(171, "button", 69);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_button_click_171_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.complianceRequirementDelete());
    });
    i02.\u0275\u0275element(172, "i", 70);
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275template(173, TestUpdatesComponent_div_173_Template, 7, 3, "div", 71);
    i02.\u0275\u0275elementEnd()()()()();
    i02.\u0275\u0275elementStart(174, "div", 25)(175, "div", 72)(176, "div", 27)(177, "form", 73)(178, "div", 74)(179, "h6", 75);
    i02.\u0275\u0275text(180, " Engagement Scope ");
    i02.\u0275\u0275template(181, TestUpdatesComponent_span_181_Template, 2, 0, "span", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(182, TestUpdatesComponent_div_182_Template, 33, 3, "div", 76);
    i02.\u0275\u0275elementStart(183, "div", 77)(184, "button", 78);
    i02.\u0275\u0275listener("click", function TestUpdatesComponent_Template_button_click_184_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.addEngagement());
    });
    i02.\u0275\u0275text(185, " Add Engagement Scope ");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(186, TestUpdatesComponent_div_186_Template, 2, 0, "div", 34);
    i02.\u0275\u0275elementEnd()()()()()();
    i02.\u0275\u0275elementStart(187, "div", 25)(188, "div", 72)(189, "div", 27)(190, "div", 28)(191, "form", 73)(192, "div", 30)(193, "div", 79);
    i02.\u0275\u0275element(194, "input", 80);
    i02.\u0275\u0275elementStart(195, "label", 81);
    i02.\u0275\u0275text(196, " Out of Scope ");
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275template(197, TestUpdatesComponent_div_197_Template, 2, 0, "div", 71);
    i02.\u0275\u0275elementStart(198, "div", 82)(199, "div", 83)(200, "div")(201, "label", 84);
    i02.\u0275\u0275text(202, "Kick off document");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(203, "input", 85);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_Template_input_change_203_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onFileChange($event));
    });
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275elementStart(204, "div", 86)(205, "div", 87);
    i02.\u0275\u0275element(206, "input", 88);
    i02.\u0275\u0275text(207, " \xA0 \xA0 ");
    i02.\u0275\u0275elementStart(208, "label", 89);
    i02.\u0275\u0275text(209, "Zero Knowledge");
    i02.\u0275\u0275elementEnd()()()();
    i02.\u0275\u0275elementStart(210, "div", 30)(211, "label", 90);
    i02.\u0275\u0275text(212, "Assets page");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(213, "span", 32);
    i02.\u0275\u0275text(214, "*");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(215, "input", 91);
    i02.\u0275\u0275listener("keydown", function TestUpdatesComponent_Template_input_keydown_215_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(216, TestUpdatesComponent_div_216_Template, 3, 2, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(217, "div", 30)(218, "label", 64);
    i02.\u0275\u0275text(219, "Team Leader");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(220, "span", 32);
    i02.\u0275\u0275text(221, "*");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(222, "ng-select", 92);
    i02.\u0275\u0275listener("change", function TestUpdatesComponent_Template_ng_select_change_222_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.getTeamLeadSelect($event));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(223, TestUpdatesComponent_div_223_Template, 2, 1, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(224, "div", 30)(225, "label", 93);
    i02.\u0275\u0275text(226, "II Reviewer");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(227, "span", 32);
    i02.\u0275\u0275text(228, "*");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(229, "ng-multiselect-dropdown", 94, 4);
    i02.\u0275\u0275listener("onSelect", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onSelect_229_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onItemSelect($event, "assignedIIReviewers"));
    })("onDeSelect", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onDeSelect_229_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onDeSelect($event, "assignedIIReviewers"));
    })("onSelectAll", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onSelectAll_229_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onSelectAll($event, "assignedIIReviewers"));
    })("onDeSelectAll", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onDeSelectAll_229_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onDeSelectAll($event, "assignedIIReviewers"));
    });
    i02.\u0275\u0275twoWayListener("ngModelChange", function TestUpdatesComponent_Template_ng_multiselect_dropdown_ngModelChange_229_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.assignedIIReviewers, $event) || (ctx.assignedIIReviewers = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(231, TestUpdatesComponent_div_231_Template, 2, 0, "div", 34);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(232, "div", 30)(233, "label", 93);
    i02.\u0275\u0275text(234, "Assign Analyst");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(235, "span", 32);
    i02.\u0275\u0275text(236, "*");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(237, "ng-multiselect-dropdown", 95, 4);
    i02.\u0275\u0275listener("onSelect", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onSelect_237_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onItemSelect($event, "assignedAnalysts"));
    })("onDeSelect", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onDeSelect_237_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onDeSelect($event, "assignedAnalysts"));
    })("onSelectAll", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onSelectAll_237_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onSelectAll($event, "assignedAnalysts"));
    })("onDeSelectAll", function TestUpdatesComponent_Template_ng_multiselect_dropdown_onDeSelectAll_237_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onDeSelectAll($event, "assignedAnalysts"));
    });
    i02.\u0275\u0275twoWayListener("ngModelChange", function TestUpdatesComponent_Template_ng_multiselect_dropdown_ngModelChange_237_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.assignedAnalysts, $event) || (ctx.assignedAnalysts = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(239, TestUpdatesComponent_div_239_Template, 2, 0, "div", 34);
    i02.\u0275\u0275elementEnd()()()()()();
  }
  if (rf & 2) {
    let tmp_9_0;
    let tmp_12_0;
    let tmp_13_0;
    let tmp_17_0;
    let tmp_19_0;
    let tmp_21_0;
    let tmp_22_0;
    let tmp_24_0;
    let tmp_32_0;
    let tmp_34_0;
    let tmp_36_0;
    let tmp_40_0;
    let tmp_44_0;
    let tmp_48_0;
    let tmp_49_0;
    let tmp_52_0;
    let tmp_55_0;
    let tmp_57_0;
    let tmp_61_0;
    let tmp_72_0;
    let tmp_74_0;
    let tmp_75_0;
    let tmp_77_0;
    let tmp_80_0;
    i02.\u0275\u0275advance(9);
    i02.\u0275\u0275textInterpolate1(" ", (ctx.state == null ? null : ctx.state.testId) ? "Update Test " + ctx.testSeqId : "New Test", " ");
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("formGroup", ctx.testForm);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx.testForm == null ? null : (tmp_9_0 = ctx.testForm.get("isInProgress")) == null ? null : tmp_9_0.value);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx.canManageIReview);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx.canManageIIReview);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_12_0 = ctx.testForm.get("iReviewed")) == null ? null : tmp_12_0.value) && (ctx.testForm == null ? null : (tmp_12_0 = ctx.testForm.get("iiReviewed")) == null ? null : tmp_12_0.value));
    i02.\u0275\u0275advance(10);
    i02.\u0275\u0275property("ngIf", (ctx == null ? null : ctx.testId) && ((tmp_13_0 = ctx.testForm.get("createdBy")) == null ? null : tmp_13_0.value));
    i02.\u0275\u0275advance(5);
    i02.\u0275\u0275property("formGroup", ctx.testForm);
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("items", ctx.listOfProjects)("loading", ctx.isLoadingProject);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_17_0 = ctx.testForm.get("projectId")) == null ? null : tmp_17_0.dirty) && (ctx.testForm == null ? null : (tmp_17_0 = ctx.testForm.get("projectId")) == null ? null : tmp_17_0.errors) || (ctx.testForm == null ? null : (tmp_17_0 = ctx.testForm.get("projectId")) == null ? null : tmp_17_0.touched));
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("items", ctx.testList)("readonly", ((tmp_19_0 = ctx.testForm.get("testScopeId")) == null ? null : tmp_19_0.value) === "666192a1740fc56380d9f44c")("loading", ctx.isLoadingTest);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_21_0 = ctx.testForm.get("revalTestId")) == null ? null : tmp_21_0.dirty) && (ctx.testForm == null ? null : (tmp_21_0 = ctx.testForm.get("revalTestId")) == null ? null : tmp_21_0.errors) || (ctx.testForm == null ? null : (tmp_21_0 = ctx.testForm.get("revalTestId")) == null ? null : tmp_21_0.touched));
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_22_0 = ctx.testForm.get("testTitle")) == null ? null : tmp_22_0.dirty) && (ctx.testForm == null ? null : (tmp_22_0 = ctx.testForm.get("testTitle")) == null ? null : tmp_22_0.errors) || (ctx.testForm == null ? null : (tmp_22_0 = ctx.testForm.get("testTitle")) == null ? null : tmp_22_0.touched));
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("modules", ctx.preContentConfig);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_24_0 = ctx.testForm.get("testDesc")) == null ? null : tmp_24_0.dirty) && (ctx.testForm == null ? null : (tmp_24_0 = ctx.testForm.get("testDesc")) == null ? null : tmp_24_0.errors) || (ctx.testForm == null ? null : (tmp_24_0 = ctx.testForm.get("testDesc")) == null ? null : tmp_24_0.touched));
    i02.\u0275\u0275advance(5);
    i02.\u0275\u0275classProp("disabled", ctx.isDisabled);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.startDate);
    i02.\u0275\u0275property("ngModelOptions", i02.\u0275\u0275pureFunction0(90, _c02));
    i02.\u0275\u0275advance(8);
    i02.\u0275\u0275classProp("disabled", ctx.isDisabled);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.endDate);
    i02.\u0275\u0275property("ngModelOptions", i02.\u0275\u0275pureFunction0(91, _c02));
    i02.\u0275\u0275advance(9);
    i02.\u0275\u0275property("nzTooltipColor", ctx.color);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_32_0 = ctx.testForm.get("contactPerson")) == null ? null : tmp_32_0.dirty) && (ctx.testForm == null ? null : (tmp_32_0 = ctx.testForm.get("contactPerson")) == null ? null : tmp_32_0.errors) || (ctx.testForm == null ? null : (tmp_32_0 = ctx.testForm.get("contactPerson")) == null ? null : tmp_32_0.touched));
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("nzTooltipColor", ctx.color);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ((tmp_34_0 = ctx.testForm.get("contactNumber")) == null ? null : tmp_34_0.invalid) && (((tmp_34_0 = ctx.testForm.get("contactNumber")) == null ? null : tmp_34_0.touched) || ((tmp_34_0 = ctx.testForm.get("contactNumber")) == null ? null : tmp_34_0.dirty)));
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("nzTooltipColor", ctx.color);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_36_0 = ctx.testForm.get("emailId")) == null ? null : tmp_36_0.dirty) && (ctx.testForm == null ? null : (tmp_36_0 = ctx.testForm.get("emailId")) == null ? null : tmp_36_0.errors));
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("formGroup", ctx.testForm);
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("items", ctx.getTestScope)("loading", ctx.isLoading);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_40_0 = ctx.testForm.get("testScopeId")) == null ? null : tmp_40_0.dirty) && (ctx.testForm == null ? null : (tmp_40_0 = ctx.testForm.get("testScopeId")) == null ? null : tmp_40_0.errors) || (ctx.testForm == null ? null : (tmp_40_0 = ctx.testForm.get("testScopeId")) == null ? null : tmp_40_0.touched));
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("ngIf", ctx.testName.length > 0);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("items", ctx.testName)("loading", ctx.isLoading);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_44_0 = ctx.testForm.get("testNameId")) == null ? null : tmp_44_0.dirty) && (ctx.testForm == null ? null : (tmp_44_0 = ctx.testForm.get("testNameId")) == null ? null : tmp_44_0.errors) || (ctx.testForm == null ? null : (tmp_44_0 = ctx.testForm.get("testNameId")) == null ? null : tmp_44_0.touched));
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275classProp("disabled", ctx.isDisabled);
    i02.\u0275\u0275property("items", ctx.getTestStatus)("loading", ctx.isLoading);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_48_0 = ctx.testForm.get("testStatusId")) == null ? null : tmp_48_0.dirty) && (ctx.testForm == null ? null : (tmp_48_0 = ctx.testForm.get("testStatusId")) == null ? null : tmp_48_0.errors) || (ctx.testForm == null ? null : (tmp_48_0 = ctx.testForm.get("testStatusId")) == null ? null : tmp_48_0.touched));
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_49_0 = ctx.testForm.get("reportTitle")) == null ? null : tmp_49_0.dirty) && (ctx.testForm == null ? null : (tmp_49_0 = ctx.testForm.get("reportTitle")) == null ? null : tmp_49_0.errors) || (ctx.testForm == null ? null : (tmp_49_0 = ctx.testForm.get("reportTitle")) == null ? null : tmp_49_0.touched));
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.assignDate);
    i02.\u0275\u0275property("ngModelOptions", i02.\u0275\u0275pureFunction0(92, _c02));
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("ngIf", ((ctx.testForm == null ? null : (tmp_52_0 = ctx.testForm.get("assignDate")) == null ? null : tmp_52_0.dirty) || (ctx.testForm == null ? null : (tmp_52_0 = ctx.testForm.get("assignDate")) == null ? null : tmp_52_0.touched)) && ((ctx.testForm == null ? null : (tmp_52_0 = ctx.testForm.get("assignDate")) == null ? null : tmp_52_0.errors == null ? null : tmp_52_0.errors["required"]) || (ctx.testForm == null ? null : ctx.testForm.errors == null ? null : ctx.testForm.errors["assignDateGreaterThanClosureDate"])));
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.closureDate);
    i02.\u0275\u0275property("ngModelOptions", i02.\u0275\u0275pureFunction0(93, _c02));
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_55_0 = ctx.testForm.get("closureDate")) == null ? null : tmp_55_0.dirty) && (ctx.testForm == null ? null : (tmp_55_0 = ctx.testForm.get("closureDate")) == null ? null : tmp_55_0.errors) || (ctx.testForm == null ? null : (tmp_55_0 = ctx.testForm.get("closureDate")) == null ? null : tmp_55_0.touched));
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("nzTooltipColor", ctx.color);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_57_0 = ctx.testForm.get("hoursAllocated")) == null ? null : tmp_57_0.dirty) && (ctx.testForm == null ? null : (tmp_57_0 = ctx.testForm.get("hoursAllocated")) == null ? null : tmp_57_0.errors) || (ctx.testForm == null ? null : (tmp_57_0 = ctx.testForm.get("hoursAllocated")) == null ? null : tmp_57_0.touched));
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275classProp("disabled", ctx.isDisabled);
    i02.\u0275\u0275property("nzTooltipColor", ctx.color);
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("nzTooltipColor", ctx.color);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_61_0 = ctx.testForm.get("credential")) == null ? null : tmp_61_0.dirty) && (ctx.testForm == null ? null : (tmp_61_0 = ctx.testForm.get("credential")) == null ? null : tmp_61_0.errors) || (ctx.testForm == null ? null : (tmp_61_0 = ctx.testForm.get("credential")) == null ? null : tmp_61_0.touched));
    i02.\u0275\u0275advance(5);
    i02.\u0275\u0275property("data", ctx.complianceRequirementList)("settings", ctx.CRsettings)("disabled", false);
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("ngIf", ctx.showInputBox);
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("formGroup", ctx.testForm);
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("ngIf", ctx.engagementScope.controls.length);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngForOf", ctx.engagementScope.controls);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngClass", ctx.engagementScope.controls.length > 0 ? "" : "m_top");
    i02.\u0275\u0275advance(3);
    i02.\u0275\u0275property("ngIf", ctx.isEngagementScope);
    i02.\u0275\u0275advance(5);
    i02.\u0275\u0275property("formGroup", ctx.testForm);
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("ngIf", (tmp_72_0 = ctx.testForm.get("isOutOfScope")) == null ? null : tmp_72_0.value);
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("nzTooltipColor", ctx.color)("disabled", (tmp_74_0 = ctx.testForm.get("zeroKnowledge")) == null ? null : tmp_74_0.value);
    i02.\u0275\u0275attribute("readonly", ((tmp_75_0 = ctx.testForm.get("zeroKnowledge")) == null ? null : tmp_75_0.value) ? true : null);
    i02.\u0275\u0275advance(3);
    i02.\u0275\u0275property("nzTooltipColor", ctx.color);
    i02.\u0275\u0275advance(10);
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_77_0 = ctx.testForm.get("totalPages")) == null ? null : tmp_77_0.dirty) && (ctx.testForm == null ? null : (tmp_77_0 = ctx.testForm.get("totalPages")) == null ? null : tmp_77_0.errors) || (ctx.testForm == null ? null : (tmp_77_0 = ctx.testForm.get("totalPages")) == null ? null : tmp_77_0.touched));
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("items", ctx.teamLeadList)("loading", ctx.isLoadingTL);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx.testForm == null ? null : (tmp_80_0 = ctx.testForm.get("teamLeaderId")) == null ? null : tmp_80_0.dirty) && (ctx.testForm == null ? null : (tmp_80_0 = ctx.testForm.get("teamLeaderId")) == null ? null : tmp_80_0.errors) || (ctx.testForm == null ? null : (tmp_80_0 = ctx.testForm.get("teamLeaderId")) == null ? null : tmp_80_0.touched));
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("data", ctx.IIReviewerList)("settings", ctx.settingsReviewer)("disabled", false);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.assignedIIReviewers);
    i02.\u0275\u0275property("ngModelOptions", i02.\u0275\u0275pureFunction0(94, _c02));
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("ngIf", ctx.assignedIIReviewers.length === 0);
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("data", ctx.analystList)("settings", ctx.settingsAssignAnalyst)("disabled", false);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.assignedAnalysts);
    i02.\u0275\u0275property("ngModelOptions", i02.\u0275\u0275pureFunction0(95, _c02));
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("ngIf", ctx.assignedAnalysts.length === 0);
  }
}, dependencies: [i3.NgClass, i3.NgForOf, i3.NgIf, i4.\u0275NgNoValidate, i4.DefaultValueAccessor, i4.NumberValueAccessor, i4.CheckboxControlValueAccessor, i4.NgControlStatus, i4.NgControlStatusGroup, i4.MinValidator, i4.NgModel, i4.FormGroupDirective, i4.FormControlName, i4.FormGroupName, i4.FormArrayName, i8.\u0275NzTransitionPatchDirective, i92.NzTooltipDirective, i102.NgSelectComponent, FeatherIconDirective, i122.NgbInputDatepicker, i132.MultiSelectComponent, i142.QuillEditorComponent], styles: ['\n\n[_nghost-%COMP%]     .multiselect-dropdown .dropdown-btn {\n  border: var(--bs-border-width) solid #e9ecef !important;\n  color: #a9b3c7 !important;\n  min-height: 38px !important;\n}\n[_nghost-%COMP%]     .multiselect-dropdown .dropdown-btn .dropdown-multiselect__caret:before {\n  border-width: 5px 5px 0 6px !important;\n}\n[_nghost-%COMP%]     .multiselect-dropdown .dropdown-btn .selected-item-container .selected-item {\n  border: none !important;\n  background-color: #6571ff !important;\n  padding: 5px 8px !important;\n  max-width: 150px !important;\n}\n[_nghost-%COMP%]     .multiselect-dropdown .dropdown-list input:hover {\n  background-color: #cacef6;\n  color: #6571ff !important;\n  cursor: pointer !important;\n}\n[_nghost-%COMP%]     .multiselect-item-checkbox input[type=checkbox] + div:hover {\n  color: #6571ff !important;\n}\n[_nghost-%COMP%]     .multiselect-item-checkbox input[type=checkbox] + div:before {\n  width: 15px;\n  height: 15px;\n  border: var(--bs-border-width) solid #c4cad0 !important;\n  border-radius: 2px;\n}\n[_nghost-%COMP%]     .multiselect-item-checkbox input[type=checkbox]:checked + div:before {\n  background: #6571ff !important;\n  width: 15px;\n  height: 15px;\n  border: 2px solid #6571ff !important;\n}\n[_nghost-%COMP%]     .multiselect-item-checkbox input[type=checkbox]:checked + div {\n  color: #6571ff !important;\n  font-size: 14px !important;\n  font-weight: 600 !important;\n}\n  .ng-dropdown-panel .ng-dropdown-panel-items .ng-option, .ng-dropdown-panel[_ngcontent-%COMP%]   .ng-dropdown-panel-items[_ngcontent-%COMP%]   .ng-optgroup[_ngcontent-%COMP%] {\n  background-color: #fff;\n  color: var(--bs-body-color);\n}\n.ant-picker[_ngcontent-%COMP%]:hover, .ant-picker-focused[_ngcontent-%COMP%] {\n  border-color: #ced4da;\n  box-shadow: none !important;\n}\n[_nghost-%COMP%]     .ant-picker-input > input:focus, .ant-picker-input[_ngcontent-%COMP%]    > input-focused[_ngcontent-%COMP%] {\n  border-color: #ced4da;\n  box-shadow: 0 0 0 2px rgba(236, 238, 240, 0.2);\n  border-right-width: 1px;\n  outline: 0;\n}\n[_nghost-%COMP%]     .ant-picker-input > input:placeholder-shown {\n  font-size: 14px !important;\n}\n  .ng-dropdown-panel .ng-dropdown-panel-items .ng-option, .ng-dropdown-panel[_ngcontent-%COMP%]   .ng-dropdown-panel-items[_ngcontent-%COMP%]   .ng-optgroup[_ngcontent-%COMP%] {\n  background-color: #fff;\n  color: var(--bs-body-color);\n}\n.level[_ngcontent-%COMP%] {\n  margin-right: 6rem;\n}\n.disabled[_ngcontent-%COMP%] {\n  opacity: 0.5;\n  pointer-events: none;\n  background-color: #ddd;\n}\n.select-flex[_ngcontent-%COMP%] {\n  flex-grow: 1;\n  margin-right: 10px;\n}\n.float_none[_ngcontent-%COMP%] {\n  float: none;\n}\n  .ql-editor.ql-blank::before {\n  font-style: normal;\n  font-family:\n    "Roboto",\n    Helvetica,\n    sans-serif;\n  font-size: 14px;\n  color: #999;\n}\n  .dropdown-list li h5 {\n  font-style: normal;\n  font-family:\n    "Roboto",\n    Helvetica,\n    sans-serif;\n  font-size: 14px;\n  color: #999;\n  font-weight: 400;\n}\n  .ql-toolbar {\n  border-radius: 0.25rem 0.25rem 0 0 !important;\n}\n  .ql-container {\n  border-radius: 0 0 0.25rem 0.25rem !important;\n}\n.m_top[_ngcontent-%COMP%] {\n  margin-top: -3%;\n}\n@media (min-width: 1800px) {\n  .m_top[_ngcontent-%COMP%] {\n    margin-top: -2%;\n  }\n}\n.bg-purple[_ngcontent-%COMP%] {\n  background-color: rgb(185, 191, 255);\n}\n.btn_icon[_ngcontent-%COMP%]:hover {\n  transform: scale(1.2);\n}\n  .multiselect-dropdown .dropdown-btn .dropdown-multiselect__caret:before {\n  top: 60% !important;\n}\n/*# sourceMappingURL=test-updates.component.css.map */'] });
var TestUpdatesComponent = _TestUpdatesComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i02.\u0275setClassDebugInfo(TestUpdatesComponent, { className: "TestUpdatesComponent", filePath: "src/app/modules/test/test-updates/test-updates.component.ts", lineNumber: 24 });
})();

// src/app/modules/test/master-findings/master-findings.component.ts
import { Component as Component3 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i03 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i111 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i24 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";
import * as i32 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
import * as i52 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_table.js?v=ca23e844";
function MasterFindingsComponent_tr_31_Template(rf, ctx) {
  if (rf & 1) {
    const _r1 = i03.\u0275\u0275getCurrentView();
    i03.\u0275\u0275elementStart(0, "tr")(1, "td", 21);
    i03.\u0275\u0275text(2);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(3, "td", 22);
    i03.\u0275\u0275listener("click", function MasterFindingsComponent_tr_31_Template_td_click_3_listener() {
      const item_r2 = i03.\u0275\u0275restoreView(_r1).$implicit;
      const ctx_r2 = i03.\u0275\u0275nextContext();
      return i03.\u0275\u0275resetView(ctx_r2.goToFindingData(item_r2.titleKey, item_r2.testNameId, item_r2.testId, item_r2.testName));
    });
    i03.\u0275\u0275text(4);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(5, "td", 23);
    i03.\u0275\u0275text(6);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(7, "td", 24);
    i03.\u0275\u0275text(8);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(9, "td", 25);
    i03.\u0275\u0275text(10);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(11, "td", 26);
    i03.\u0275\u0275text(12);
    i03.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const item_r2 = ctx.$implicit;
    i03.\u0275\u0275advance(2);
    i03.\u0275\u0275textInterpolate(item_r2.testTitle);
    i03.\u0275\u0275advance(2);
    i03.\u0275\u0275textInterpolate(item_r2.findingTitle);
    i03.\u0275\u0275advance(2);
    i03.\u0275\u0275textInterpolate(item_r2.updatedOn);
    i03.\u0275\u0275advance(2);
    i03.\u0275\u0275textInterpolate(item_r2.updatedBy);
    i03.\u0275\u0275advance(2);
    i03.\u0275\u0275textInterpolate1("", item_r2.createdBy, " ");
    i03.\u0275\u0275advance(2);
    i03.\u0275\u0275textInterpolate1("", item_r2.findingDate, " ");
  }
}
var _MasterFindingsComponent = class _MasterFindingsComponent {
  constructor(router, toastr, location, testService) {
    this.router = router;
    this.toastr = toastr;
    this.location = location;
    this.testService = testService;
    this.listOfMasterData = [];
    this.loading = false;
    this.state = this.location.getState();
    this.testId = "";
  }
  ngOnInit() {
  }
  loadDataFromServer(pageIndex, pageSize, sortField, sortOrder, search) {
    this.loading = true;
    this.testService.GetTestMasterList(this.state?.testId).subscribe({
      next: (response) => {
        if (response.status === true) {
          const data = response.data;
          this.listOfMasterData = data;
          this.loading = false;
        }
      },
      error: (err) => {
        this.loading = false;
        return this.toastr.error(err.error.message, "Test Management");
      }
    });
  }
  onQueryParamsChange(params) {
    const { pageSize, pageIndex, sort, filter } = params;
    const currentSort = sort.find((item) => item.value !== null);
    const sortField = currentSort && currentSort.key || null;
    const sortOrder = currentSort && currentSort.value || null;
    const sortingData = { type: "sort", key: sortField, value: sortOrder };
    this.loadDataFromServer(pageIndex, pageSize, sortField, sortingData, filter);
  }
  goToFindingData(titleKey, testNameId, testId, testName) {
    if (titleKey.toLowerCase() == "es") {
      this.router.navigate(["/main/tests_management/executive_summary"], { state: { testId } });
    }
    if (titleKey.toLowerCase() == "fl") {
      this.router.navigate(["/main/finding_management/finding_list"], {
        state: { testId }
      });
    }
    if (titleKey.toLowerCase() == "cl") {
      this.router.navigate(["/main/checkList_management/test_checklist"], {
        state: { testNameId, testId, testName }
      });
    }
    if (titleKey.toLowerCase() == "wq") {
      this.router.navigate(["/main/walkThrough_management/test_walkThrough"], {
        state: { testNameId, testId, testName }
      });
    }
    if (titleKey.toLowerCase() == "bl") {
      this.router.navigate(["/main/businessLogic_management/test_business"], {
        state: { testId }
      });
    }
    if (titleKey.toLowerCase() == "rl") {
      this.router.navigate(["/main/resources_management/resources_test"], {
        state: { testNameId, testId, testName }
      });
    }
  }
};
_MasterFindingsComponent.\u0275fac = function MasterFindingsComponent_Factory(t) {
  return new (t || _MasterFindingsComponent)(i03.\u0275\u0275directiveInject(i111.Router), i03.\u0275\u0275directiveInject(i24.ToastrService), i03.\u0275\u0275directiveInject(i32.Location), i03.\u0275\u0275directiveInject(TestService));
};
_MasterFindingsComponent.\u0275cmp = /* @__PURE__ */ i03.\u0275\u0275defineComponent({ type: _MasterFindingsComponent, selectors: [["app-master-findings"]], decls: 32, vars: 4, consts: [[1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "page-breadcrumb", "m-0"], [1, "breadcrumb", "mb-0"], [1, "breadcrumb-item"], ["routerLink", "/main/tests_management/test_list"], ["aria-current", "page", 1, "breadcrumb-item", "active"], [1, "row"], [1, "col-md-12", "stretch-card"], [1, "card"], [1, "card-body"], [1, "table-container", "dataTable"], ["nzShowSizeChanger", "", 3, "nzQueryParams", "nzData", "nzShowPagination", "nzLoading"], ["id", "1", "nzColumnKey", "projectName"], ["id", "2", "nzColumnKey", "nwPlacementName"], ["id", "1", "nzColumnKey", "orgName"], ["id", "5"], ["id", "6"], ["id", "57"], [4, "ngFor", "ngForOf"], ["nzCellControl", "testTitle"], [3, "click"], ["nzCellControl", "lastEdited"], ["nzCellControl", "lastEditedBy"], ["nzCellControl", "createdBy"], ["nzCellControl", "findingDate"]], template: function MasterFindingsComponent_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 0)(1, "div", 1)(2, "div", 2)(3, "nav", 3)(4, "ol", 4)(5, "li", 5)(6, "a", 6);
    i03.\u0275\u0275text(7, "Test Management");
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275elementStart(8, "li", 7);
    i03.\u0275\u0275text(9, "Test Masters");
    i03.\u0275\u0275elementEnd()()()()()();
    i03.\u0275\u0275elementStart(10, "div", 8)(11, "div", 9)(12, "div", 10)(13, "div", 11)(14, "div", 12)(15, "nz-table", 13);
    i03.\u0275\u0275listener("nzQueryParams", function MasterFindingsComponent_Template_nz_table_nzQueryParams_15_listener($event) {
      return ctx.onQueryParamsChange($event);
    });
    i03.\u0275\u0275elementStart(16, "thead")(17, "tr")(18, "th", 14);
    i03.\u0275\u0275text(19, " Test ");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(20, "th", 15);
    i03.\u0275\u0275text(21, " Finding Title ");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(22, "th", 16);
    i03.\u0275\u0275text(23, " last edited ");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(24, "th", 17);
    i03.\u0275\u0275text(25, "last edited by");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(26, "th", 18);
    i03.\u0275\u0275text(27, "First Created by");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(28, "th", 19);
    i03.\u0275\u0275text(29, "Finding Date");
    i03.\u0275\u0275elementEnd()()();
    i03.\u0275\u0275elementStart(30, "tbody");
    i03.\u0275\u0275template(31, MasterFindingsComponent_tr_31_Template, 13, 6, "tr", 20);
    i03.\u0275\u0275elementEnd()()()()()()();
  }
  if (rf & 2) {
    i03.\u0275\u0275advance(15);
    i03.\u0275\u0275property("nzData", ctx.listOfMasterData)("nzShowPagination", false)("nzLoading", ctx.loading);
    i03.\u0275\u0275advance(16);
    i03.\u0275\u0275property("ngForOf", ctx.listOfMasterData);
  }
}, dependencies: [i32.NgForOf, i111.RouterLink, i52.NzTableComponent, i52.NzThAddOnComponent, i52.NzTableCellDirective, i52.NzThMeasureDirective, i52.NzTheadComponent, i52.NzTbodyComponent, i52.NzTrDirective, i52.NzCustomColumnDirective] });
var MasterFindingsComponent = _MasterFindingsComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i03.\u0275setClassDebugInfo(MasterFindingsComponent, { className: "MasterFindingsComponent", filePath: "src/app/modules/test/master-findings/master-findings.component.ts", lineNumber: 12 });
})();

// src/app/modules/test/executive-summary/executive-summary.component.ts
import { Component as Component4, ViewChild as ViewChild2 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { Validators as Validators2 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import Chart from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/chart__js_auto.js?v=ca23e844";
import * as i04 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i112 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i25 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
import * as i42 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";
import * as i72 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i93 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-quill.js?v=ca23e844";
var _c03 = ["chartBarCanvas"];
var _c12 = ["chartPieCanvas"];
var _c22 = () => ({ standalone: true });
function ExecutiveSummaryComponent_div_15_Template(rf, ctx) {
  if (rf & 1) {
    const _r2 = i04.\u0275\u0275getCurrentView();
    i04.\u0275\u0275elementStart(0, "div", 53)(1, "input", 54);
    i04.\u0275\u0275listener("change", function ExecutiveSummaryComponent_div_15_Template_input_change_1_listener() {
      i04.\u0275\u0275restoreView(_r2);
      const ctx_r2 = i04.\u0275\u0275nextContext();
      return i04.\u0275\u0275resetView(ctx_r2.onReviewChange("isInProgress", true));
    });
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(2, "label", 55);
    i04.\u0275\u0275text(3, " In Progress ");
    i04.\u0275\u0275elementEnd()();
  }
}
function ExecutiveSummaryComponent_div_16_div_1_Template(rf, ctx) {
  if (rf & 1) {
    const _r4 = i04.\u0275\u0275getCurrentView();
    i04.\u0275\u0275elementStart(0, "div")(1, "div", 53)(2, "label", 56);
    i04.\u0275\u0275text(3, "I Review ");
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(4, "div", 53)(5, "input", 57);
    i04.\u0275\u0275listener("change", function ExecutiveSummaryComponent_div_16_div_1_Template_input_change_5_listener() {
      i04.\u0275\u0275restoreView(_r4);
      const ctx_r2 = i04.\u0275\u0275nextContext(2);
      return i04.\u0275\u0275resetView(ctx_r2.onReviewChange("iReviewed", true));
    });
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(6, "label", 58);
    i04.\u0275\u0275text(7, "Pass ");
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(8, "div", 53)(9, "input", 59);
    i04.\u0275\u0275listener("change", function ExecutiveSummaryComponent_div_16_div_1_Template_input_change_9_listener() {
      i04.\u0275\u0275restoreView(_r4);
      const ctx_r2 = i04.\u0275\u0275nextContext(2);
      return i04.\u0275\u0275resetView(ctx_r2.onReviewChange("iReviewed", false));
    });
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(10, "label", 60);
    i04.\u0275\u0275text(11, "Fail");
    i04.\u0275\u0275elementEnd()()();
  }
}
function ExecutiveSummaryComponent_div_16_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275elementStart(0, "div");
    i04.\u0275\u0275template(1, ExecutiveSummaryComponent_div_16_div_1_Template, 12, 0, "div", 14);
    i04.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_3_0;
    const ctx_r2 = i04.\u0275\u0275nextContext();
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", !((tmp_3_0 = ctx_r2.executiveSummaryForm.get("isInProgress")) == null ? null : tmp_3_0.value) && !((tmp_3_0 = ctx_r2.executiveSummaryForm.get("iReviewed")) == null ? null : tmp_3_0.value));
  }
}
function ExecutiveSummaryComponent_div_17_div_1_Template(rf, ctx) {
  if (rf & 1) {
    const _r5 = i04.\u0275\u0275getCurrentView();
    i04.\u0275\u0275elementStart(0, "div")(1, "div", 53)(2, "label", 61);
    i04.\u0275\u0275text(3, "II Review ");
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(4, "div", 53)(5, "input", 62);
    i04.\u0275\u0275listener("change", function ExecutiveSummaryComponent_div_17_div_1_Template_input_change_5_listener() {
      i04.\u0275\u0275restoreView(_r5);
      const ctx_r2 = i04.\u0275\u0275nextContext(2);
      return i04.\u0275\u0275resetView(ctx_r2.onReviewChange("iiReviewed", true));
    });
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(6, "label", 63);
    i04.\u0275\u0275text(7, "Pass ");
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(8, "div", 53)(9, "input", 64);
    i04.\u0275\u0275listener("change", function ExecutiveSummaryComponent_div_17_div_1_Template_input_change_9_listener() {
      i04.\u0275\u0275restoreView(_r5);
      const ctx_r2 = i04.\u0275\u0275nextContext(2);
      return i04.\u0275\u0275resetView(ctx_r2.onReviewChange("iiReviewed", false));
    });
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(10, "label", 65);
    i04.\u0275\u0275text(11, "Fail");
    i04.\u0275\u0275elementEnd()()();
  }
}
function ExecutiveSummaryComponent_div_17_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275elementStart(0, "div");
    i04.\u0275\u0275template(1, ExecutiveSummaryComponent_div_17_div_1_Template, 12, 0, "div", 14);
    i04.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_3_0;
    const ctx_r2 = i04.\u0275\u0275nextContext();
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", ((tmp_3_0 = ctx_r2.executiveSummaryForm.get("iReviewed")) == null ? null : tmp_3_0.value) && !((tmp_3_0 = ctx_r2.executiveSummaryForm.get("iiReviewed")) == null ? null : tmp_3_0.value));
  }
}
function ExecutiveSummaryComponent_span_30_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275elementStart(0, "span");
    i04.\u0275\u0275text(1);
    i04.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_3_0;
    const ctx_r2 = i04.\u0275\u0275nextContext();
    i04.\u0275\u0275advance();
    i04.\u0275\u0275textInterpolate1(" [ First Created by ", (tmp_3_0 = ctx_r2.executiveSummaryForm.get("createdBy")) == null ? null : tmp_3_0.value, " ] ");
  }
}
function ExecutiveSummaryComponent_span_31_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275elementStart(0, "span");
    i04.\u0275\u0275text(1);
    i04.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_3_0;
    const ctx_r2 = i04.\u0275\u0275nextContext();
    i04.\u0275\u0275advance();
    i04.\u0275\u0275textInterpolate1(" [ I Reviewed by ", (tmp_3_0 = ctx_r2.executiveSummaryForm.get("iReviewedBy")) == null ? null : tmp_3_0.value, " ] ");
  }
}
function ExecutiveSummaryComponent_span_32_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275elementStart(0, "span");
    i04.\u0275\u0275text(1);
    i04.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_3_0;
    const ctx_r2 = i04.\u0275\u0275nextContext();
    i04.\u0275\u0275advance();
    i04.\u0275\u0275textInterpolate1(" [ II Reviewed by ", (tmp_3_0 = ctx_r2.executiveSummaryForm.get("iiReviewedBy")) == null ? null : tmp_3_0.value, " ] ");
  }
}
function ExecutiveSummaryComponent_div_44_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275elementStart(0, "div");
    i04.\u0275\u0275text(1, " Please enter test introduction! ");
    i04.\u0275\u0275elementEnd();
  }
}
function ExecutiveSummaryComponent_div_44_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275elementStart(0, "div", 27);
    i04.\u0275\u0275template(1, ExecutiveSummaryComponent_div_44_div_1_Template, 2, 0, "div", 14);
    i04.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_3_0;
    const ctx_r2 = i04.\u0275\u0275nextContext();
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", ctx_r2.executiveSummaryForm == null ? null : (tmp_3_0 = ctx_r2.executiveSummaryForm.get("testIntroduction")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["required"]);
  }
}
function ExecutiveSummaryComponent_div_49_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275elementStart(0, "div");
    i04.\u0275\u0275text(1, " Please enter executive summary ");
    i04.\u0275\u0275elementEnd();
  }
}
function ExecutiveSummaryComponent_div_49_Template(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275elementStart(0, "div", 27);
    i04.\u0275\u0275template(1, ExecutiveSummaryComponent_div_49_div_1_Template, 2, 0, "div", 14);
    i04.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_3_0;
    const ctx_r2 = i04.\u0275\u0275nextContext();
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", ctx_r2.executiveSummaryForm == null ? null : (tmp_3_0 = ctx_r2.executiveSummaryForm.get("executiveSummaryDesc")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["required"]);
  }
}
function ExecutiveSummaryComponent_div_95_Template(rf, ctx) {
  if (rf & 1) {
    const _r6 = i04.\u0275\u0275getCurrentView();
    i04.\u0275\u0275elementStart(0, "div", 66)(1, "div", 67)(2, "div", 68)(3, "div");
    i04.\u0275\u0275text(4);
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(5, "div", 45)(6, "span", 69);
    i04.\u0275\u0275listener("click", function ExecutiveSummaryComponent_div_95_Template_span_click_6_listener() {
      const i_r7 = i04.\u0275\u0275restoreView(_r6).index;
      const ctx_r2 = i04.\u0275\u0275nextContext();
      return i04.\u0275\u0275resetView(ctx_r2.getDown(i_r7));
    });
    i04.\u0275\u0275element(7, "i", 70);
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(8, "span", 69);
    i04.\u0275\u0275listener("click", function ExecutiveSummaryComponent_div_95_Template_span_click_8_listener() {
      const i_r7 = i04.\u0275\u0275restoreView(_r6).index;
      const ctx_r2 = i04.\u0275\u0275nextContext();
      return i04.\u0275\u0275resetView(ctx_r2.getUp(i_r7));
    });
    i04.\u0275\u0275element(9, "i", 71);
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(10, "div")(11, "div", 53);
    i04.\u0275\u0275element(12, "input", 72);
    i04.\u0275\u0275elementStart(13, "label", 73);
    i04.\u0275\u0275text(14, " Show/Hide ");
    i04.\u0275\u0275elementEnd()()()()();
    i04.\u0275\u0275elementStart(15, "div")(16, "div", 22)(17, "label", 74);
    i04.\u0275\u0275text(18, "Key Issue");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(19, "quill-editor", 75);
    i04.\u0275\u0275listener("keydown", function ExecutiveSummaryComponent_div_95_Template_quill_editor_keydown_19_listener() {
      i04.\u0275\u0275restoreView(_r6);
      const ctx_r2 = i04.\u0275\u0275nextContext();
      return i04.\u0275\u0275resetView(ctx_r2.onKeyPressInputChange(true));
    });
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(20, "div", 22)(21, "label", 74);
    i04.\u0275\u0275text(22, "Impact Summary");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(23, "quill-editor", 76);
    i04.\u0275\u0275listener("keydown", function ExecutiveSummaryComponent_div_95_Template_quill_editor_keydown_23_listener() {
      i04.\u0275\u0275restoreView(_r6);
      const ctx_r2 = i04.\u0275\u0275nextContext();
      return i04.\u0275\u0275resetView(ctx_r2.onKeyPressInputChange(true));
    });
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(24, "div", 22)(25, "label", 74);
    i04.\u0275\u0275text(26, "Remediation");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(27, "quill-editor", 77);
    i04.\u0275\u0275listener("keydown", function ExecutiveSummaryComponent_div_95_Template_quill_editor_keydown_27_listener() {
      i04.\u0275\u0275restoreView(_r6);
      const ctx_r2 = i04.\u0275\u0275nextContext();
      return i04.\u0275\u0275resetView(ctx_r2.onKeyPressInputChange(true));
    });
    i04.\u0275\u0275elementEnd()()()();
  }
  if (rf & 2) {
    let tmp_6_0;
    let tmp_12_0;
    let tmp_13_0;
    let tmp_17_0;
    let tmp_18_0;
    let tmp_22_0;
    let tmp_23_0;
    const finding_r8 = ctx.$implicit;
    const i_r7 = ctx.index;
    const ctx_r2 = i04.\u0275\u0275nextContext();
    i04.\u0275\u0275property("formGroupName", i_r7);
    i04.\u0275\u0275advance(4);
    i04.\u0275\u0275textInterpolate3("Finding ID ", (tmp_6_0 = finding_r8.get("findingSeqId")) == null ? null : tmp_6_0.value, " Severity ", (tmp_6_0 = finding_r8.get("cvssSeverity")) == null ? null : tmp_6_0.value, " (CVSS ", (tmp_6_0 = finding_r8.get("cvssScore")) == null ? null : tmp_6_0.value, ") ");
    i04.\u0275\u0275advance(8);
    i04.\u0275\u0275propertyInterpolate1("id", "showFinding", i_r7, "");
    i04.\u0275\u0275advance();
    i04.\u0275\u0275propertyInterpolate1("for", "showFinding", i_r7, "");
    i04.\u0275\u0275advance(4);
    i04.\u0275\u0275propertyInterpolate1("for", "keyIssuesDetail", i_r7, "");
    i04.\u0275\u0275advance(2);
    i04.\u0275\u0275propertyInterpolate1("id", "keyIssuesDetail", i_r7, "");
    i04.\u0275\u0275property("modules", ctx_r2.preContentConfig)("readOnly", !((tmp_12_0 = finding_r8.get("isHidden")) == null ? null : tmp_12_0.value))("ngClass", !((tmp_13_0 = finding_r8.get("isHidden")) == null ? null : tmp_13_0.value) ? "disabled" : "");
    i04.\u0275\u0275advance(2);
    i04.\u0275\u0275propertyInterpolate1("for", "impactSummary", i_r7, "");
    i04.\u0275\u0275advance(2);
    i04.\u0275\u0275propertyInterpolate1("id", "impactSummary", i_r7, "");
    i04.\u0275\u0275property("modules", ctx_r2.preContentConfig)("readOnly", !((tmp_17_0 = finding_r8.get("isHidden")) == null ? null : tmp_17_0.value))("ngClass", !((tmp_18_0 = finding_r8.get("isHidden")) == null ? null : tmp_18_0.value) ? "disabled" : "");
    i04.\u0275\u0275advance(2);
    i04.\u0275\u0275propertyInterpolate1("for", "remediation", i_r7, "");
    i04.\u0275\u0275advance(2);
    i04.\u0275\u0275propertyInterpolate1("id", "remediation", i_r7, "");
    i04.\u0275\u0275property("modules", ctx_r2.preContentConfig)("readOnly", !((tmp_22_0 = finding_r8.get("isHidden")) == null ? null : tmp_22_0.value))("ngClass", !((tmp_23_0 = finding_r8.get("isHidden")) == null ? null : tmp_23_0.value) ? "disabled" : "");
  }
}
var _ExecutiveSummaryComponent = class _ExecutiveSummaryComponent {
  constructor(fb, location, testService, toastr, loaderService, commonService) {
    this.fb = fb;
    this.location = location;
    this.testService = testService;
    this.toastr = toastr;
    this.loaderService = loaderService;
    this.commonService = commonService;
    this.state = this.location.getState();
    this.testId = "";
    this.preContentConfig = {
      toolbar: {
        container: [
          ["bold", "italic", "underline", "link", "image"]
        ]
      }
    };
    this.hasUnsavedChanges = false;
    this.isAllShow = false;
    this.canManageIReview = false;
    this.canManageIIReview = false;
  }
  ngOnInit() {
    this.testId = this.state.testId;
    this.initializeForm();
    const fetchData = this.commonService.getItem("executiveSummaryForm");
    if (fetchData) {
      this.executiveSummaryForm.patchValue(fetchData);
    }
  }
  permissionForReview(testId) {
    this.loaderService.show();
    this.testService.PermissionForReview(testId).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.canManageIReview = response.data?.canManageIReview;
          this.canManageIIReview = response.data?.canManageIIReview;
          this.loaderService.hide();
        }
      },
      error: (err) => {
        return this.loaderService.hide();
      }
    });
  }
  onKeyPressInputChange(hasUnsavedChanges) {
    this.hasUnsavedChanges = hasUnsavedChanges;
  }
  initializeForm() {
    this.executiveSummaryForm = this.fb.group({
      _id: [""],
      testId: [""],
      findingSeqId: [""],
      findingTitle: [""],
      testTitle: [""],
      testIntroduction: ["", [Validators2.required]],
      executiveSummaryDesc: [
        `A high-level overview of the key audit findings and vulnerabilities.This section is for senior management to understand business risks.`,
        [Validators2.required]
      ],
      criticality: [""],
      businessImplication: [""],
      managementRecommendations: [""],
      findings: this.fb.array([]),
      isInProgress: [true],
      isInProgressPass: [true],
      isInProgressFail: [false],
      iReviewedPass: [false],
      iReviewedFail: [false],
      iiReviewedPass: [false],
      iiReviewedFail: [false],
      createdBy: [""],
      iReviewedBy: [""],
      iiReviewedBy: [""],
      iReviewed: [false],
      iiReviewed: [false]
    });
    this.getExecutiveDetails(this.testId);
  }
  get findings() {
    return this.executiveSummaryForm.get("findings");
  }
  getExecutiveDetails(testId) {
    this.loaderService.show();
    this.testService.GetExecutiveData(testId).subscribe({
      next: (response) => __async(this, null, function* () {
        if (response.status === true) {
          const data = response.data;
          this.vulnerability = data[0]?.vulnerability || null;
          this.impact = data[0]?.impact;
          this.executiveSummaryForm.patchValue(data[0]?.executiveSummary);
          this.executiveSummaryForm.get("isInProgressPass")?.setValue(data[0]?.executiveSummary.isInProgress);
          const findingsArray = this.findings;
          const findings = data[0]?.findings || [];
          findings.sort((a, b) => a.keyIssuesAndRemediation?.orderId - b.keyIssuesAndRemediation?.orderId);
          yield findings.forEach((finding) => {
            if (finding.isHidden) {
              this.isAllShow = true;
            }
            findingsArray.push(this.fb.group({
              _id: [finding._id],
              testId: [finding.testId],
              findingTitle: [finding.findingTitle],
              cvssScore: [finding.cvssScore],
              cvssSeverity: [finding.cvssSeverity],
              findingSeqId: [finding.findingSeqId],
              impactSummary: [finding.keyIssuesAndRemediation.impactSummary],
              isHidden: [finding.keyIssuesAndRemediation.isHidden],
              keyIssuesDetail: [finding.keyIssuesAndRemediation?.keyIssuesDetail || ""],
              remediation: [finding.keyIssuesAndRemediation?.remediation || ""],
              orderId: [finding.keyIssuesAndRemediation?.orderId || 1]
            }));
          });
          this.permissionForReview(testId);
          yield this.BarChartDisplay();
          yield this.PieChartDisplay();
          this.loaderService.hide();
        }
      }),
      error: (err) => {
        this.loaderService.hide();
        return;
      }
    });
  }
  transformResponse(response) {
    const executiveSummary = {
      findingId: response._id,
      testId: response.testId,
      findingTitle: response.findingTitle,
      testIntroduction: response.testIntroduction,
      executiveSummaryDesc: response.executiveSummaryDesc,
      managementRecommendations: response.managementRecommendations,
      criticality: response.criticality,
      businessImplication: response.businessImplication,
      isInProgress: response.isInProgress,
      iReviewed: response.iReviewed ?? false,
      iiReviewed: response.iiReviewed ?? false
    };
    const findings = response.findings.map((finding) => {
      const keyIssuesAndRemediation = finding.keyIssuesDetail ? {
        keyIssuesDetail: finding.keyIssuesDetail || "",
        remediation: finding.remediation || "",
        orderId: finding.orderId,
        isHidden: finding.isHidden || false,
        impactSummary: finding.impactSummary || ""
      } : null;
      return {
        findingSeqId: finding.findingSeqId.toString(),
        findingId: finding._id,
        keyIssuesAndRemediation
      };
    });
    return {
      executiveSummary,
      findings
    };
  }
  onReviewChange(reviewType, isPass) {
    if (reviewType === "iReviewed") {
      if (isPass) {
        this.executiveSummaryForm.get("iReviewedFail")?.setValue(false);
      } else {
        this.executiveSummaryForm.get("iReviewedPass")?.setValue(false);
      }
    } else if (reviewType === "iiReviewed") {
      if (isPass) {
        this.executiveSummaryForm.get("iiReviewedFail")?.setValue(false);
      } else {
        this.executiveSummaryForm.get("iiReviewedPass")?.setValue(false);
      }
    } else if (reviewType === "isInProgress") {
      if (isPass) {
        this.executiveSummaryForm.get("isInProgressFail")?.setValue(false);
      } else {
        this.executiveSummaryForm.get("isInProgressPass")?.setValue(false);
      }
    }
  }
  allShowHide(event) {
    const isChecked = event;
    this.findings.controls.forEach((control) => {
      const finding = control;
      finding.get("isHidden")?.setValue(isChecked);
    });
  }
  removePTags(str) {
    if (typeof str === "string") {
      return str.replace(/<\/?p>/g, "");
    }
    return str;
  }
  onSubmit() {
    return __async(this, null, function* () {
      let hasErrors = false;
      if (this.executiveSummaryForm.valid) {
        const formValues = this.executiveSummaryForm.value;
        if (formValues.isInProgressPass) {
          this.executiveSummaryForm.get("isInProgress")?.setValue(true);
        } else {
          this.executiveSummaryForm.get("isInProgress")?.setValue(false);
        }
        if (formValues.iReviewedPass) {
          this.executiveSummaryForm.get("iReviewed")?.setValue(true);
        } else if (formValues.iReviewedFail) {
          this.executiveSummaryForm.get("iReviewed")?.setValue(false);
          this.executiveSummaryForm.get("isInProgress")?.setValue(true);
        }
        if (formValues.iiReviewedPass) {
          this.executiveSummaryForm.get("iiReviewed")?.setValue(true);
        } else if (formValues.iiReviewedFail) {
          this.executiveSummaryForm.get("iiReviewed")?.setValue(false);
          this.executiveSummaryForm.get("iReviewed")?.setValue(false);
        }
        const response = __spreadProps(__spreadValues({
          _id: this.executiveSummaryForm.value.findingId
        }, formValues), {
          isInProgress: this.hasUnsavedChanges ? true : this.executiveSummaryForm.value.isInProgress,
          iReviewed: this.hasUnsavedChanges ? false : this.executiveSummaryForm.value.iReviewed,
          iiReviewed: this.hasUnsavedChanges ? false : this.executiveSummaryForm.value.iiReviewed
        });
        const payload = this.transformResponse(response);
        this.loaderService.show();
        this.testService.editExecutiveData(payload).subscribe({
          next: (response2) => {
            if (response2.status === true) {
              this.toastr.success(response2.message, "Executive Management");
              this.hasUnsavedChanges = false;
              this.reloadData();
              this.loaderService.hide();
            }
          },
          error: (err) => {
            this.loaderService.hide();
            this.toastr.error(err.error.message, "Executive Management");
          }
        });
      } else {
        Object.values(this.executiveSummaryForm.controls).forEach((control) => {
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
    });
  }
  BarChartDisplay() {
    return __async(this, null, function* () {
      const ctx = this.chartBarCanvasRef.nativeElement.getContext("2d");
      const data = {
        labels: ["Critical", "High", "Medium", "Low", "Info"],
        datasets: [{
          label: "Severity based Vulnerability Distribution",
          data: [
            this.vulnerability?.critical != null && this.vulnerability.critical !== 0 ? this.vulnerability.critical : 0.1,
            this.vulnerability?.high != null && this.vulnerability.high !== 0 ? this.vulnerability.high : 0.1,
            this.vulnerability?.medium != null && this.vulnerability.medium !== 0 ? this.vulnerability.medium : 0.1,
            this.vulnerability?.low != null && this.vulnerability.low !== 0 ? this.vulnerability.low : 0.1,
            this.vulnerability?.info != null && this.vulnerability.info !== 0 ? this.vulnerability.info : 0.1
          ],
          backgroundColor: [
            "rgb(255,0,0)",
            "rgb(255,69,0)",
            "rgb(255, 206, 86)",
            "rgb(0,128,0)",
            "rgb(32,178,170)"
          ]
        }]
      };
      const options = {
        plugins: {
          legend: {
            display: true,
            // Ensure the legend is displayed
            labels: {
              usePointStyle: true,
              // Use point style to hide the color box
              boxWidth: 0,
              // Set box width to 0 to hide the color box
              font: {
                size: 12,
                // Adjust the font size as needed
                weight: 700
                // Make the font bold
              }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            min: 0,
            // Set the minimum value for the y-axis
            max: 10
            // Set the maximum value for the y-axis (adjust as needed)
          }
        }
      };
      this.chartInstanceBar = new Chart(ctx, {
        type: "bar",
        data,
        options
      });
    });
  }
  PieChartDisplay() {
    return __async(this, null, function* () {
      const ctx = this.chartPieCanvasRef.nativeElement.getContext("2d");
      const xValues = ["Critical", "High", "Medium", "Low"];
      const yValues = [this.impact?.critical, this.impact?.high, this.impact?.medium, this.impact?.low ?? 1];
      const barColors = [
        "rgb(255,0,0)",
        "rgb(255,69,0)",
        "rgb(255, 206, 86)",
        "rgb(0,128,0)"
      ];
      this.chartInstancePie = new Chart(ctx, {
        type: "pie",
        data: {
          labels: xValues,
          datasets: [{
            backgroundColor: barColors,
            data: yValues
          }]
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: "Impact to security posture"
            }
          }
        }
      });
    });
  }
  goBack() {
    this.location.back();
  }
  saveTemporaryData() {
    this.commonService.setItem("executiveSummaryForm", this.executiveSummaryForm.value);
    this.toastr.info("Temporary data saved", "Executive Management");
  }
  reloadData() {
    this.destroyChart();
    this.executiveSummaryForm.reset();
    this.findings.clear();
    this.getExecutiveDetails(this.testId);
  }
  destroyChart() {
    if (this.chartInstanceBar) {
      this.chartInstanceBar.destroy();
      this.chartInstanceBar = null;
    }
    if (this.chartInstancePie) {
      this.chartInstancePie.destroy();
      this.chartInstancePie = null;
    }
  }
  getDown(index) {
    if (index < this.findings.length - 1) {
      const step = this.findings.at(index);
      this.findings.removeAt(index);
      this.findings.insert(index + 1, step);
      this.updateOrderIds();
    }
  }
  getUp(index) {
    if (index > 0) {
      const step = this.findings.at(index);
      this.findings.removeAt(index);
      this.findings.insert(index - 1, step);
      this.updateOrderIds();
    }
  }
  updateOrderIds() {
    this.findings.controls.forEach((step, index) => {
      step.get("orderId")?.setValue(index + 1);
    });
    this.hasUnsavedChanges = true;
  }
};
_ExecutiveSummaryComponent.\u0275fac = function ExecutiveSummaryComponent_Factory(t) {
  return new (t || _ExecutiveSummaryComponent)(i04.\u0275\u0275directiveInject(i112.FormBuilder), i04.\u0275\u0275directiveInject(i25.Location), i04.\u0275\u0275directiveInject(TestService), i04.\u0275\u0275directiveInject(i42.ToastrService), i04.\u0275\u0275directiveInject(LoadingService), i04.\u0275\u0275directiveInject(CommonService));
};
_ExecutiveSummaryComponent.\u0275cmp = /* @__PURE__ */ i04.\u0275\u0275defineComponent({ type: _ExecutiveSummaryComponent, selectors: [["app-executive-summary"]], viewQuery: function ExecutiveSummaryComponent_Query(rf, ctx) {
  if (rf & 1) {
    i04.\u0275\u0275viewQuery(_c03, 5);
    i04.\u0275\u0275viewQuery(_c12, 5);
  }
  if (rf & 2) {
    let _t;
    i04.\u0275\u0275queryRefresh(_t = i04.\u0275\u0275loadQuery()) && (ctx.chartBarCanvasRef = _t.first);
    i04.\u0275\u0275queryRefresh(_t = i04.\u0275\u0275loadQuery()) && (ctx.chartPieCanvasRef = _t.first);
  }
}, decls: 96, vars: 20, consts: [["chartBarCanvas", ""], ["chartPieCanvas", ""], [1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "page-breadcrumb", "m-0"], [1, "breadcrumb", "mb-0"], [1, "breadcrumb-item"], ["routerLink", "/main/tests_management/test_list"], [1, "abc", 3, "click"], ["aria-current", "page", 1, "breadcrumb-item", "active"], [1, "button-container"], [3, "formGroup"], ["class", "form-check form-check-inline", 4, "ngIf"], [4, "ngIf"], [1, "btn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], [1, "btn", "btn-secondary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], [1, "forms-sample", 3, "formGroup"], [1, "row"], [1, "col-md-12", "grid-margin", "stretch-card"], [1, "card"], [1, "card-body"], [1, "mb-3"], [1, "card-title", "me-3", "d-flex", "gap-5", "justify-content-center"], ["for", "TestName", 1, "form-label", "d-flex", "gap-1"], [2, "margin-top", "3px"], ["for", "TestName", 1, "form-label"], [1, "text-danger"], ["id", "testIntroduction", "rows", "4", "placeholder", "Enter test introduction", "formControlName", "testIntroduction", 3, "keydown", "modules"], ["class", "text-danger", 4, "ngIf"], ["id", "esd", "rows", "4", "placeholder", "Enter executive summary", "formControlName", "executiveSummaryDesc", 3, "keydown", "modules"], ["for", "Business", 1, "form-label"], ["id", "Business", "rows", "4", "placeholder", "Enter business criticality", "formControlName", "criticality", 3, "keydown", "modules"], ["for", "TestDescription", 1, "form-label"], ["id", "TestDescription", "rows", "4", "placeholder", "Enter High-Level business risks", "formControlName", "businessImplication", 3, "keydown", "modules"], ["for", "managementRecommendations", 1, "form-label"], ["id", "managementRecommendations", "rows", "4", "placeholder", "Enter recommendations for management", "formControlName", "managementRecommendations", 3, "keydown", "modules"], [1, "col-md-6", "grid-margin", "stretch-card"], [1, "card-body", "d-flex", "justify-content-center"], ["id", "chart"], [1, "ChartWidth"], [1, "d-flex", "justify-content-between", "align-items-center", "flex-wrap", "grid-margin"], [1, "col-12", "col-md-auto", "my-2", "mb-md-0"], [1, "fw-semibold"], [1, "button-container", "d-flex", "align-items-center"], [1, "mx-1", "d-flex", "align-items-center"], [1, "form-check", "form-check-inline", "mb-md-0"], ["type", "checkbox", "id", "canManageTest", 1, "form-check-input", 3, "ngModelChange", "ngModel", "ngModelOptions"], ["for", "canManageTest", 1, "form-check-label"], [1, "mx-1", "d-flex", "align-items-center", "button-container"], ["type", "button", 1, "btn", "btn-outline-primary", "btn-icon-text", "mb-2", "mb-md-0", "extraBtn_w", 3, "click"], ["formArrayName", "findings"], [3, "formGroupName", 4, "ngFor", "ngForOf"], [1, "form-check", "form-check-inline"], ["type", "checkbox", "id", "inProgress", "formControlName", "isInProgressPass", 1, "form-check-input", 3, "change"], ["for", "inProgress", 1, "form-check-label"], ["for", "iReviewedLabel", 1, "form-check-label", "custom-bold"], ["type", "checkbox", "id", "passReview", "formControlName", "iReviewedPass", 1, "form-check-input", 3, "change"], ["for", "passReview", 1, "form-check-label"], ["type", "checkbox", "id", "failReview", "formControlName", "iReviewedFail", 1, "form-check-input", 3, "change"], ["for", "failReview", 1, "form-check-label"], ["for", "iiReviewedLabel", 1, "form-check-label", "custom-bold"], ["type", "checkbox", "id", "passIIReview", "formControlName", "iiReviewedPass", 1, "form-check-input", 3, "change"], ["for", "passIIReview", 1, "form-check-label"], ["type", "checkbox", "id", "failIIReview", "formControlName", "iiReviewedFail", 1, "form-check-input", 3, "change"], ["for", "failIIReview", 1, "form-check-label"], [3, "formGroupName"], [1, "card", "card-grey", "mb-3"], [1, "card-body", "d-flex", "justify-content-between", "align-items-center", "p-0", "p-2"], [3, "click"], ["data-feather", "arrow-down-circle", "appFeatherIcon", "", 1, "btn-icon-prepend", "hover-icon", "btn_icon"], ["data-feather", "arrow-up-circle", "appFeatherIcon", "", 1, "btn-icon-prepend", "hover-icon", "btn_icon"], ["type", "checkbox", "formControlName", "isHidden", 1, "form-check-input", 3, "id"], [1, "form-check-label", 3, "for"], [1, "form-label", 3, "for"], ["rows", "4", "placeholder", "Key Issue", "formControlName", "keyIssuesDetail", 3, "keydown", "modules", "id", "readOnly", "ngClass"], ["rows", "4", "placeholder", "Impact Summary", "formControlName", "impactSummary", 3, "keydown", "modules", "id", "readOnly", "ngClass"], ["rows", "4", "placeholder", "Remediation", "formControlName", "remediation", 3, "keydown", "modules", "id", "readOnly", "ngClass"]], template: function ExecutiveSummaryComponent_Template(rf, ctx) {
  if (rf & 1) {
    const _r1 = i04.\u0275\u0275getCurrentView();
    i04.\u0275\u0275elementStart(0, "div", 2)(1, "div", 3)(2, "div", 4)(3, "nav", 5)(4, "ol", 6)(5, "li", 7)(6, "a", 8);
    i04.\u0275\u0275text(7, "Test Management");
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(8, "li", 7)(9, "a", 9);
    i04.\u0275\u0275listener("click", function ExecutiveSummaryComponent_Template_a_click_9_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.goBack());
    });
    i04.\u0275\u0275text(10, "Test Masters");
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(11, "li", 10);
    i04.\u0275\u0275text(12, " Executive summary ");
    i04.\u0275\u0275elementEnd()()();
    i04.\u0275\u0275elementStart(13, "div", 11)(14, "form", 12);
    i04.\u0275\u0275template(15, ExecutiveSummaryComponent_div_15_Template, 4, 0, "div", 13)(16, ExecutiveSummaryComponent_div_16_Template, 2, 1, "div", 14)(17, ExecutiveSummaryComponent_div_17_Template, 2, 1, "div", 14);
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(18, "div", 11)(19, "button", 15);
    i04.\u0275\u0275listener("click", function ExecutiveSummaryComponent_Template_button_click_19_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.onSubmit());
    });
    i04.\u0275\u0275text(20, "Save");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(21, "button", 16);
    i04.\u0275\u0275listener("click", function ExecutiveSummaryComponent_Template_button_click_21_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.goBack());
    });
    i04.\u0275\u0275text(22, "Cancel");
    i04.\u0275\u0275elementEnd()()()()();
    i04.\u0275\u0275elementStart(23, "form", 17)(24, "div", 18)(25, "div", 19)(26, "div", 20)(27, "div", 21)(28, "div", 22)(29, "h6", 23);
    i04.\u0275\u0275template(30, ExecutiveSummaryComponent_span_30_Template, 2, 1, "span", 14)(31, ExecutiveSummaryComponent_span_31_Template, 2, 1, "span", 14)(32, ExecutiveSummaryComponent_span_32_Template, 2, 1, "span", 14);
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(33, "div", 22)(34, "label", 24);
    i04.\u0275\u0275text(35, "Test title: ");
    i04.\u0275\u0275elementStart(36, "h6", 25);
    i04.\u0275\u0275text(37);
    i04.\u0275\u0275elementEnd()()();
    i04.\u0275\u0275elementStart(38, "div", 22)(39, "label", 26);
    i04.\u0275\u0275text(40, "Test Introduction");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(41, "span", 27);
    i04.\u0275\u0275text(42, " *");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(43, "quill-editor", 28);
    i04.\u0275\u0275listener("keydown", function ExecutiveSummaryComponent_Template_quill_editor_keydown_43_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275template(44, ExecutiveSummaryComponent_div_44_Template, 2, 1, "div", 29);
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(45, "div", 22)(46, "label", 26);
    i04.\u0275\u0275text(47, "Executive Summary");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(48, "quill-editor", 30);
    i04.\u0275\u0275listener("keydown", function ExecutiveSummaryComponent_Template_quill_editor_keydown_48_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275template(49, ExecutiveSummaryComponent_div_49_Template, 2, 1, "div", 29);
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(50, "div", 22)(51, "label", 31);
    i04.\u0275\u0275text(52, "Business Criticality");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(53, "quill-editor", 32);
    i04.\u0275\u0275listener("keydown", function ExecutiveSummaryComponent_Template_quill_editor_keydown_53_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(54, "div", 22)(55, "label", 33);
    i04.\u0275\u0275text(56, " High-Level Business Risks ");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(57, "quill-editor", 34);
    i04.\u0275\u0275listener("keydown", function ExecutiveSummaryComponent_Template_quill_editor_keydown_57_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(58, "div", 22)(59, "label", 35);
    i04.\u0275\u0275text(60, " Recommendations for Management ");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(61, "quill-editor", 36);
    i04.\u0275\u0275listener("keydown", function ExecutiveSummaryComponent_Template_quill_editor_keydown_61_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.onKeyPressInputChange(true));
    });
    i04.\u0275\u0275elementEnd()()()()()();
    i04.\u0275\u0275elementStart(62, "div", 18)(63, "div", 37)(64, "div", 20)(65, "div", 38)(66, "div");
    i04.\u0275\u0275element(67, "canvas", 39, 0);
    i04.\u0275\u0275elementEnd()()()();
    i04.\u0275\u0275elementStart(69, "div", 37)(70, "div", 20)(71, "div", 38)(72, "div");
    i04.\u0275\u0275element(73, "canvas", 40, 1);
    i04.\u0275\u0275elementEnd()()()()();
    i04.\u0275\u0275elementStart(75, "div", 18)(76, "div", 19)(77, "div", 20)(78, "div", 21)(79, "div", 41)(80, "div", 42)(81, "h5", 43);
    i04.\u0275\u0275text(82, " Key issues, Impact Summary and Remediation ");
    i04.\u0275\u0275elementEnd()();
    i04.\u0275\u0275elementStart(83, "div", 44)(84, "div", 45)(85, "div", 46)(86, "input", 47);
    i04.\u0275\u0275twoWayListener("ngModelChange", function ExecutiveSummaryComponent_Template_input_ngModelChange_86_listener($event) {
      i04.\u0275\u0275restoreView(_r1);
      i04.\u0275\u0275twoWayBindingSet(ctx.isAllShow, $event) || (ctx.isAllShow = $event);
      return i04.\u0275\u0275resetView($event);
    });
    i04.\u0275\u0275listener("ngModelChange", function ExecutiveSummaryComponent_Template_input_ngModelChange_86_listener($event) {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.allShowHide($event));
    });
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(87, "label", 48);
    i04.\u0275\u0275text(88, " Show All/None ");
    i04.\u0275\u0275elementEnd()()();
    i04.\u0275\u0275elementStart(89, "div", 49)(90, "button", 50);
    i04.\u0275\u0275listener("click", function ExecutiveSummaryComponent_Template_button_click_90_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.saveTemporaryData());
    });
    i04.\u0275\u0275text(91, " Apply Changes ");
    i04.\u0275\u0275elementEnd();
    i04.\u0275\u0275elementStart(92, "button", 50);
    i04.\u0275\u0275listener("click", function ExecutiveSummaryComponent_Template_button_click_92_listener() {
      i04.\u0275\u0275restoreView(_r1);
      return i04.\u0275\u0275resetView(ctx.reloadData());
    });
    i04.\u0275\u0275text(93, " Load New Issues ");
    i04.\u0275\u0275elementEnd()()()();
    i04.\u0275\u0275elementStart(94, "div", 51);
    i04.\u0275\u0275template(95, ExecutiveSummaryComponent_div_95_Template, 28, 29, "div", 52);
    i04.\u0275\u0275elementEnd()()()()()();
  }
  if (rf & 2) {
    let tmp_3_0;
    let tmp_7_0;
    let tmp_8_0;
    let tmp_9_0;
    let tmp_10_0;
    let tmp_12_0;
    let tmp_14_0;
    i04.\u0275\u0275advance(14);
    i04.\u0275\u0275property("formGroup", ctx.executiveSummaryForm);
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", (tmp_3_0 = ctx.executiveSummaryForm.get("isInProgress")) == null ? null : tmp_3_0.value);
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", ctx.canManageIReview);
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", ctx.canManageIIReview);
    i04.\u0275\u0275advance(6);
    i04.\u0275\u0275property("formGroup", ctx.executiveSummaryForm);
    i04.\u0275\u0275advance(7);
    i04.\u0275\u0275property("ngIf", (tmp_7_0 = ctx.executiveSummaryForm.get("createdBy")) == null ? null : tmp_7_0.value);
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", (tmp_8_0 = ctx.executiveSummaryForm.get("iReviewed")) == null ? null : tmp_8_0.value);
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", (tmp_9_0 = ctx.executiveSummaryForm.get("iiReviewed")) == null ? null : tmp_9_0.value);
    i04.\u0275\u0275advance(5);
    i04.\u0275\u0275textInterpolate1(" ", (tmp_10_0 = ctx.executiveSummaryForm.get("testTitle")) == null ? null : tmp_10_0.value, "");
    i04.\u0275\u0275advance(6);
    i04.\u0275\u0275property("modules", ctx.preContentConfig);
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", (ctx.executiveSummaryForm == null ? null : (tmp_12_0 = ctx.executiveSummaryForm.get("testIntroduction")) == null ? null : tmp_12_0.dirty) && (ctx.executiveSummaryForm == null ? null : (tmp_12_0 = ctx.executiveSummaryForm.get("testIntroduction")) == null ? null : tmp_12_0.errors) || (ctx.executiveSummaryForm == null ? null : (tmp_12_0 = ctx.executiveSummaryForm.get("testIntroduction")) == null ? null : tmp_12_0.touched));
    i04.\u0275\u0275advance(4);
    i04.\u0275\u0275property("modules", ctx.preContentConfig);
    i04.\u0275\u0275advance();
    i04.\u0275\u0275property("ngIf", (ctx.executiveSummaryForm == null ? null : (tmp_14_0 = ctx.executiveSummaryForm.get("executiveSummaryDesc")) == null ? null : tmp_14_0.dirty) && (ctx.executiveSummaryForm == null ? null : (tmp_14_0 = ctx.executiveSummaryForm.get("executiveSummaryDesc")) == null ? null : tmp_14_0.errors) || (ctx.executiveSummaryForm == null ? null : (tmp_14_0 = ctx.executiveSummaryForm.get("executiveSummaryDesc")) == null ? null : tmp_14_0.touched));
    i04.\u0275\u0275advance(4);
    i04.\u0275\u0275property("modules", ctx.preContentConfig);
    i04.\u0275\u0275advance(4);
    i04.\u0275\u0275property("modules", ctx.preContentConfig);
    i04.\u0275\u0275advance(4);
    i04.\u0275\u0275property("modules", ctx.preContentConfig);
    i04.\u0275\u0275advance(25);
    i04.\u0275\u0275twoWayProperty("ngModel", ctx.isAllShow);
    i04.\u0275\u0275property("ngModelOptions", i04.\u0275\u0275pureFunction0(19, _c22));
    i04.\u0275\u0275advance(9);
    i04.\u0275\u0275property("ngForOf", ctx.findings.controls);
  }
}, dependencies: [i25.NgClass, i25.NgForOf, i25.NgIf, i72.RouterLink, i112.\u0275NgNoValidate, i112.CheckboxControlValueAccessor, i112.NgControlStatus, i112.NgControlStatusGroup, i112.NgModel, i112.FormGroupDirective, i112.FormControlName, i112.FormGroupName, i112.FormArrayName, FeatherIconDirective, i93.QuillEditorComponent], styles: ['\n\n.hover-icon[_ngcontent-%COMP%] {\n  transition: transform 0.3s, color 0.3s;\n  font-size: 16px !important;\n}\n.hover-icon[_ngcontent-%COMP%]:hover {\n  transform: scale(1.2);\n  color: #515acc;\n  font-size: 20px !important;\n}\n.card-grey[_ngcontent-%COMP%] {\n  background-color: #e9ebfd;\n}\n.ChartWidth[_ngcontent-%COMP%] {\n  width: 256px;\n  height: 256px;\n}\n#chart[_ngcontent-%COMP%] {\n  display: block;\n  box-sizing: border-box;\n  height: 240px;\n  width: 480px;\n}\n.chart-pie-w[_ngcontent-%COMP%] {\n  width: 400px !important;\n}\n@media (max-width: 780px) {\n  .extraBtn_w[_ngcontent-%COMP%] {\n    width: 20vh;\n  }\n}\n  .ql-toolbar {\n  border-radius: 0.25rem 0.25rem 0 0 !important;\n}\n  .ql-container {\n  border-radius: 0 0 0.25rem 0.25rem !important;\n}\n  .ql-editor.ql-blank::before {\n  font-style: normal;\n  font-family:\n    "Roboto",\n    Helvetica,\n    sans-serif;\n  font-size: 14px;\n  color: #999;\n}\n  .dropdown-list li h5 {\n  font-style: normal;\n  font-family:\n    "Roboto",\n    Helvetica,\n    sans-serif;\n  font-size: 14px;\n  color: #999;\n  font-weight: 400;\n}\n.disabled[_ngcontent-%COMP%] {\n  opacity: 0.5;\n  pointer-events: none;\n  background-color: #ddd;\n}\n/*# sourceMappingURL=executive-summary.component.css.map */'] });
var ExecutiveSummaryComponent = _ExecutiveSummaryComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i04.\u0275setClassDebugInfo(ExecutiveSummaryComponent, { className: "ExecutiveSummaryComponent", filePath: "src/app/modules/test/executive-summary/executive-summary.component.ts", lineNumber: 15 });
})();

// src/app/modules/test/test-routing.module.ts
import * as i05 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
var routes = [
  {
    path: "test_list",
    component: TestManagementComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "test_update",
    component: TestUpdatesComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "master_test_data",
    component: MasterFindingsComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "executive_summary",
    component: ExecutiveSummaryComponent,
    canActivate: [AuthGuard]
  }
];
var _TestRoutingModule = class _TestRoutingModule {
};
_TestRoutingModule.\u0275fac = function TestRoutingModule_Factory(t) {
  return new (t || _TestRoutingModule)();
};
_TestRoutingModule.\u0275mod = /* @__PURE__ */ i05.\u0275\u0275defineNgModule({ type: _TestRoutingModule });
_TestRoutingModule.\u0275inj = /* @__PURE__ */ i05.\u0275\u0275defineInjector({ imports: [RouterModule.forChild(routes), RouterModule] });
var TestRoutingModule = _TestRoutingModule;

// src/app/modules/test/test.module.ts
import { QuillModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-quill.js?v=ca23e844";
import * as i06 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
var _TestModule = class _TestModule {
};
_TestModule.\u0275fac = function TestModule_Factory(t) {
  return new (t || _TestModule)();
};
_TestModule.\u0275mod = /* @__PURE__ */ i06.\u0275\u0275defineNgModule({ type: _TestModule });
_TestModule.\u0275inj = /* @__PURE__ */ i06.\u0275\u0275defineInjector({ imports: [
  CommonModule,
  TestRoutingModule,
  SharedModule,
  QuillModule.forRoot()
] });
var TestModule = _TestModule;
export {
  TestModule
};
