import {
  OrganizationService
} from "/chunk-PMOPTSW5.js";
import {
  UserService
} from "/chunk-5YCVMAC5.js";
import {
  LoadingService
} from "/chunk-DDGOKMT7.js";
import {
  AuthGuard
} from "/chunk-WGCVQTUY.js";
import "/chunk-RTM3KQT4.js";
import {
  FeatherIconDirective,
  SharedModule,
  __spreadProps,
  __spreadValues
} from "/chunk-2CBLJUUC.js";

// src/app/modules/organizations/organizations.module.ts
import { NgModule as NgModule2 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { CommonModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";

// src/app/modules/organizations/organizations-routing.module.ts
import { NgModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { RouterModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";

// src/app/modules/organizations/organizations-management/organizations-management.component.ts
import { Component } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i0 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i1 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i3 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";
import * as i6 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
import * as i7 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i8 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_button.js?v=ca23e844";
import * as i9 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_core_transition-patch.js?v=ca23e844";
import * as i10 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_core_wave.js?v=ca23e844";
import * as i11 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_icon.js?v=ca23e844";
import * as i12 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_dropdown.js?v=ca23e844";
import * as i13 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_input.js?v=ca23e844";
import * as i14 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_table.js?v=ca23e844";
import * as i15 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_tooltip.js?v=ca23e844";
import * as i16 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_popconfirm.js?v=ca23e844";
import * as i18 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@ng-bootstrap_ng-bootstrap.js?v=ca23e844";
function OrganizationsManagementComponent_button_7_Template(rf, ctx) {
  if (rf & 1) {
    const _r2 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "button", 39);
    i0.\u0275\u0275listener("click", function OrganizationsManagementComponent_button_7_Template_button_click_0_listener() {
      i0.\u0275\u0275restoreView(_r2);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.addRow());
    });
    i0.\u0275\u0275element(1, "i", 40);
    i0.\u0275\u0275text(2, " Add Organization ");
    i0.\u0275\u0275elementEnd();
  }
}
function OrganizationsManagementComponent_a_26_Template(rf, ctx) {
  if (rf & 1) {
    const _r4 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "a", 41);
    i0.\u0275\u0275listener("nzOnConfirm", function OrganizationsManagementComponent_a_26_Template_a_nzOnConfirm_0_listener() {
      i0.\u0275\u0275restoreView(_r4);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.deleteOrg());
    });
    i0.\u0275\u0275elementStart(1, "button", 42);
    i0.\u0275\u0275element(2, "span", 43);
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipColor", ctx_r2.color);
  }
}
function OrganizationsManagementComponent_th_31_Template(rf, ctx) {
  if (rf & 1) {
    const _r5 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "th", 44);
    i0.\u0275\u0275listener("nzCheckedChange", function OrganizationsManagementComponent_th_31_Template_th_nzCheckedChange_0_listener($event) {
      i0.\u0275\u0275restoreView(_r5);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.onAllChecked($event));
    });
    i0.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275property("nzChecked", ctx_r2.checked)("nzIndeterminate", ctx_r2.indeterminate);
  }
}
function OrganizationsManagementComponent_tr_45_td_1_Template(rf, ctx) {
  if (rf & 1) {
    const _r8 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "td", 49);
    i0.\u0275\u0275listener("nzCheckedChange", function OrganizationsManagementComponent_tr_45_td_1_Template_td_nzCheckedChange_0_listener($event) {
      i0.\u0275\u0275restoreView(_r8);
      const data_r7 = i0.\u0275\u0275nextContext().$implicit;
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView(ctx_r2.onItemChecked(data_r7._id, $event));
    });
    i0.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const data_r7 = i0.\u0275\u0275nextContext().$implicit;
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275property("nzChecked", ctx_r2.setOfCheckedId.has(data_r7._id))("nzLabel", data_r7.name);
  }
}
function OrganizationsManagementComponent_tr_45_Template(rf, ctx) {
  if (rf & 1) {
    const _r6 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "tr", 45);
    i0.\u0275\u0275listener("click", function OrganizationsManagementComponent_tr_45_Template_tr_click_0_listener() {
      const data_r7 = i0.\u0275\u0275restoreView(_r6).$implicit;
      const ctx_r2 = i0.\u0275\u0275nextContext();
      return i0.\u0275\u0275resetView((ctx_r2.canManageOrg || ctx_r2.isAdmin) && ctx_r2.addRow(data_r7._id));
    });
    i0.\u0275\u0275template(1, OrganizationsManagementComponent_tr_45_td_1_Template, 1, 2, "td", 46);
    i0.\u0275\u0275elementStart(2, "td", 47);
    i0.\u0275\u0275text(3);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(4, "td", 48);
    i0.\u0275\u0275text(5);
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(6, "td", 48);
    i0.\u0275\u0275text(7);
    i0.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const data_r7 = ctx.$implicit;
    const ctx_r2 = i0.\u0275\u0275nextContext();
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("ngIf", ctx_r2.canManageOrg || ctx_r2.isAdmin);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipTitle", data_r7.orgName)("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", data_r7.orgName, " ");
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipTitle", data_r7.industrySector)("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", data_r7.industrySector, " ");
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzTooltipTitle", data_r7.headQuarterLocation)("nzTooltipColor", ctx_r2.color);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275textInterpolate1(" ", data_r7.headQuarterLocation, " ");
  }
}
function OrganizationsManagementComponent_div_46_ng_template_6_Template(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275text(0, "Prev");
  }
}
function OrganizationsManagementComponent_div_46_ng_template_7_Template(rf, ctx) {
  if (rf & 1) {
    i0.\u0275\u0275text(0, "Next");
  }
}
function OrganizationsManagementComponent_div_46_Template(rf, ctx) {
  if (rf & 1) {
    const _r9 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 9)(1, "div", 50)(2, "div", 51);
    i0.\u0275\u0275text(3);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(4, "div", 52)(5, "ngb-pagination", 53);
    i0.\u0275\u0275twoWayListener("pageChange", function OrganizationsManagementComponent_div_46_Template_ngb_pagination_pageChange_5_listener($event) {
      i0.\u0275\u0275restoreView(_r9);
      const ctx_r2 = i0.\u0275\u0275nextContext();
      i0.\u0275\u0275twoWayBindingSet(ctx_r2.pageIndex, $event) || (ctx_r2.pageIndex = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275template(6, OrganizationsManagementComponent_div_46_ng_template_6_Template, 1, 0, "ng-template", 54)(7, OrganizationsManagementComponent_div_46_ng_template_7_Template, 1, 0, "ng-template", 55);
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
var _OrganizationsManagementComponent = class _OrganizationsManagementComponent {
  constructor(router, organizationService, toastr, userService, loaderService) {
    this.router = router;
    this.organizationService = organizationService;
    this.toastr = toastr;
    this.userService = userService;
    this.loaderService = loaderService;
    this.totalRecords = 0;
    this.totalPages = 1;
    this.loading = false;
    this.pageSize = 10;
    this.pageIndex = 1;
    this.onKeyString = "";
    this.orgSearchValue = "";
    this.indusSearchValue = "";
    this.headSearchValue = "";
    this.isOrgSearchValue = false;
    this.isIndusSearchValue = false;
    this.isHeadSearchValue = false;
    this.listOfOrg = [];
    this.currentPageRange = "";
    this.color = "black";
    this.canManageOrg = false;
    this.isAdmin = false;
    this.checked = false;
    this.indeterminate = false;
    this.listOfCurrentPageData = [];
    this.setOfCheckedId = /* @__PURE__ */ new Set();
  }
  ngOnInit() {
    this.accsssData();
  }
  accsssData() {
    const getUserAccessData = this.userService.getUserAccessData();
    this.canManageOrg = getUserAccessData[0]?.canManageOrg;
  }
  loadDataFromServer(pageIndex, pageSize, sortField, sortOrder, search) {
    this.loading = true;
    this.organizationService.GetOrgList(pageIndex, pageSize, search, sortOrder).subscribe({
      next: (response) => {
        if (response.status === true) {
          if (!response.data.length) {
            this.listOfOrg = [];
            this.loading = false;
            return;
          }
          this.listOfOrg = response.data;
          this.totalRecords = response.totalRecords;
          this.isAdmin = response?.isAdmin;
          this.onCurrentPageDataChange(this.listOfOrg);
          this.calculatePageRange();
          this.loading = false;
        }
      },
      error: (err) => {
        this.loading = false;
        return this.toastr.error(err.error.message, "Organization Management");
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
  resetPageIndex() {
    this.pageIndex = 1;
  }
  reset() {
    this.orgSearchValue = "";
    this.indusSearchValue = "";
    this.headSearchValue = "";
    this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, []);
  }
  onKeyUp(columName, event) {
    this.onKeyString += event.key;
    setTimeout(() => {
      this.search(columName, this.onKeyString);
    }, 1e3);
  }
  search(columName, onKeyString) {
    if (columName === "orgName") {
      this.isOrgSearchValue = false;
      const searchData = { type: "sort", key: columName, value: this.orgSearchValue };
      this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "industrySector") {
      this.isIndusSearchValue = false;
      const searchData = { type: "sort", key: columName, value: this.indusSearchValue };
      this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "headQuarterLocation") {
      this.isHeadSearchValue = false;
      const searchData = { type: "sort", key: columName, value: this.headSearchValue };
      this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
    } else {
      this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, []);
    }
  }
  addRow(_id) {
    this.router.navigate(["/main/organizations_management/add_organizations"], { state: { data: _id } });
  }
  deleteOrg() {
    this.loading = true;
    const oraganizationIds = [...this.setOfCheckedId];
    this.organizationService.DeleteOrgrDetails({ orgIds: oraganizationIds }).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, []);
          this.setOfCheckedId = new Set([...this.setOfCheckedId].filter((id) => !oraganizationIds.includes(id)));
          this.toastr.success(response.message, "Organization Management");
          this.loading = false;
        }
      },
      error: (err) => {
        this.loading = false;
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  calculatePageRange() {
    const startItem = (this.pageIndex - 1) * this.pageSize + 1;
    const endItem = Math.min(this.pageIndex * this.pageSize, this.totalRecords);
    this.totalPages = Math.ceil(this.totalRecords / this.pageSize);
    this.currentPageRange = `Showing ${startItem} to ${endItem} of ${this.totalRecords} entries`;
  }
  changePage(page) {
    if (page > 0 && page <= this.totalPages) {
      this.pageIndex = page;
      this.calculatePageRange();
    }
  }
  onEnter(columName) {
    this.search(columName);
  }
  onKeydown(columName) {
    if (this.debounceTimeout) {
      clearTimeout(this.debounceTimeout);
    }
    this.debounceTimeout = setTimeout(() => {
      if (columName === "orgName") {
        const searchData = { type: "sort", key: columName, value: this.orgSearchValue };
        this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
      } else if (columName === "industrySector") {
        const searchData = { type: "sort", key: columName, value: this.indusSearchValue };
        this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
      } else if (columName === "headQuarterLocation") {
        const searchData = { type: "sort", key: columName, value: this.headSearchValue };
        this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
      } else {
        this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, []);
      }
    }, 2e3);
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
};
_OrganizationsManagementComponent.\u0275fac = function OrganizationsManagementComponent_Factory(t) {
  return new (t || _OrganizationsManagementComponent)(i0.\u0275\u0275directiveInject(i1.Router), i0.\u0275\u0275directiveInject(OrganizationService), i0.\u0275\u0275directiveInject(i3.ToastrService), i0.\u0275\u0275directiveInject(UserService), i0.\u0275\u0275directiveInject(LoadingService));
};
_OrganizationsManagementComponent.\u0275cmp = /* @__PURE__ */ i0.\u0275\u0275defineComponent({ type: _OrganizationsManagementComponent, selectors: [["app-organizations-management"]], decls: 77, vars: 27, consts: [["orgSearch", "nzDropdownMenu"], ["indusSearch", "nzDropdownMenu"], ["headSearch", "nzDropdownMenu"], [1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "mb-3", "mb-md-0"], [1, "d-flex", "align-items-center", "flex-wrap", "text-nowrap"], ["type", "button", "class", "btn btn-primary btn-icon-text mb-2 mb-md-0", 3, "click", 4, "ngIf"], [1, "row"], [1, "col-md-12", "stretch-card"], [1, "card"], [1, "card-body"], [1, "dataTable-top"], [1, "dataTable-dropdown"], [1, "dataTable-selector", 3, "ngModelChange", "change", "ngModel"], ["value", "10", "selected", ""], ["value", "15"], ["value", "20"], ["value", "25"], [1, "d-flex", "justify-content-end"], ["nz-popconfirm", "", "nzPopconfirmTitle", "Sure to delete?", 3, "nzOnConfirm", 4, "ngIf"], [1, "table-container", "dataTable"], ["nzShowSizeChanger", "", 3, "nzQueryParams", "nzCurrentPageDataChange", "nzData", "nzLoading", "nzTotal", "nzPageSize", "nzPageIndex", "nzShowPagination"], ["class", "check-Box-Width", "nzLabel", "Select all", 3, "nzChecked", "nzIndeterminate", "nzCheckedChange", 4, "ngIf"], ["id", "1", "nzColumnKey", "orgName", "nzCustomFilter", "", 3, "nzSortFn"], [3, "nzVisibleChange", "nzVisible", "nzActive", "nzDropdownMenu"], ["nz-icon", "", "nzType", "search"], ["id", "2", "nzColumnKey", "industrySector", "nzCustomFilter", "", 3, "nzSortFn"], ["id", "3", "nzColumnKey", "headQuarterLocation", "nzCustomFilter", "", 3, "nzSortFn"], [3, "click", 4, "ngFor", "ngForOf"], ["class", "row", 4, "ngIf"], [1, "ant-table-filter-dropdown"], [1, "search-box"], ["type", "text", "id", "", "nz-input", "", "placeholder", "Search organization", 3, "keydown", "keydown.enter", "ngModelChange", "ngModel"], ["type", "button", 1, "btn", "searchbtn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["type", "button", 1, "btn", "searchbtn", "btn-outline-primary", "btn-icon-text", "me-2", "mb-2", "mb-md-0", 3, "click"], ["type", "text", "nz-input", "", "placeholder", "Search industry sector ", 3, "keydown", "keydown.enter", "ngModelChange", "ngModel"], ["type", "text", "nz-input", "", "placeholder", "Search headquarter", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "button", 1, "btn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["data-feather", "plus", "appFeatherIcon", "", 1, "btn-icon-prepend"], ["nz-popconfirm", "", "nzPopconfirmTitle", "Sure to delete?", 3, "nzOnConfirm"], ["nz-button", "", "nzType", "primary", "nzSize", "large", "nzTooltipTitle", "Delete All Organization", "nzTooltipPlacement", "top", "nz-tooltip", "", 3, "nzTooltipColor"], ["nz-icon", "", "nzType", "delete", "nzTheme", "outline"], ["nzLabel", "Select all", 1, "check-Box-Width", 3, "nzCheckedChange", "nzChecked", "nzIndeterminate"], [3, "click"], ["class", "check-Box-Width", 3, "nzChecked", "nzLabel", "nzCheckedChange", 4, "ngIf"], ["nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", 1, "ellipsis", 3, "nzTooltipTitle", "nzTooltipColor"], ["nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", "nz-tooltip", "", 1, "ellipsis", 3, "nzTooltipTitle", "nzTooltipColor"], [1, "check-Box-Width", 3, "nzCheckedChange", "nzChecked", "nzLabel"], [1, "col-sm-6", "col-md-5"], ["id", "dataTableExample_info", "role", "status", "aria-live", "polite", 1, "dataTables_info"], [1, "col-sm-6", "col-md-7"], [1, "d-flex", "justify-content-end", 3, "pageChange", "collectionSize", "page", "maxSize", "rotate", "ellipses", "boundaryLinks"], ["ngbPaginationPrevious", ""], ["ngbPaginationNext", ""]], template: function OrganizationsManagementComponent_Template(rf, ctx) {
  if (rf & 1) {
    const _r1 = i0.\u0275\u0275getCurrentView();
    i0.\u0275\u0275elementStart(0, "div", 3)(1, "div", 4)(2, "div", 5)(3, "div")(4, "h4", 6);
    i0.\u0275\u0275text(5, "Organization Management");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(6, "div", 7);
    i0.\u0275\u0275template(7, OrganizationsManagementComponent_button_7_Template, 3, 0, "button", 8);
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(8, "div", 9)(9, "div", 10)(10, "div", 11)(11, "div", 12)(12, "div", 13)(13, "div", 14)(14, "label")(15, "select", 15);
    i0.\u0275\u0275twoWayListener("ngModelChange", function OrganizationsManagementComponent_Template_select_ngModelChange_15_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.pageSize, $event) || (ctx.pageSize = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("change", function OrganizationsManagementComponent_Template_select_change_15_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.resetPageIndex());
    });
    i0.\u0275\u0275elementStart(16, "option", 16);
    i0.\u0275\u0275text(17, "10");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(18, "option", 17);
    i0.\u0275\u0275text(19, "15");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(20, "option", 18);
    i0.\u0275\u0275text(21, "20");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(22, "option", 19);
    i0.\u0275\u0275text(23, "25");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275text(24, " entries per page");
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(25, "div", 20);
    i0.\u0275\u0275template(26, OrganizationsManagementComponent_a_26_Template, 3, 1, "a", 21);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(27, "div", 22)(28, "nz-table", 23);
    i0.\u0275\u0275listener("nzQueryParams", function OrganizationsManagementComponent_Template_nz_table_nzQueryParams_28_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onQueryParamsChange($event));
    })("nzCurrentPageDataChange", function OrganizationsManagementComponent_Template_nz_table_nzCurrentPageDataChange_28_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onCurrentPageDataChange($event));
    });
    i0.\u0275\u0275elementStart(29, "thead")(30, "tr");
    i0.\u0275\u0275template(31, OrganizationsManagementComponent_th_31_Template, 1, 2, "th", 24);
    i0.\u0275\u0275elementStart(32, "th", 25);
    i0.\u0275\u0275text(33, " Organization ");
    i0.\u0275\u0275elementStart(34, "nz-filter-trigger", 26);
    i0.\u0275\u0275twoWayListener("nzVisibleChange", function OrganizationsManagementComponent_Template_nz_filter_trigger_nzVisibleChange_34_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isOrgSearchValue, $event) || (ctx.isOrgSearchValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275element(35, "span", 27);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(36, "th", 28);
    i0.\u0275\u0275text(37, " Industry Sector ");
    i0.\u0275\u0275elementStart(38, "nz-filter-trigger", 26);
    i0.\u0275\u0275twoWayListener("nzVisibleChange", function OrganizationsManagementComponent_Template_nz_filter_trigger_nzVisibleChange_38_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isIndusSearchValue, $event) || (ctx.isIndusSearchValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275element(39, "span", 27);
    i0.\u0275\u0275elementEnd()();
    i0.\u0275\u0275elementStart(40, "th", 29);
    i0.\u0275\u0275text(41, " Headquarter ");
    i0.\u0275\u0275elementStart(42, "nz-filter-trigger", 26);
    i0.\u0275\u0275twoWayListener("nzVisibleChange", function OrganizationsManagementComponent_Template_nz_filter_trigger_nzVisibleChange_42_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.isHeadSearchValue, $event) || (ctx.isHeadSearchValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275element(43, "span", 27);
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(44, "tbody");
    i0.\u0275\u0275template(45, OrganizationsManagementComponent_tr_45_Template, 8, 10, "tr", 30);
    i0.\u0275\u0275elementEnd()()();
    i0.\u0275\u0275template(46, OrganizationsManagementComponent_div_46_Template, 8, 7, "div", 31);
    i0.\u0275\u0275elementStart(47, "nz-dropdown-menu", null, 0)(49, "div", 32)(50, "div", 33)(51, "input", 34);
    i0.\u0275\u0275listener("keydown", function OrganizationsManagementComponent_Template_input_keydown_51_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onKeydown("orgName"));
    })("keydown.enter", function OrganizationsManagementComponent_Template_input_keydown_enter_51_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onEnter("orgName"));
    });
    i0.\u0275\u0275twoWayListener("ngModelChange", function OrganizationsManagementComponent_Template_input_ngModelChange_51_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.orgSearchValue, $event) || (ctx.orgSearchValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(52, "button", 35);
    i0.\u0275\u0275listener("click", function OrganizationsManagementComponent_Template_button_click_52_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.search("orgName"));
    });
    i0.\u0275\u0275text(53, " Search");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275text(54, "\xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(55, "button", 36);
    i0.\u0275\u0275listener("click", function OrganizationsManagementComponent_Template_button_click_55_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.reset());
    });
    i0.\u0275\u0275text(56, " Reset ");
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(57, "nz-dropdown-menu", null, 1)(59, "div", 32)(60, "div", 33)(61, "input", 37);
    i0.\u0275\u0275listener("keydown", function OrganizationsManagementComponent_Template_input_keydown_61_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onKeydown("industrySector"));
    })("keydown.enter", function OrganizationsManagementComponent_Template_input_keydown_enter_61_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onEnter("industrySector"));
    });
    i0.\u0275\u0275twoWayListener("ngModelChange", function OrganizationsManagementComponent_Template_input_ngModelChange_61_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.indusSearchValue, $event) || (ctx.indusSearchValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(62, "button", 35);
    i0.\u0275\u0275listener("click", function OrganizationsManagementComponent_Template_button_click_62_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.search("industrySector"));
    });
    i0.\u0275\u0275text(63, " Search");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275text(64, "\xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(65, "button", 36);
    i0.\u0275\u0275listener("click", function OrganizationsManagementComponent_Template_button_click_65_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.reset());
    });
    i0.\u0275\u0275text(66, " Reset ");
    i0.\u0275\u0275elementEnd()()()();
    i0.\u0275\u0275elementStart(67, "nz-dropdown-menu", null, 2)(69, "div", 32)(70, "div", 33)(71, "input", 38);
    i0.\u0275\u0275twoWayListener("ngModelChange", function OrganizationsManagementComponent_Template_input_ngModelChange_71_listener($event) {
      i0.\u0275\u0275restoreView(_r1);
      i0.\u0275\u0275twoWayBindingSet(ctx.headSearchValue, $event) || (ctx.headSearchValue = $event);
      return i0.\u0275\u0275resetView($event);
    });
    i0.\u0275\u0275listener("keydown", function OrganizationsManagementComponent_Template_input_keydown_71_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onKeydown("headQuarterLocation"));
    })("keydown.enter", function OrganizationsManagementComponent_Template_input_keydown_enter_71_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.onEnter("headQuarterLocation"));
    });
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275elementStart(72, "button", 35);
    i0.\u0275\u0275listener("click", function OrganizationsManagementComponent_Template_button_click_72_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.search("headQuarterLocation"));
    });
    i0.\u0275\u0275text(73, " Search");
    i0.\u0275\u0275elementEnd();
    i0.\u0275\u0275text(74, "\xA0\xA0\xA0 ");
    i0.\u0275\u0275elementStart(75, "button", 36);
    i0.\u0275\u0275listener("click", function OrganizationsManagementComponent_Template_button_click_75_listener() {
      i0.\u0275\u0275restoreView(_r1);
      return i0.\u0275\u0275resetView(ctx.reset());
    });
    i0.\u0275\u0275text(76, " Reset ");
    i0.\u0275\u0275elementEnd()()()()()()()();
  }
  if (rf & 2) {
    const orgSearch_r10 = i0.\u0275\u0275reference(48);
    const indusSearch_r11 = i0.\u0275\u0275reference(58);
    const headSearch_r12 = i0.\u0275\u0275reference(68);
    i0.\u0275\u0275advance(7);
    i0.\u0275\u0275property("ngIf", ctx.canManageOrg || ctx.isAdmin);
    i0.\u0275\u0275advance(8);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.pageSize);
    i0.\u0275\u0275advance(11);
    i0.\u0275\u0275property("ngIf", ctx.setOfCheckedId.size > 0);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzData", ctx.listOfOrg)("nzLoading", ctx.loading)("nzTotal", ctx.totalRecords)("nzPageSize", ctx.pageSize)("nzPageIndex", ctx.pageIndex)("nzShowPagination", false);
    i0.\u0275\u0275advance(3);
    i0.\u0275\u0275property("ngIf", ctx.canManageOrg || ctx.isAdmin);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("nzSortFn", true);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzVisible", ctx.isOrgSearchValue);
    i0.\u0275\u0275property("nzActive", ctx.orgSearchValue.length > 0)("nzDropdownMenu", orgSearch_r10);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzSortFn", true);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzVisible", ctx.isIndusSearchValue);
    i0.\u0275\u0275property("nzActive", ctx.indusSearchValue.length > 0)("nzDropdownMenu", indusSearch_r11);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275property("nzSortFn", true);
    i0.\u0275\u0275advance(2);
    i0.\u0275\u0275twoWayProperty("nzVisible", ctx.isHeadSearchValue);
    i0.\u0275\u0275property("nzActive", ctx.headSearchValue.length > 0)("nzDropdownMenu", headSearch_r12);
    i0.\u0275\u0275advance(3);
    i0.\u0275\u0275property("ngForOf", ctx.listOfOrg);
    i0.\u0275\u0275advance();
    i0.\u0275\u0275property("ngIf", ctx.listOfOrg.length);
    i0.\u0275\u0275advance(5);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.orgSearchValue);
    i0.\u0275\u0275advance(10);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.indusSearchValue);
    i0.\u0275\u0275advance(10);
    i0.\u0275\u0275twoWayProperty("ngModel", ctx.headSearchValue);
  }
}, dependencies: [i6.NgForOf, i6.NgIf, i7.NgSelectOption, i7.\u0275NgSelectMultipleOption, i7.DefaultValueAccessor, i7.SelectControlValueAccessor, i7.NgControlStatus, i7.NgModel, i8.NzButtonComponent, i9.\u0275NzTransitionPatchDirective, i10.NzWaveDirective, i11.NzIconDirective, i12.NzDropdownMenuComponent, i13.NzInputDirective, i14.NzTableComponent, i14.NzThAddOnComponent, i14.NzTableCellDirective, i14.NzThMeasureDirective, i14.NzTdAddOnComponent, i14.NzTheadComponent, i14.NzTbodyComponent, i14.NzTrDirective, i14.NzFilterTriggerComponent, i14.NzThSelectionComponent, i15.NzTooltipDirective, i16.NzPopconfirmDirective, FeatherIconDirective, i18.NgbPagination, i18.NgbPaginationNext, i18.NgbPaginationPrevious], styles: [`

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
/*# sourceMappingURL=organizations-management.component.css.map */`] });
var OrganizationsManagementComponent = _OrganizationsManagementComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i0.\u0275setClassDebugInfo(OrganizationsManagementComponent, { className: "OrganizationsManagementComponent", filePath: "src/app/modules/organizations/organizations-management/organizations-management.component.ts", lineNumber: 14 });
})();

// src/app/modules/organizations/add-organization/add-organization.component.ts
import { Component as Component2 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { Validators } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import { Observable } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/rxjs.js?v=ca23e844";
import * as i02 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i17 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_message.js?v=ca23e844";
import * as i2 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i4 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i5 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
import * as i62 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";
import * as i72 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@ng-bootstrap_ng-bootstrap.js?v=ca23e844";
import * as i92 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_button.js?v=ca23e844";
import * as i102 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_core_transition-patch.js?v=ca23e844";
import * as i112 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_core_wave.js?v=ca23e844";
import * as i122 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_icon.js?v=ca23e844";
import * as i132 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_upload.js?v=ca23e844";
import * as i142 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_table.js?v=ca23e844";
import * as i152 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_popconfirm.js?v=ca23e844";
import * as i162 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@ng-select_ng-select.js?v=ca23e844";
var _c0 = () => ({ standalone: true });
function AddOrganizationComponent_ng_container_26_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementContainerStart(0);
    i02.\u0275\u0275element(1, "span", 50);
    i02.\u0275\u0275elementStart(2, "div", 51);
    i02.\u0275\u0275text(3, "Upload logo");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementContainerEnd();
  }
  if (rf & 2) {
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("nzType", ctx_r1.loading ? "loading" : "plus");
  }
}
function AddOrganizationComponent_img_27_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275element(0, "img", 52);
  }
  if (rf & 2) {
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275property("src", ctx_r1.logo, i02.\u0275\u0275sanitizeUrl);
  }
}
function AddOrganizationComponent_div_34_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Please enter your organization name! ");
    i02.\u0275\u0275elementEnd();
  }
}
function AddOrganizationComponent_div_34_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 25);
    i02.\u0275\u0275template(1, AddOrganizationComponent_div_34_div_1_Template, 2, 0, "div", 22);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r1.validateForm == null ? null : (tmp_2_0 = ctx_r1.validateForm.get("orgName")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
  }
}
function AddOrganizationComponent_div_50_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Please enter your contact person! ");
    i02.\u0275\u0275elementEnd();
  }
}
function AddOrganizationComponent_div_50_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 25);
    i02.\u0275\u0275template(1, AddOrganizationComponent_div_50_div_1_Template, 2, 0, "div", 22);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r1.validateForm == null ? null : (tmp_2_0 = ctx_r1.validateForm.get("contactPerson")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
  }
}
function AddOrganizationComponent_div_58_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Please enter designation! ");
    i02.\u0275\u0275elementEnd();
  }
}
function AddOrganizationComponent_div_58_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 25);
    i02.\u0275\u0275template(1, AddOrganizationComponent_div_58_div_1_Template, 2, 0, "div", 22);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r1.validateForm == null ? null : (tmp_2_0 = ctx_r1.validateForm.get("designation")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
  }
}
function AddOrganizationComponent_div_65_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "The input is not a valid mail-ID! ");
    i02.\u0275\u0275elementEnd();
  }
}
function AddOrganizationComponent_div_65_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Please enter your valid email-ID!");
    i02.\u0275\u0275elementEnd();
  }
}
function AddOrganizationComponent_div_65_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 25);
    i02.\u0275\u0275template(1, AddOrganizationComponent_div_65_div_1_Template, 2, 0, "div", 22)(2, AddOrganizationComponent_div_65_div_2_Template, 2, 0, "div", 22);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r1.validateForm == null ? null : (tmp_2_0 = ctx_r1.validateForm.get("emailId")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["email"]);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (ctx_r1.validateForm == null ? null : (tmp_3_0 = ctx_r1.validateForm.get("emailId")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["required"]) || !ctx_r1.worngMailId);
  }
}
function AddOrganizationComponent_div_73_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, " Please enter your headquarter location! ");
    i02.\u0275\u0275elementEnd();
  }
}
function AddOrganizationComponent_div_73_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 25);
    i02.\u0275\u0275template(1, AddOrganizationComponent_div_73_div_1_Template, 2, 0, "div", 22);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r1.validateForm == null ? null : (tmp_2_0 = ctx_r1.validateForm.get("headQuarterLocation")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
  }
}
function AddOrganizationComponent_div_80_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div");
    i02.\u0275\u0275text(1, "Please select a country!");
    i02.\u0275\u0275elementEnd();
  }
}
function AddOrganizationComponent_div_80_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 25);
    i02.\u0275\u0275template(1, AddOrganizationComponent_div_80_div_1_Template, 2, 0, "div", 22);
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", (tmp_2_0 = ctx_r1.validateForm.get("country")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
  }
}
function AddOrganizationComponent_ng_template_86_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275element(0, "input", 53);
    i02.\u0275\u0275text(1);
  }
  if (rf & 2) {
    const item_r3 = ctx.item;
    const item$_r4 = ctx.item$;
    const index_r5 = ctx.index;
    i02.\u0275\u0275propertyInterpolate1("id", "item-", index_r5, "");
    i02.\u0275\u0275property("ngModel", item$_r4.selected)("ngModelOptions", i02.\u0275\u0275pureFunction0(5, _c0));
    i02.\u0275\u0275advance();
    i02.\u0275\u0275textInterpolate1(" ", item_r3.industrySectorName, " ");
  }
}
function AddOrganizationComponent_div_91_Template(rf, ctx) {
  if (rf & 1) {
    const _r6 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 54)(1, "div", 37)(2, "input", 55);
    i02.\u0275\u0275twoWayListener("ngModelChange", function AddOrganizationComponent_div_91_Template_input_ngModelChange_2_listener($event) {
      i02.\u0275\u0275restoreView(_r6);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      i02.\u0275\u0275twoWayBindingSet(ctx_r1.addIndustry, $event) || (ctx_r1.addIndustry = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(3, "button", 56);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_div_91_Template_button_click_3_listener() {
      i02.\u0275\u0275restoreView(_r6);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.addIndustrySector());
    });
    i02.\u0275\u0275element(4, "i", 41);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(5, "button", 57);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_div_91_Template_button_click_5_listener() {
      i02.\u0275\u0275restoreView(_r6);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.toggleInputBox());
    });
    i02.\u0275\u0275element(6, "i", 58);
    i02.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx_r1.addIndustry);
    i02.\u0275\u0275property("ngModelOptions", i02.\u0275\u0275pureFunction0(3, _c0));
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("disabled", !(ctx_r1.addIndustry == null ? null : ctx_r1.addIndustry.trim()));
  }
}
function AddOrganizationComponent_div_107_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275elementStart(0, "div", 59);
    i02.\u0275\u0275text(1, " Please select Turn Over! ");
    i02.\u0275\u0275elementEnd();
  }
}
function AddOrganizationComponent_div_114_Template(rf, ctx) {
  if (rf & 1) {
    const _r7 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div")(1, "div", 20)(2, "label", 60);
    i02.\u0275\u0275text(3, "Template upload");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(4, "br");
    i02.\u0275\u0275elementStart(5, "div", 61)(6, "input", 62);
    i02.\u0275\u0275listener("change", function AddOrganizationComponent_div_114_Template_input_change_6_listener($event) {
      i02.\u0275\u0275restoreView(_r7);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.onRadioChange($event));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(7, "label", 63);
    i02.\u0275\u0275text(8, "New");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(9, "div", 61)(10, "input", 64);
    i02.\u0275\u0275listener("change", function AddOrganizationComponent_div_114_Template_input_change_10_listener($event) {
      i02.\u0275\u0275restoreView(_r7);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.onRadioChange($event));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(11, "label", 65);
    i02.\u0275\u0275text(12, "Reval");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(13, "input", 66);
    i02.\u0275\u0275listener("change", function AddOrganizationComponent_div_114_Template_input_change_13_listener($event) {
      i02.\u0275\u0275restoreView(_r7);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r1.onFileChange($event));
    });
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(14, "a", 67);
    i02.\u0275\u0275text(15, " Existing Report Template ");
    i02.\u0275\u0275elementStart(16, "span", 68);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_div_114_Template_span_click_16_listener() {
      i02.\u0275\u0275restoreView(_r7);
      const ctx_r1 = i02.\u0275\u0275nextContext();
      const basicModal_r8 = i02.\u0275\u0275reference(116);
      return i02.\u0275\u0275resetView(ctx_r1.openBasicModal(basicModal_r8));
    });
    i02.\u0275\u0275text(17, " Existing Template");
    i02.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("checked", ((tmp_2_0 = ctx_r1.validateForm.get("reportType")) == null ? null : tmp_2_0.value) === "New");
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("checked", ((tmp_3_0 = ctx_r1.validateForm.get("reportType")) == null ? null : tmp_3_0.value) === "Reval");
  }
}
function AddOrganizationComponent_ng_template_115_tr_18_Template(rf, ctx) {
  if (rf & 1) {
    const _r11 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "tr")(1, "td", 82);
    i02.\u0275\u0275text(2);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(3, "td", 82);
    i02.\u0275\u0275text(4);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(5, "td");
    i02.\u0275\u0275text(6);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(7, "td", 83)(8, "a", 84);
    i02.\u0275\u0275listener("nzOnConfirm", function AddOrganizationComponent_ng_template_115_tr_18_Template_a_nzOnConfirm_8_listener() {
      const item_r12 = i02.\u0275\u0275restoreView(_r11).$implicit;
      const ctx_r1 = i02.\u0275\u0275nextContext(2);
      return i02.\u0275\u0275resetView(ctx_r1.deleteFile(item_r12._id));
    });
    i02.\u0275\u0275elementStart(9, "button", 85);
    i02.\u0275\u0275element(10, "span", 86);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275text(11, " \xA0 ");
    i02.\u0275\u0275elementStart(12, "button", 87);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_ng_template_115_tr_18_Template_button_click_12_listener() {
      const item_r12 = i02.\u0275\u0275restoreView(_r11).$implicit;
      const ctx_r1 = i02.\u0275\u0275nextContext(2);
      return i02.\u0275\u0275resetView(ctx_r1.getFileExtensionFromBase64(item_r12.reportTemplateFile, item_r12.reportTemplateName));
    });
    i02.\u0275\u0275element(13, "span", 88);
    i02.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const item_r12 = ctx.$implicit;
    const i_r13 = ctx.index;
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275textInterpolate(i_r13 + 1);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275textInterpolate(item_r12.fileNameWithoutExtension);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275textInterpolate(item_r12.fileExtension);
  }
}
function AddOrganizationComponent_ng_template_115_Template(rf, ctx) {
  if (rf & 1) {
    const _r9 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 69)(1, "h5", 70);
    i02.\u0275\u0275text(2, "Existing Template");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(3, "button", 71);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_ng_template_115_Template_button_click_3_listener() {
      const modal_r10 = i02.\u0275\u0275restoreView(_r9).$implicit;
      return i02.\u0275\u0275resetView(modal_r10.close("by: close icon"));
    });
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(4, "div", 72)(5, "div", 73)(6, "nz-table", 74)(7, "thead")(8, "tr")(9, "th", 75);
    i02.\u0275\u0275text(10, " No ");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(11, "th", 76);
    i02.\u0275\u0275text(12, " Template Name ");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(13, "th", 77);
    i02.\u0275\u0275text(14, " Extension ");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(15, "th", 78);
    i02.\u0275\u0275text(16, "Action");
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275elementStart(17, "tbody");
    i02.\u0275\u0275template(18, AddOrganizationComponent_ng_template_115_tr_18_Template, 14, 3, "tr", 79);
    i02.\u0275\u0275elementEnd()()()();
    i02.\u0275\u0275elementStart(19, "div", 80)(20, "button", 81);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_ng_template_115_Template_button_click_20_listener() {
      const modal_r10 = i02.\u0275\u0275restoreView(_r9).$implicit;
      return i02.\u0275\u0275resetView(modal_r10.close("by: close button"));
    });
    i02.\u0275\u0275text(21, "Close");
    i02.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const ctx_r1 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("nzShowPagination", false)("nzData", ctx_r1.extingTemplateListData)("nzLoading", ctx_r1.loading);
    i02.\u0275\u0275advance(12);
    i02.\u0275\u0275property("ngForOf", ctx_r1.extingTemplateListData);
  }
}
var _AddOrganizationComponent = class _AddOrganizationComponent {
  constructor(msg, fb, organizationService, router, location, toastr, modalService, loaderService) {
    this.msg = msg;
    this.fb = fb;
    this.organizationService = organizationService;
    this.router = router;
    this.location = location;
    this.toastr = toastr;
    this.modalService = modalService;
    this.loaderService = loaderService;
    this.size = "large";
    this.justifySegment = [
      "flex-start",
      "center",
      "flex-end",
      "space-between",
      "space-around",
      "space-evenly"
    ];
    this.alignSegment = ["flex-start", "center", "flex-end"];
    this.selectedJustification = 3;
    this.selectedLAlignment = 1;
    this.country = null;
    this.selectIndusSector = null;
    this.isLoading = false;
    this.countryList = [];
    this.industrySectorList = [];
    this.index = 0;
    this.empStrengthList = [];
    this.turnOverList = [];
    this.logo = "";
    this.loading = false;
    this.isActive = true;
    this.state = this.location.getState();
    this.reportTemplateFile = "";
    this.reportTemplateName = "";
    this.allReportTypeList = [
      {
        _id: "",
        reportTemplateName: "NET-SQUARE"
      }
    ];
    this.addIndustry = void 0;
    this.worngMailId = true;
    this.beforeUpload = (file, _fileList) => new Observable((observer) => {
      const isJpgOrPng = file.type === "image/jpeg" || file.type === "image/png";
      if (!isJpgOrPng) {
        this.msg.error("You can only upload JPG file!");
        observer.complete();
        return;
      }
      const isLt2M = file.size / 1024 / 1024 < 5;
      if (!isLt2M) {
        this.msg.error("Image must smaller than 5MB!");
        observer.complete();
        return;
      }
      observer?.next(isJpgOrPng && isLt2M);
      observer?.complete();
    });
    this.value = false;
    this.showInputBox = false;
    this.basicModalCloseResult = "";
    this.base64String = null;
  }
  ngOnInit() {
    this.init();
    this.ApiCalling();
    if (this.state?.data) {
      this.getReportTemplate(this.state?.data);
      this.orgDetails(this.state?.data);
    }
  }
  ApiCalling() {
    this.getCountryList();
    this.getIndustryList();
    this.getEmpCountList();
    this.getTurnOverList();
  }
  init() {
    this.validateForm = this.fb.group({
      orgName: ["", [Validators.required]],
      orgDesc: [""],
      orgShortName: [""],
      contactPerson: ["", [Validators.required]],
      designation: ["", [Validators.required]],
      emailId: ["", [Validators.email, Validators.required]],
      industrySector: [""],
      headQuarterLocation: ["", [Validators.required]],
      country: ["", [Validators.required]],
      regulationStandards: [""],
      employeeStrength: [null],
      turnOver: [null],
      reportTemplateId: ["NET-SQUARE"],
      reportType: ["New"]
    });
  }
  orgDetails(id) {
    this.loaderService.show();
    this.organizationService.GetOrgDetails(id).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.logo = response.data[0]?.logo;
          this.isActive = response.data[0]?.isActive;
          this.reportTemplateId = response.data[0]?.reportTemplateId;
          this.validateForm.patchValue(__spreadValues({}, response.data[0]));
          this.loaderService.hide();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  submitForm() {
    //if (this.validateForm.valid) {
      if (this.state.data) {
        this.updateData();
      } else {
        this.SaveData();
      }
    //} else {
    //  Object.values(this.validateForm.controls).forEach((control) => {
    //    if (control.invalid) {
    //      control.markAsDirty();
    //      control.updateValueAndValidity({ onlySelf: true });
     //   }
     // });
    //}
  }
  updateData() {
    this.loaderService.show();
    const payload = __spreadProps(__spreadValues({
      orgId: this.state.data
    }, this.validateForm.value), {
      logo: this.logo,
      isActive: this.isActive,
      reportTemplateFile: this.reportTemplateFile,
      reportTemplateName: this.reportTemplateName,
      reportTemplateId: this.reportTemplateId
    });
    this.organizationService.EditOrg(payload).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Organization Management");
          this.loaderService.hide();
          this.goBack();
        }
      },
      error: (err) => {
        if (err.error.message == "Invalid email address.") {
          this.worngMailId = err.error.status;
        } else {
          this.worngMailId = true;
        }
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  SaveData() {
    this.loaderService.show();
    const payload = __spreadProps(__spreadValues({}, this.validateForm.value), {
      isActive: this.isActive,
      logo: this.logo
    });
    this.organizationService.Add_Org(payload).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Organization Management");
          this.loaderService.hide();
          this.goBack();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  getBase64(img, callback) {
    const reader = new FileReader();
    reader.addEventListener("load", () => callback(reader.result.toString()));
    reader.readAsDataURL(img);
  }
  handleChange(info) {
    this.getBase64(info.file.originFileObj, (img) => {
      this.loading = false;
      this.logo = img;
    });
  }
  uploadTemplate(info) {
    this.getBase64(info.file.originFileObj, (img) => {
      this.loading = false;
      this.reportTemplateFile = img;
    });
  }
  // dropdown
  // Get Country data
  getCountryList() {
    this.isLoading = true;
    this.organizationService.GetCountry().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.countryList = response.data;
          this.isLoading = false;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  // industry
  getIndustryList() {
    this.isLoading = true;
    this.organizationService.GetIndustryList().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.industrySectorList = response.data;
          this.isLoading = false;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  addIndustrySector() {
    const value = this.addIndustry;
    this.loaderService.show();
    this.organizationService.GetIndustryAdd({ industrySectorName: value }).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.getIndustryList();
          this.toggleInputBox();
          this.loaderService.hide();
          this.toastr.success(response.message, "Organization Management");
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  deleteInsustry() {
    const value = this.industryId;
    this.loaderService.show();
    this.organizationService.GetIndustryDelete(value).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.getIndustryList();
          this.validateForm.get("industrySector")?.setValue("");
          this.selectIndusSector = null;
          this.loaderService.hide();
          this.toastr.success(response.message, "Organization Management");
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  // Emp
  getEmpCountList() {
    this.isLoading = true;
    this.organizationService.GetEmpCount().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.empStrengthList = response.data;
          this.validateForm.get("employeeStrength")?.setValue(this.empStrengthList[0]?.employeeStrengthValue);
          this.isLoading = false;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  // turnover
  getTurnOverList() {
    this.isLoading = true;
    this.organizationService.GetTurnOverList().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.turnOverList = response.data;
          this.validateForm.get("turnOver")?.setValue(this.turnOverList[0]?.turnOverValue);
          this.isLoading = false;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  getReportTemplate(orgId) {
    this.isLoading = true;
    this.organizationService.GetReportTypes(orgId).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.allReportTypeList = response.data;
          if (response.data.length == 0) {
            this.allReportTypeList = [
              {
                _id: "",
                reportTemplateName: "NET-SQUARE"
              }
            ];
            this.isLoading = false;
          }
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  goBack() {
    this.router.navigate(["/main/organizations_management/organizations_list"]);
  }
  onUploadError(event) {
  }
  onUploadSuccess(event) {
    this.reportTemplateFile = event[0]?.dataURL;
    this.reportTemplateName = event[0]?.name;
  }
  changed() {
    this.isActive = this.value;
  }
  onMaterialGroupChange(event) {
    this.industryId = event._id;
  }
  // Method to toggle the visibility of the input box
  toggleInputBox() {
    this.showInputBox = !this.showInputBox;
  }
  openBasicModal(content) {
    this.extingTemplateList(this.state?.data);
    this.modalService.open(content, {}).result.then((result) => {
      this.basicModalCloseResult = "Modal closed" + result;
    }).catch((res) => {
    });
  }
  extingTemplateList(orgId) {
    this.organizationService.GetExtingTemplateList(orgId).subscribe({
      next: (response) => {
        if (response.status === true) {
          const data = response.data;
          data.forEach((item) => {
            if (item.reportTemplateName) {
              const extension = item.reportTemplateName.split(".").pop();
              item.fileExtension = extension;
              const fileNameWithoutExtension = item.reportTemplateName.replace(/\.[^/.]+$/, "");
              item.fileNameWithoutExtension = fileNameWithoutExtension;
            } else {
              item.fileExtension = null;
            }
          });
          this.extingTemplateListData = data.filter((x) => x.reportTemplateName);
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  getFileExtensionFromBase64(base64String, fileName) {
    const [contentTypePart, base64Data] = base64String.split(";base64,");
    const contentType = contentTypePart.split(":")[1];
    const byteCharacters = atob(base64Data);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
      byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    const blob = new Blob([byteArray], { type: contentType });
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
  onRadioChange(event) {
    const value = event.target?.value;
    this.validateForm.get("reportType")?.setValue(value);
  }
  deleteFile(id) {
    this.organizationService.DeleteExtingTemplate(this.state?.data, id).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Organization Management");
          this.closeModal();
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Organization Management");
      }
    });
  }
  closeModal() {
    this.modalService.dismissAll();
  }
  onFileChange(event) {
    const fileInput = event.target;
    const file = event.target.files[0];
    const allowedExtensions = /(\.docx)$/i;
    if (!allowedExtensions.exec(file.name)) {
      fileInput.value = "";
      this.toastr.warning("Invalid file type. Only .docx files are allowed.");
      return;
    }
    this.reportTemplateName = file.name;
    const reader = new FileReader();
    reader.onload = this._handleReaderLoaded.bind(this);
    reader.readAsDataURL(file);
  }
  _handleReaderLoaded(event) {
    const reader = event.target;
    this.base64String = reader.result;
    this.reportTemplateFile = this.base64String;
  }
};
_AddOrganizationComponent.\u0275fac = function AddOrganizationComponent_Factory(t) {
  return new (t || _AddOrganizationComponent)(i02.\u0275\u0275directiveInject(i17.NzMessageService), i02.\u0275\u0275directiveInject(i2.NonNullableFormBuilder), i02.\u0275\u0275directiveInject(OrganizationService), i02.\u0275\u0275directiveInject(i4.Router), i02.\u0275\u0275directiveInject(i5.Location), i02.\u0275\u0275directiveInject(i62.ToastrService), i02.\u0275\u0275directiveInject(i72.NgbModal), i02.\u0275\u0275directiveInject(LoadingService));
};
_AddOrganizationComponent.\u0275cmp = /* @__PURE__ */ i02.\u0275\u0275defineComponent({ type: _AddOrganizationComponent, selectors: [["app-add-organization"]], decls: 117, vars: 31, consts: [["basicModal", ""], [1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "page-breadcrumb", "m-0"], [1, "breadcrumb", "mb-0"], [1, "breadcrumb-item"], ["routerLink", "/main/organizations_management/organizations_list"], ["aria-current", "page", 1, "breadcrumb-item", "active"], [1, "form-check", "form-switch", "button-container"], ["type", "checkbox", "role", "switch", "id", "flexSwitchCheckChecked", 1, "form-check-input", 3, "ngModelChange", "ngModel"], ["for", "flexSwitchCheckChecked", 1, "form-check-label"], [1, "button-container"], [1, "btn", "btn-secondary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], [1, "btn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], [1, "row"], [1, "col-md-12", "grid-margin", "stretch-card"], [1, "card"], [1, "card-body"], [1, "forms-sample", 3, "formGroup"], [1, "mb-3"], ["nzName", "avatar", "nzListType", "picture-card", 1, "avatar-uploader", 3, "nzChange", "nzShowUploadList", "nzBeforeUpload"], [4, "ngIf"], ["class", "w-100 h-100 rounded-circle", "alt", "Logo", 3, "src", 4, "ngIf"], ["required", "", 1, "form-label"], [1, "text-danger"], ["formControlName", "orgName", "placeholder", "Enter organization name", "id", "orgName", "required", "", 1, "form-control"], ["class", "text-danger", 4, "ngIf"], [1, "form-label"], ["formControlName", "orgShortName", "id", "orgShortName", "placeholder", "Enter organization short name", 1, "form-control"], ["formControlName", "orgDesc", "id", "orgDesc", "placeholder", "Enter organization description", "rows", "3", 1, "form-control"], [1, "col"], ["formControlName", "contactPerson", "id", "contactPerson", "placeholder", "Enter contact person", "required", "", 1, "form-control"], ["formControlName", "designation", "id", "designation", "placeholder", "Enter designation", "required", "", 1, "form-control"], ["formControlName", "emailId", "id", "emailId", "placeholder", "Enter your Email-ID", "required", "", 1, "form-control"], ["formControlName", "headQuarterLocation", "id", "headQuarterLocation", "placeholder", "Enter headquarter location", "required", "", 1, "form-control"], ["id", "countryList", "bindLabel", "name", "bindValue", "name", "placeholder", "Select Country", "formControlName", "country", 3, "ngModelChange", "items", "ngModel", "loading"], [1, "d-flex", "align-items-center"], ["bindLabel", "industrySectorName", "bindValue", "industrySectorName", "formControlName", "industrySector", "id", "industrySector", "placeholder", "Select industry sector", 1, "select-flex", 3, "ngModelChange", "change", "items", "closeOnSelect", "ngModel", "loading"], ["ng-option-tmp", ""], [1, "btn", "btn-outline-primary", "me-1", 3, "click"], [1, "feather", "icon-plus"], [1, "btn", "btn-danger", 3, "click", "disabled"], [1, "feather", "icon-trash"], ["class", "mb-3 pb-1", 4, "ngIf"], ["formControlName", "regulationStandards", "id", "regulationStandards", "placeholder", "Enter regular standard", 1, "form-control"], ["bindLabel", "employeeStrengthValue", "bindValue", "employeeStrengthValue", "placeholder", "Select a employee strength", "formControlName", "employeeStrength", "id", "employeeStrength", 3, "items", "loading"], ["bindLabel", "turnOverValue", "bindValue", "turnOverValue", "placeholder", "Select a turn over", "formControlName", "turnOver", "id", "turnOverList", 3, "items", "loading"], ["class", "invalid-feedback", 4, "ngIf"], ["bindLabel", "reportTemplateName", "bindValue", "_id", "placeholder", "Select a report template", "formControlName", "reportTemplateId", 3, "ngModelChange", "items", "ngModel", "loading"], ["nz-icon", "", 1, "upload-icon", 3, "nzType"], [1, "ant-upload-text"], ["alt", "Logo", 1, "w-100", "h-100", "rounded-circle", 3, "src"], ["type", "checkbox", 3, "id", "ngModel", "ngModelOptions"], [1, "mb-3", "pb-1"], ["id", "addIndustrySector", "placeholder", "Add New Industry Sector", 1, "form-control", "select-flex", 3, "ngModelChange", "ngModel", "ngModelOptions"], ["id", "btnAddIndustrySector", 1, "btn", "btn-outline-primary", "me-1", 3, "click", "disabled"], [1, "btn", "btn-secondary", 3, "click"], [1, "feather", "icon-x"], [1, "invalid-feedback"], ["for", "formFile", 1, "form-label"], [1, "form-check", "form-check-inline"], ["type", "radio", "id", "New", "value", "New", "formControlName", "reportType", 1, "form-check-input", 3, "change", "checked"], ["for", "New", 1, "form-check-label"], ["type", "radio", "id", "Reval", "value", "Reval", "formControlName", "reportType", 1, "form-check-input", 3, "change", "checked"], ["for", "Reval", 1, "form-check-label"], ["type", "file", "id", "formFile", "accept", ".docx", 1, "form-control", 3, "change"], [1, "sidebar-brand", "nobleui-logo"], [3, "click"], [1, "modal-header"], ["id", "exampleModalLabel", 1, "modal-title"], ["type", "button", "id", "btnExistingTemplate", "aria-label", "Close", 1, "btn-close", 3, "click"], [1, "modal-body"], [1, "table-responsive"], ["nzShowSizeChanger", "", 3, "nzShowPagination", "nzData", "nzLoading"], ["id", "1", "nzColumnKey", "orgName"], ["id", "2", "nzColumnKey", "TemplateName"], ["id", "3", "nzColumnKey", "headQuarterLocation"], ["id", "5", 1, "text-center"], [4, "ngFor", "ngForOf"], [1, "modal-footer"], ["id", "orgBtn", "type", "button", 1, "btn", "btn-secondary", "btn-sm", "m-1", 3, "click"], [1, "ellipsis"], [1, "text-center", "action"], ["nz-popconfirm", "", "nzPopconfirmTitle", "Sure to delete?", 3, "nzOnConfirm"], ["nz-button", "", "nzType", "primary", "nzShape", "circle"], ["nz-icon", "", "nzType", "delete", "nzTheme", "outline"], ["nz-button", "", "nzType", "primary", "id", "downloadTemplate", "nzShape", "circle", 3, "click"], ["nz-icon", "", "nzType", "download", "nzTheme", "outline"]], template: function AddOrganizationComponent_Template(rf, ctx) {
  if (rf & 1) {
    const _r1 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 1)(1, "div", 2)(2, "div", 3)(3, "nav", 4)(4, "ol", 5)(5, "li", 6)(6, "a", 7);
    i02.\u0275\u0275text(7, "Organization");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(8, "li", 8);
    i02.\u0275\u0275text(9);
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275elementStart(10, "div", 9)(11, "input", 10);
    i02.\u0275\u0275twoWayListener("ngModelChange", function AddOrganizationComponent_Template_input_ngModelChange_11_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.isActive, $event) || (ctx.isActive = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(12, "label", 11);
    i02.\u0275\u0275text(13, "Active");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(14, "div", 12)(15, "button", 13);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_Template_button_click_15_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.goBack());
    });
    i02.\u0275\u0275text(16, "Back");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(17, "button", 14);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_Template_button_click_17_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.submitForm());
    });
    i02.\u0275\u0275text(18, " Submit");
    i02.\u0275\u0275elementEnd()()()()();
    i02.\u0275\u0275elementStart(19, "div", 15)(20, "div", 16)(21, "div", 17)(22, "div", 18)(23, "form", 19)(24, "div", 20)(25, "nz-upload", 21);
    i02.\u0275\u0275listener("nzChange", function AddOrganizationComponent_Template_nz_upload_nzChange_25_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.handleChange($event));
    });
    i02.\u0275\u0275template(26, AddOrganizationComponent_ng_container_26_Template, 4, 1, "ng-container", 22)(27, AddOrganizationComponent_img_27_Template, 1, 1, "img", 23);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(28, "div", 20)(29, "label", 24);
    i02.\u0275\u0275text(30, "Organization Name");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(31, "span", 25);
    i02.\u0275\u0275text(32, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(33, "input", 26);
    i02.\u0275\u0275template(34, AddOrganizationComponent_div_34_Template, 2, 1, "div", 27);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(35, "div", 20)(36, "label", 28);
    i02.\u0275\u0275text(37, "Organization Short Name");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(38, "input", 29);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(39, "div", 20)(40, "label", 28);
    i02.\u0275\u0275text(41, "Organization Description");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(42, "textarea", 30);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(43, "div", 20)(44, "div", 31)(45, "label", 28);
    i02.\u0275\u0275text(46, "Contact Person");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(47, "span", 25);
    i02.\u0275\u0275text(48, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(49, "input", 32);
    i02.\u0275\u0275template(50, AddOrganizationComponent_div_50_Template, 2, 1, "div", 27);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(51, "div", 20)(52, "div", 31)(53, "label", 28);
    i02.\u0275\u0275text(54, "Designation");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(55, "span", 25);
    i02.\u0275\u0275text(56, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(57, "input", 33);
    i02.\u0275\u0275template(58, AddOrganizationComponent_div_58_Template, 2, 1, "div", 27);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(59, "div", 20)(60, "label", 28);
    i02.\u0275\u0275text(61, "Email ID");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(62, "span", 25);
    i02.\u0275\u0275text(63, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(64, "input", 34);
    i02.\u0275\u0275template(65, AddOrganizationComponent_div_65_Template, 3, 2, "div", 27);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(66, "div", 20)(67, "div", 31)(68, "label", 28);
    i02.\u0275\u0275text(69, "Headquarter Location");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(70, "span", 25);
    i02.\u0275\u0275text(71, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(72, "input", 35);
    i02.\u0275\u0275template(73, AddOrganizationComponent_div_73_Template, 2, 1, "div", 27);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(74, "div", 20)(75, "label", 28);
    i02.\u0275\u0275text(76, "Country");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(77, "span", 25);
    i02.\u0275\u0275text(78, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(79, "ng-select", 36);
    i02.\u0275\u0275twoWayListener("ngModelChange", function AddOrganizationComponent_Template_ng_select_ngModelChange_79_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.country, $event) || (ctx.country = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275template(80, AddOrganizationComponent_div_80_Template, 2, 1, "div", 27);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(81, "div", 20)(82, "label", 28);
    i02.\u0275\u0275text(83, "Industry Sector");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(84, "div", 37)(85, "ng-select", 38);
    i02.\u0275\u0275twoWayListener("ngModelChange", function AddOrganizationComponent_Template_ng_select_ngModelChange_85_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.selectIndusSector, $event) || (ctx.selectIndusSector = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275listener("change", function AddOrganizationComponent_Template_ng_select_change_85_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onMaterialGroupChange($event));
    });
    i02.\u0275\u0275template(86, AddOrganizationComponent_ng_template_86_Template, 2, 6, "ng-template", 39);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(87, "button", 40);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_Template_button_click_87_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.toggleInputBox());
    });
    i02.\u0275\u0275element(88, "i", 41);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(89, "button", 42);
    i02.\u0275\u0275listener("click", function AddOrganizationComponent_Template_button_click_89_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.deleteInsustry());
    });
    i02.\u0275\u0275element(90, "i", 43);
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275template(91, AddOrganizationComponent_div_91_Template, 7, 4, "div", 44);
    i02.\u0275\u0275elementStart(92, "div", 20)(93, "label", 28);
    i02.\u0275\u0275text(94, "Regular Standard");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(95, "input", 45);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(96, "div", 20)(97, "div", 31)(98, "label", 28);
    i02.\u0275\u0275text(99, "Employee Strength");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(100, "ng-select", 46);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(101, "div", 20)(102, "label", 28);
    i02.\u0275\u0275text(103, "Turn Over (in $)");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(104, "span", 25);
    i02.\u0275\u0275text(105, " *");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275element(106, "ng-select", 47);
    i02.\u0275\u0275template(107, AddOrganizationComponent_div_107_Template, 2, 0, "div", 48);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(108, "div", 20)(109, "div", 31)(110, "label", 28);
    i02.\u0275\u0275text(111, "Report Template");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(112, "ng-select", 49);
    i02.\u0275\u0275twoWayListener("ngModelChange", function AddOrganizationComponent_Template_ng_select_ngModelChange_112_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.reportTemplateId, $event) || (ctx.reportTemplateId = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275elementStart(113, "div", 20);
    i02.\u0275\u0275template(114, AddOrganizationComponent_div_114_Template, 18, 2, "div", 22);
    i02.\u0275\u0275elementEnd()()()()()();
    i02.\u0275\u0275template(115, AddOrganizationComponent_ng_template_115_Template, 22, 4, "ng-template", null, 0, i02.\u0275\u0275templateRefExtractor);
  }
  if (rf & 2) {
    let tmp_8_0;
    let tmp_9_0;
    let tmp_10_0;
    let tmp_11_0;
    let tmp_12_0;
    let tmp_16_0;
    let tmp_27_0;
    i02.\u0275\u0275advance(9);
    i02.\u0275\u0275textInterpolate1(" ", (ctx.state == null ? null : ctx.state.data) ? "Update" : "New", " Organization ");
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.isActive);
    i02.\u0275\u0275advance(12);
    i02.\u0275\u0275property("formGroup", ctx.validateForm);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("nzShowUploadList", false)("nzBeforeUpload", ctx.beforeUpload);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", !ctx.logo);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx.logo);
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275property("ngIf", (ctx.validateForm == null ? null : (tmp_8_0 = ctx.validateForm.get("orgName")) == null ? null : tmp_8_0.dirty) && (ctx.validateForm == null ? null : (tmp_8_0 = ctx.validateForm.get("orgName")) == null ? null : tmp_8_0.errors) || (ctx.validateForm == null ? null : (tmp_8_0 = ctx.validateForm.get("orgName")) == null ? null : tmp_8_0.touched));
    i02.\u0275\u0275advance(16);
    i02.\u0275\u0275property("ngIf", (ctx.validateForm == null ? null : (tmp_9_0 = ctx.validateForm.get("contactPerson")) == null ? null : tmp_9_0.dirty) && (ctx.validateForm == null ? null : (tmp_9_0 = ctx.validateForm.get("contactPerson")) == null ? null : tmp_9_0.errors) || (ctx.validateForm == null ? null : (tmp_9_0 = ctx.validateForm.get("contactPerson")) == null ? null : tmp_9_0.touched));
    i02.\u0275\u0275advance(8);
    i02.\u0275\u0275property("ngIf", (ctx.validateForm == null ? null : (tmp_10_0 = ctx.validateForm.get("designation")) == null ? null : tmp_10_0.dirty) && (ctx.validateForm == null ? null : (tmp_10_0 = ctx.validateForm.get("designation")) == null ? null : tmp_10_0.errors) || (ctx.validateForm == null ? null : (tmp_10_0 = ctx.validateForm.get("designation")) == null ? null : tmp_10_0.touched));
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275property("ngIf", (ctx.validateForm == null ? null : (tmp_11_0 = ctx.validateForm.get("emailId")) == null ? null : tmp_11_0.dirty) && (ctx.validateForm == null ? null : (tmp_11_0 = ctx.validateForm.get("emailId")) == null ? null : tmp_11_0.errors) || !ctx.worngMailId);
    i02.\u0275\u0275advance(8);
    i02.\u0275\u0275property("ngIf", (ctx.validateForm == null ? null : (tmp_12_0 = ctx.validateForm.get("headQuarterLocation")) == null ? null : tmp_12_0.dirty) && (ctx.validateForm == null ? null : (tmp_12_0 = ctx.validateForm.get("headQuarterLocation")) == null ? null : tmp_12_0.errors) || (ctx.validateForm == null ? null : (tmp_12_0 = ctx.validateForm.get("headQuarterLocation")) == null ? null : tmp_12_0.touched));
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("items", ctx.countryList);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.country);
    i02.\u0275\u0275property("loading", ctx.isLoading);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ((tmp_16_0 = ctx.validateForm.get("country")) == null ? null : tmp_16_0.invalid) && (((tmp_16_0 = ctx.validateForm.get("country")) == null ? null : tmp_16_0.dirty) || ((tmp_16_0 = ctx.validateForm.get("country")) == null ? null : tmp_16_0.touched)));
    i02.\u0275\u0275advance(5);
    i02.\u0275\u0275property("items", ctx.industrySectorList)("closeOnSelect", false);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.selectIndusSector);
    i02.\u0275\u0275property("loading", ctx.isLoading);
    i02.\u0275\u0275advance(4);
    i02.\u0275\u0275property("disabled", !(ctx.industryId == null ? null : ctx.industryId.trim()));
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("ngIf", ctx.showInputBox);
    i02.\u0275\u0275advance(9);
    i02.\u0275\u0275property("items", ctx.empStrengthList)("loading", ctx.isLoading);
    i02.\u0275\u0275advance(6);
    i02.\u0275\u0275property("items", ctx.turnOverList)("loading", ctx.isLoading);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ((tmp_27_0 = ctx.validateForm.get("turnOver")) == null ? null : tmp_27_0.invalid) && (((tmp_27_0 = ctx.validateForm.get("turnOver")) == null ? null : tmp_27_0.dirty) || ((tmp_27_0 = ctx.validateForm.get("turnOver")) == null ? null : tmp_27_0.touched)));
    i02.\u0275\u0275advance(5);
    i02.\u0275\u0275property("items", ctx.allReportTypeList);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.reportTemplateId);
    i02.\u0275\u0275property("loading", ctx.isLoading);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("ngIf", ctx.state == null ? null : ctx.state.data);
  }
}, dependencies: [i5.NgForOf, i5.NgIf, i4.RouterLink, i2.\u0275NgNoValidate, i2.DefaultValueAccessor, i2.CheckboxControlValueAccessor, i2.RadioControlValueAccessor, i2.NgControlStatus, i2.NgControlStatusGroup, i2.RequiredValidator, i2.NgModel, i2.FormGroupDirective, i2.FormControlName, i92.NzButtonComponent, i102.\u0275NzTransitionPatchDirective, i112.NzWaveDirective, i122.NzIconDirective, i132.NzUploadComponent, i142.NzTableComponent, i142.NzThAddOnComponent, i142.NzTableCellDirective, i142.NzThMeasureDirective, i142.NzTheadComponent, i142.NzTbodyComponent, i142.NzTrDirective, i152.NzPopconfirmDirective, i162.NgSelectComponent, i162.NgOptionTemplateDirective], styles: ["\n\n[_nghost-%COMP%]     .avatar-uploader > .ant-upload {\n  width: 128px;\n  height: 128px;\n}\n[_nghost-%COMP%]     .ant-upload.ant-upload-select-picture-card {\n  border-radius: 50%;\n}\n[_nghost-%COMP%]     .ant-upload.ant-upload-select-picture-card:hover {\n  border-color: #515acc;\n}\n.dropzone.dz-clickable[_ngcontent-%COMP%]   .dz-message[_ngcontent-%COMP%] {\n  margin-top: 38px;\n}\n.dropzone[_ngcontent-%COMP%] {\n  min-height: 100px;\n  padding: 0;\n  width: 39%;\n  border: 1px solid #e9ecef;\n  border-radius: 0.25rem;\n}\n.js[_ngcontent-%COMP%] {\n  justify-content: space-between;\n}\n.nobleui-logo[_ngcontent-%COMP%] {\n  font-weight: 400;\n  font-size: 14px;\n  color: black !important;\n}\n.icon[_ngcontent-%COMP%] {\n  cursor: pointer;\n}\n  .ng-dropdown-panel .ng-dropdown-panel-items .ng-option, .ng-dropdown-panel[_ngcontent-%COMP%]   .ng-dropdown-panel-items[_ngcontent-%COMP%]   .ng-optgroup[_ngcontent-%COMP%] {\n  background-color: #fff;\n  color: var(--bs-body-color);\n}\n.select-flex[_ngcontent-%COMP%] {\n  flex-grow: 1;\n  margin-right: 10px;\n}\n/*# sourceMappingURL=add-organization.component.css.map */"] });
var AddOrganizationComponent = _AddOrganizationComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i02.\u0275setClassDebugInfo(AddOrganizationComponent, { className: "AddOrganizationComponent", filePath: "src/app/modules/organizations/add-organization/add-organization.component.ts", lineNumber: 25 });
})();

// src/app/modules/organizations/organizations-routing.module.ts
import * as i03 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
var routes = [
  {
    path: "organizations_list",
    component: OrganizationsManagementComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "add_organizations",
    component: AddOrganizationComponent,
    canActivate: [AuthGuard]
  }
];
var _OrganizationsRoutingModule = class _OrganizationsRoutingModule {
};
_OrganizationsRoutingModule.\u0275fac = function OrganizationsRoutingModule_Factory(t) {
  return new (t || _OrganizationsRoutingModule)();
};
_OrganizationsRoutingModule.\u0275mod = /* @__PURE__ */ i03.\u0275\u0275defineNgModule({ type: _OrganizationsRoutingModule });
_OrganizationsRoutingModule.\u0275inj = /* @__PURE__ */ i03.\u0275\u0275defineInjector({ imports: [RouterModule.forChild(routes), RouterModule] });
var OrganizationsRoutingModule = _OrganizationsRoutingModule;

// src/app/modules/organizations/organizations.module.ts
import * as i04 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
var _OrganizationsModule = class _OrganizationsModule {
};
_OrganizationsModule.\u0275fac = function OrganizationsModule_Factory(t) {
  return new (t || _OrganizationsModule)();
};
_OrganizationsModule.\u0275mod = /* @__PURE__ */ i04.\u0275\u0275defineNgModule({ type: _OrganizationsModule });
_OrganizationsModule.\u0275inj = /* @__PURE__ */ i04.\u0275\u0275defineInjector({ imports: [
  CommonModule,
  OrganizationsRoutingModule,
  SharedModule
] });
var OrganizationsModule = _OrganizationsModule;
export {
  OrganizationsModule
};
