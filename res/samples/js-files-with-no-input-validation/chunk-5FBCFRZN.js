import {
  SettingsService
} from "/chunk-H7EVQOP5.js";
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
  urlMap
} from "/chunk-2CBLJUUC.js";

// src/app/modules/projects/projects.module.ts
import { NgModule as NgModule2 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { CommonModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";

// src/app/modules/projects/projects-routing.module.ts
import { NgModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { RouterModule } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";

// src/app/modules/projects/projects-lists/projects-lists.component.ts
import { Component } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i02 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i12 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i2 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";

// src/app/services/projects.service.ts
import { HttpParams } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common_http.js?v=ca23e844";
import { Injectable } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i0 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i1 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common_http.js?v=ca23e844";
var _ProjectsService = class _ProjectsService {
  constructor(http) {
    this.http = http;
  }
  GetProjectList(pageIndex, pageSize, search, sortData) {
    let params = new HttpParams();
    params = params.set("page", pageIndex);
    params = params.set("limit", pageSize);
    if (search?.length !== 0) {
      if (search.key && search.value) {
        params = params.set("type", "search");
        params = params.set("key", search.key);
        params = params.set("value", search.value);
      }
    }
    if (sortData) {
      if (sortData.key && sortData.value) {
        params = params.set("type", "sort");
        params = params.set("key", sortData.key);
        params = params.set("value", sortData.value);
      }
    }
    return this.http.get(`${urlMap.PROJECTS_LIST}?`, { params });
  }
  GetOrgProjectList(id, pageIndex, pageSize, search, sortData) {
    let params = new HttpParams();
    params = params.set("page", pageIndex);
    params = params.set("limit", pageSize);
    if (search?.length !== 0) {
      if (search.key && search.value) {
        params = params.set("type", "search");
        params = params.set("key", search.key);
        params = params.set("value", search.value);
      }
    }
    if (sortData) {
      if (sortData.key && sortData.value) {
        params = params.set("type", "sort");
        params = params.set("key", sortData.key);
        params = params.set("value", sortData.value);
      }
    }
    return this.http.get(`${urlMap.PROJECTS_ORG_LIST}/${id}?`, { params });
  }
  ProjectAdd(payload) {
    return this.http.post(urlMap.PROJECT_ADD, payload);
  }
  ProjectEdit(payload) {
    return this.http.put(urlMap.PROJECT_EDIT, payload);
  }
  ProjectDetails(id) {
    return this.http.get(`${urlMap.PROJECT_DETAILS}/${id}`);
  }
  ProjectDelete(id) {
    return this.http.post(urlMap.PROJECT_DELETE, id);
  }
  GetNetwork() {
    return this.http.get(`${urlMap.NETWORK}`);
  }
};
_ProjectsService.\u0275fac = function ProjectsService_Factory(t) {
  return new (t || _ProjectsService)(i0.\u0275\u0275inject(i1.HttpClient));
};
_ProjectsService.\u0275prov = /* @__PURE__ */ i0.\u0275\u0275defineInjectable({ token: _ProjectsService, factory: _ProjectsService.\u0275fac, providedIn: "root" });
var ProjectsService = _ProjectsService;

// src/app/modules/projects/projects-lists/projects-lists.component.ts
import * as i4 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
import * as i7 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i8 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_button.js?v=ca23e844";
import * as i9 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_core_transition-patch.js?v=ca23e844";
import * as i10 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_core_wave.js?v=ca23e844";
import * as i11 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_icon.js?v=ca23e844";
import * as i122 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_dropdown.js?v=ca23e844";
import * as i13 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_input.js?v=ca23e844";
import * as i14 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_table.js?v=ca23e844";
import * as i15 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_tooltip.js?v=ca23e844";
import * as i16 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ng-zorro-antd_popconfirm.js?v=ca23e844";
import * as i18 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@ng-bootstrap_ng-bootstrap.js?v=ca23e844";
function ProjectsListsComponent_button_7_Template(rf, ctx) {
  if (rf & 1) {
    const _r2 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "button", 50);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_button_7_Template_button_click_0_listener() {
      i02.\u0275\u0275restoreView(_r2);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.addRow());
    });
    i02.\u0275\u0275element(1, "i", 51);
    i02.\u0275\u0275text(2, " Add Project ");
    i02.\u0275\u0275elementEnd();
  }
}
function ProjectsListsComponent_a_26_Template(rf, ctx) {
  if (rf & 1) {
    const _r4 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "a", 52);
    i02.\u0275\u0275listener("nzOnConfirm", function ProjectsListsComponent_a_26_Template_a_nzOnConfirm_0_listener() {
      i02.\u0275\u0275restoreView(_r4);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.projectDelete());
    });
    i02.\u0275\u0275elementStart(1, "button", 53);
    i02.\u0275\u0275element(2, "span", 54);
    i02.\u0275\u0275elementEnd()();
  }
  if (rf & 2) {
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("nzTooltipColor", ctx_r2.color);
  }
}
function ProjectsListsComponent_th_31_Template(rf, ctx) {
  if (rf & 1) {
    const _r5 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "th", 55);
    i02.\u0275\u0275listener("nzCheckedChange", function ProjectsListsComponent_th_31_Template_th_nzCheckedChange_0_listener($event) {
      i02.\u0275\u0275restoreView(_r5);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.onAllChecked($event));
    });
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275property("nzChecked", ctx_r2.listOfprojects.length ? ctx_r2.checked : false)("nzIndeterminate", ctx_r2.indeterminate);
  }
}
function ProjectsListsComponent_tr_53_td_1_Template(rf, ctx) {
  if (rf & 1) {
    const _r8 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "td", 63);
    i02.\u0275\u0275listener("nzCheckedChange", function ProjectsListsComponent_tr_53_td_1_Template_td_nzCheckedChange_0_listener($event) {
      i02.\u0275\u0275restoreView(_r8);
      const data_r7 = i02.\u0275\u0275nextContext().$implicit;
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.onItemChecked(data_r7._id, $event));
    });
    i02.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    const data_r7 = i02.\u0275\u0275nextContext().$implicit;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275property("nzChecked", ctx_r2.setOfCheckedId.has(data_r7._id))("nzLabel", data_r7.name);
  }
}
function ProjectsListsComponent_tr_53_Template(rf, ctx) {
  if (rf & 1) {
    const _r6 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "tr", 56);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_tr_53_Template_tr_click_0_listener() {
      const data_r7 = i02.\u0275\u0275restoreView(_r6).$implicit;
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView((ctx_r2.canManageProject || ctx_r2.isAdmin) && ctx_r2.editRow(data_r7._id));
    });
    i02.\u0275\u0275template(1, ProjectsListsComponent_tr_53_td_1_Template, 1, 2, "td", 57);
    i02.\u0275\u0275elementStart(2, "td", 58);
    i02.\u0275\u0275text(3);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(4, "td", 58);
    i02.\u0275\u0275text(5);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(6, "td", 59);
    i02.\u0275\u0275text(7);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(8, "td");
    i02.\u0275\u0275text(9);
    i02.\u0275\u0275pipe(10, "date");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(11, "td", 60);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_tr_53_Template_td_click_11_listener() {
      const data_r7 = i02.\u0275\u0275restoreView(_r6).$implicit;
      const ctx_r2 = i02.\u0275\u0275nextContext();
      return i02.\u0275\u0275resetView(ctx_r2.getProjectTestList(data_r7._id));
    });
    i02.\u0275\u0275text(12);
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(13, "td")(14, "div", 61);
    i02.\u0275\u0275element(15, "input", 62);
    i02.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const data_r7 = ctx.$implicit;
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx_r2.canManageProject || ctx_r2.isAdmin);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("nzTooltipTitle", data_r7 == null ? null : data_r7.projectName)("nzTooltipColor", ctx_r2.color);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275textInterpolate1(" ", data_r7.projectName, " ");
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("nzTooltipTitle", data_r7 == null ? null : data_r7.nwPlacementName)("nzTooltipColor", ctx_r2.color);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275textInterpolate1(" ", data_r7.nwPlacementName, " ");
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("nzTooltipTitle", data_r7 == null ? null : data_r7.orgName)("nzTooltipColor", ctx_r2.color);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275textInterpolate1(" ", data_r7 == null ? null : data_r7.orgName, " ");
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275textInterpolate1(" ", i02.\u0275\u0275pipeBind2(10, 13, data_r7.creationDate, "dd/MM/yyyy"), " ");
    i02.\u0275\u0275advance(3);
    i02.\u0275\u0275textInterpolate1(" ", data_r7.totalTests, " ");
    i02.\u0275\u0275advance(3);
    i02.\u0275\u0275property("checked", data_r7.isSensitive);
  }
}
function ProjectsListsComponent_div_54_ng_template_6_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275text(0, "Prev");
  }
}
function ProjectsListsComponent_div_54_ng_template_7_Template(rf, ctx) {
  if (rf & 1) {
    i02.\u0275\u0275text(0, "Next");
  }
}
function ProjectsListsComponent_div_54_Template(rf, ctx) {
  if (rf & 1) {
    const _r9 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 11)(1, "div", 64)(2, "div", 65);
    i02.\u0275\u0275text(3);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(4, "div", 66)(5, "ngb-pagination", 67);
    i02.\u0275\u0275twoWayListener("pageChange", function ProjectsListsComponent_div_54_Template_ngb_pagination_pageChange_5_listener($event) {
      i02.\u0275\u0275restoreView(_r9);
      const ctx_r2 = i02.\u0275\u0275nextContext();
      i02.\u0275\u0275twoWayBindingSet(ctx_r2.pageIndex, $event) || (ctx_r2.pageIndex = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275template(6, ProjectsListsComponent_div_54_ng_template_6_Template, 1, 0, "ng-template", 68)(7, ProjectsListsComponent_div_54_ng_template_7_Template, 1, 0, "ng-template", 69);
    i02.\u0275\u0275elementEnd()()();
  }
  if (rf & 2) {
    const ctx_r2 = i02.\u0275\u0275nextContext();
    i02.\u0275\u0275advance(3);
    i02.\u0275\u0275textInterpolate1(" ", ctx_r2.currentPageRange, " ");
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("collectionSize", ctx_r2.totalRecords);
    i02.\u0275\u0275twoWayProperty("page", ctx_r2.pageIndex);
    i02.\u0275\u0275property("maxSize", 5)("rotate", true)("ellipses", false)("boundaryLinks", false);
  }
}
var _ProjectsListsComponent = class _ProjectsListsComponent {
  constructor(router, toastr, projectsService, location, userService, loaderService) {
    this.router = router;
    this.toastr = toastr;
    this.projectsService = projectsService;
    this.location = location;
    this.userService = userService;
    this.loaderService = loaderService;
    this.totalRecords = 0;
    this.totalPages = 1;
    this.loading = false;
    this.pageSize = 10;
    this.pageIndex = 1;
    this.onKeyString = "";
    this.currentPageRange = "";
    this.proSearchValue = "";
    this.isproSearchValue = false;
    this.orgSearchValue = [];
    this.nwPlacementNameSearchValue = [];
    this.creationDateSearchValue = [];
    this.isOrgSearchValue = false;
    this.isnwPlacementNameSearchValue = false;
    this.iscreationDateSearchValue = false;
    this.listOfprojects = [];
    this.state = this.location.getState();
    this.color = "black";
    this.canManageProject = false;
    this.isAdmin = false;
    this.checked = false;
    this.indeterminate = false;
    this.listOfCurrentPageData = [];
    this.setOfCheckedId = /* @__PURE__ */ new Set();
  }
  ngOnInit() {
    this.orgId = this.state?.data;
    this.accsssData();
  }
  accsssData() {
    const getUserAccessData = this.userService.getUserAccessData();
    this.canManageProject = getUserAccessData[0]?.canManageProject;
  }
  loadDataFromServer(pageIndex, pageSize, sortField, sortOrder, search) {
    this.loading = true;
    this.projectsService.GetProjectList(pageIndex, pageSize, search, sortOrder).subscribe({
      next: (response) => {
        if (response.status === true) {
          if (!response.data.length) {
            this.listOfprojects = [];
            this.loading = false;
            return;
          }
          const data = response.data;
          this.listOfprojects = data;
          this.totalRecords = response.totalRecords;
          this.isAdmin = response?.isAdmin;
          this.onCurrentPageDataChange(this.listOfprojects);
          this.calculatePageRange();
          this.loading = false;
        }
      },
      error: (err) => {
        this.loading = false;
        return this.toastr.error(err.error.message, "Projects Management");
      }
    });
  }
  projectByOrg(id, pageIndex, pageSize, sortField, sortOrder, search) {
    this.loading = true;
    this.projectsService.GetOrgProjectList(this.orgId, pageIndex, pageSize, search, sortOrder).subscribe({
      next: (response) => {
        if (response.status === true) {
          const data = response.data;
          this.listOfprojects = data;
          this.onCurrentPageDataChange(this.listOfprojects);
          this.calculatePageRange();
          this.loading = false;
        }
      },
      error: (err) => {
        this.loading = false;
        return this.toastr.error(err.error.message, "Projects Management");
      }
    });
  }
  onQueryParamsChange(params) {
    const { pageSize, pageIndex, sort, filter } = params;
    const currentSort = sort.find((item) => item.value !== null);
    const sortField = currentSort && currentSort.key || null;
    const sortOrder = currentSort && currentSort.value || null;
    const sortingData = { type: "sort", key: sortField, value: sortOrder };
    if (this.orgId) {
      this.projectByOrg(this.orgId, pageIndex, pageSize, sortField, sortingData, filter);
    } else {
      this.loadDataFromServer(pageIndex, pageSize, sortField, sortingData, filter);
    }
  }
  resetPageIndex() {
    this.pageIndex = 1;
  }
  getProjectTestList(_id) {
    this.toastr.success("Test list", "");
    this.router.navigate(["/main/tests_management/test_list"], { state: { projectId: _id } });
  }
  reset() {
    this.orgSearchValue = "";
    this.nwPlacementNameSearchValue = "";
    this.creationDateSearchValue = "";
    this.proSearchValue = "";
    this.isproSearchValue = false;
    this.isnwPlacementNameSearchValue = false;
    this.isOrgSearchValue = false;
    this.iscreationDateSearchValue = false;
    this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, []);
  }
  onKeyUp(columName, event) {
    this.onKeyString += event.key;
    setTimeout(() => {
      this.search(columName, this.onKeyString);
    }, 1e3);
  }
  onChange(result) {
    if (result) {
      this.creationDateSearchValue = result;
    }
  }
  search(columName, onKeyString) {
    if (columName === "projectName") {
      this.isproSearchValue = false;
      const searchData = { type: "search", key: columName, value: this.proSearchValue };
      this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "nwPlacementName") {
      this.isnwPlacementNameSearchValue = false;
      const searchData = { type: "search", key: columName, value: this.nwPlacementNameSearchValue };
      this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "orgName") {
      this.isOrgSearchValue = false;
      const searchData = { type: "search", key: columName, value: this.orgSearchValue };
      this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
    } else if (columName === "creationDate") {
      this.iscreationDateSearchValue = false;
      this.creationDateSearchValue = `${this.creationDateSearchValue.year}-${this.creationDateSearchValue.month}-${this.creationDateSearchValue.day}`;
      const searchData = { type: "search", key: columName, value: this.creationDateSearchValue };
      this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
    } else {
      this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, []);
    }
  }
  addRow() {
    this.router.navigate(["/main/projects_management/projects_update"], { state: { orgId: this.orgId } });
  }
  editRow(_id) {
    this.router.navigate(["/main/projects_management/projects_update"], { state: { projectId: _id } });
  }
  projectDelete() {
    this.loading = true;
    const projectIds = [...this.setOfCheckedId];
    this.projectsService.ProjectDelete({ projectIds }).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, []);
          this.setOfCheckedId = new Set([...this.setOfCheckedId].filter((id) => !projectIds.includes(id)));
          this.toastr.success(response.message, "Projects Management");
          this.loading = false;
        }
      },
      error: (err) => {
        this.loading = false;
        return this.toastr.error(err.error.message, "Projects Management");
      }
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
  get pages() {
    const totalShownPages = 2;
    const pages = [];
    if (this.totalPages <= totalShownPages) {
      for (let i = 1; i <= this.totalPages; i++) {
        pages.push(i);
      }
    } else {
      let startPage = Math.max(this.pageIndex - 2, 1);
      let endPage = Math.min(startPage + totalShownPages - 1, this.totalPages);
      if (endPage - startPage < totalShownPages - 1) {
        startPage = Math.max(endPage - totalShownPages + 1, 1);
      }
      for (let i = startPage; i <= endPage; i++) {
        pages.push(i);
      }
      if (startPage > 1) {
        pages.unshift("...");
        pages.unshift(1);
      }
      if (endPage < this.totalPages) {
        pages.push("...");
        pages.push(this.totalPages);
      }
    }
    return pages;
  }
  onEnter(columName) {
    this.search(columName);
  }
  onKeydown(columName) {
    if (this.debounceTimeout) {
      clearTimeout(this.debounceTimeout);
    }
    this.debounceTimeout = setTimeout(() => {
      if (columName === "projectName") {
        const searchData = { type: "search", key: columName, value: this.proSearchValue };
        this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
      } else if (columName === "nwPlacementName") {
        const searchData = { type: "search", key: columName, value: this.nwPlacementNameSearchValue };
        this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
      } else if (columName === "orgName") {
        const searchData = { type: "search", key: columName, value: this.orgSearchValue };
        this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
      } else if (columName === "creationDate") {
        const searchData = { type: "search", key: columName, value: this.creationDateSearchValue };
        this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, searchData);
      } else {
        this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, []);
      }
    }, 2e3);
  }
};
_ProjectsListsComponent.\u0275fac = function ProjectsListsComponent_Factory(t) {
  return new (t || _ProjectsListsComponent)(i02.\u0275\u0275directiveInject(i12.Router), i02.\u0275\u0275directiveInject(i2.ToastrService), i02.\u0275\u0275directiveInject(ProjectsService), i02.\u0275\u0275directiveInject(i4.Location), i02.\u0275\u0275directiveInject(UserService), i02.\u0275\u0275directiveInject(LoadingService));
};
_ProjectsListsComponent.\u0275cmp = /* @__PURE__ */ i02.\u0275\u0275defineComponent({ type: _ProjectsListsComponent, selectors: [["app-projects-lists"]], decls: 96, vars: 32, consts: [["projectSearch", "nzDropdownMenu"], ["nwPlacementNameSearch", "nzDropdownMenu"], ["orgSearch", "nzDropdownMenu"], ["headSearch", "nzDropdownMenu"], ["esd", "ngbDatepicker"], [1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "mb-3", "mb-md-0"], [1, "d-flex", "align-items-center", "flex-wrap", "text-nowrap"], ["type", "button", "class", "btn btn-primary btn-icon-text mb-2 mb-md-0", 3, "click", 4, "ngIf"], [1, "row"], [1, "col-md-12", "stretch-card"], [1, "card"], [1, "card-body"], [1, "dataTable-top"], [1, "dataTable-dropdown"], [1, "dataTable-selector", 3, "ngModelChange", "change", "ngModel"], ["value", "10", "selected", ""], ["value", "15"], ["value", "20"], ["value", "25"], [1, "d-flex", "justify-content-end"], ["nz-popconfirm", "", "nzPopconfirmTitle", "Sure to delete?", 3, "nzOnConfirm", 4, "ngIf"], [1, "table-container", "dataTable"], ["nzShowSizeChanger", "", 3, "nzQueryParams", "nzCurrentPageDataChange", "nzData", "nzShowPagination", "nzLoading", "nzTotal", "nzPageSize", "nzPageIndex"], ["class", "check-Box-Width", "nzLabel", "Select all", 3, "nzChecked", "nzIndeterminate", "nzCheckedChange", 4, "ngIf"], ["id", "1", "nzColumnKey", "projectName", "nzCustomFilter", "", 3, "nzSortFn"], [3, "nzVisibleChange", "nzVisible", "nzActive", "nzDropdownMenu"], ["nz-icon", "", "nzType", "search"], ["id", "2", "nzColumnKey", "nwPlacementName", "nzCustomFilter", "", 3, "nzSortFn"], ["id", "1", "nzColumnKey", "orgName", "nzCustomFilter", "", 3, "nzSortFn"], ["id", "3", "nzColumnKey", "creationDate", "nzCustomFilter", "", 3, "nzSortFn"], ["id", "5"], [3, "click", 4, "ngFor", "ngForOf"], ["class", "row", 4, "ngIf"], [1, "ant-table-filter-dropdown"], [1, "search-box"], ["type", "text", "id", "projectName", "nz-input", "", "placeholder", "Search project name", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "button", "id", "btnProjectName", 1, "btn", "searchbtn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["type", "button", "id", "btnResetProj", 1, "btn", "searchbtn", "btn-outline-primary", "btn-icon-text", "me-2", "mb-2", "mb-md-0", 3, "click"], ["type", "text", "id", "nwPlacementNameSearchValue", "nz-input", "", "placeholder", "Search network placement", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "button", "id", "BtnnwPlacementName", 1, "btn", "searchbtn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["type", "button", "id", "btnResetPlacementName", 1, "btn", "searchbtn", "btn-outline-primary", "btn-icon-text", "me-2", "mb-2", "mb-md-0", 3, "click"], ["type", "text", "id", "orgName", "nz-input", "", "placeholder", "Search organization name", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "button", "id", "btnOrgName", 1, "btn", "searchbtn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["type", "button", "id", "btnResetOrgName", 1, "btn", "searchbtn", "btn-outline-primary", "btn-icon-text", "me-2", "mb-2", "mb-md-0", 3, "click"], ["id", "datePicker", "placeholder", "yyyy-mm-dd", "name", "dp", "ngbDatepicker", "", 1, "form-control", "ng-untouched", "ng-pristine", "ng-valid", "date", 3, "ngModelChange", "ngModel"], ["type", "button", "id", "btnDate", 1, "btn", "searchbtn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["type", "button", "id", "btnResetDate", 1, "btn", "searchbtn", "btn-outline-primary", "btn-icon-text", "me-2", "mb-2", "mb-md-0", 3, "click"], ["type", "button", 1, "btn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["data-feather", "plus", "appFeatherIcon", "", 1, "btn-icon-prepend"], ["nz-popconfirm", "", "nzPopconfirmTitle", "Sure to delete?", 3, "nzOnConfirm"], ["nz-button", "", "nzType", "primary", "nzSize", "large", "nzTooltipTitle", "Delete All Project", "nzTooltipPlacement", "top", "nz-tooltip", "", 3, "nzTooltipColor"], ["nz-icon", "", "nzType", "delete", "nzTheme", "outline"], ["nzLabel", "Select all", 1, "check-Box-Width", 3, "nzCheckedChange", "nzChecked", "nzIndeterminate"], [3, "click"], ["class", "check-Box-Width", 3, "nzChecked", "nzLabel", "nzCheckedChange", 4, "ngIf"], ["nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 3, "nzTooltipTitle", "nzTooltipColor"], ["nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", "Demo", "", "Organization", "", 3, "nzTooltipTitle", "nzTooltipColor"], [1, "text-center", 3, "click"], [1, "text-center"], ["type", "checkbox", "id", "isSensitive", "disabled", "", 1, "form-check-input", 3, "checked"], [1, "check-Box-Width", 3, "nzCheckedChange", "nzChecked", "nzLabel"], [1, "col-sm-6", "col-md-5"], ["id", "dataTableExample_info", "role", "status", "aria-live", "polite", 1, "dataTables_info"], [1, "col-sm-6", "col-md-7"], [1, "d-flex", "justify-content-end", 3, "pageChange", "collectionSize", "page", "maxSize", "rotate", "ellipses", "boundaryLinks"], ["ngbPaginationPrevious", ""], ["ngbPaginationNext", ""]], template: function ProjectsListsComponent_Template(rf, ctx) {
  if (rf & 1) {
    const _r1 = i02.\u0275\u0275getCurrentView();
    i02.\u0275\u0275elementStart(0, "div", 5)(1, "div", 6)(2, "div", 7)(3, "div")(4, "h4", 8);
    i02.\u0275\u0275text(5, "Projects Management");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(6, "div", 9);
    i02.\u0275\u0275template(7, ProjectsListsComponent_button_7_Template, 3, 0, "button", 10);
    i02.\u0275\u0275elementEnd()()()();
    i02.\u0275\u0275elementStart(8, "div", 11)(9, "div", 12)(10, "div", 13)(11, "div", 14)(12, "div", 15)(13, "div", 16)(14, "label")(15, "select", 17);
    i02.\u0275\u0275twoWayListener("ngModelChange", function ProjectsListsComponent_Template_select_ngModelChange_15_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.pageSize, $event) || (ctx.pageSize = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275listener("change", function ProjectsListsComponent_Template_select_change_15_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.resetPageIndex());
    });
    i02.\u0275\u0275elementStart(16, "option", 18);
    i02.\u0275\u0275text(17, "10");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(18, "option", 19);
    i02.\u0275\u0275text(19, "15");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(20, "option", 20);
    i02.\u0275\u0275text(21, "20");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(22, "option", 21);
    i02.\u0275\u0275text(23, "25");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275text(24, " entries per page");
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(25, "div", 22);
    i02.\u0275\u0275template(26, ProjectsListsComponent_a_26_Template, 3, 1, "a", 23);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(27, "div", 24)(28, "nz-table", 25);
    i02.\u0275\u0275listener("nzQueryParams", function ProjectsListsComponent_Template_nz_table_nzQueryParams_28_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onQueryParamsChange($event));
    })("nzCurrentPageDataChange", function ProjectsListsComponent_Template_nz_table_nzCurrentPageDataChange_28_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onCurrentPageDataChange($event));
    });
    i02.\u0275\u0275elementStart(29, "thead")(30, "tr");
    i02.\u0275\u0275template(31, ProjectsListsComponent_th_31_Template, 1, 2, "th", 26);
    i02.\u0275\u0275elementStart(32, "th", 27);
    i02.\u0275\u0275text(33, " Project ");
    i02.\u0275\u0275elementStart(34, "nz-filter-trigger", 28);
    i02.\u0275\u0275twoWayListener("nzVisibleChange", function ProjectsListsComponent_Template_nz_filter_trigger_nzVisibleChange_34_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.isproSearchValue, $event) || (ctx.isproSearchValue = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275element(35, "span", 29);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(36, "th", 30);
    i02.\u0275\u0275text(37, " Network Placement ");
    i02.\u0275\u0275elementStart(38, "nz-filter-trigger", 28);
    i02.\u0275\u0275twoWayListener("nzVisibleChange", function ProjectsListsComponent_Template_nz_filter_trigger_nzVisibleChange_38_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.isnwPlacementNameSearchValue, $event) || (ctx.isnwPlacementNameSearchValue = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275element(39, "span", 29);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(40, "th", 31);
    i02.\u0275\u0275text(41, " Organization ");
    i02.\u0275\u0275elementStart(42, "nz-filter-trigger", 28);
    i02.\u0275\u0275twoWayListener("nzVisibleChange", function ProjectsListsComponent_Template_nz_filter_trigger_nzVisibleChange_42_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.isOrgSearchValue, $event) || (ctx.isOrgSearchValue = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275element(43, "span", 29);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(44, "th", 32);
    i02.\u0275\u0275text(45, " Creation Date ");
    i02.\u0275\u0275elementStart(46, "nz-filter-trigger", 28);
    i02.\u0275\u0275twoWayListener("nzVisibleChange", function ProjectsListsComponent_Template_nz_filter_trigger_nzVisibleChange_46_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.iscreationDateSearchValue, $event) || (ctx.iscreationDateSearchValue = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275element(47, "span", 29);
    i02.\u0275\u0275elementEnd()();
    i02.\u0275\u0275elementStart(48, "th", 33);
    i02.\u0275\u0275text(49, "Total tests");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(50, "th", 33);
    i02.\u0275\u0275text(51, "Sensitive flag");
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275elementStart(52, "tbody");
    i02.\u0275\u0275template(53, ProjectsListsComponent_tr_53_Template, 16, 16, "tr", 34);
    i02.\u0275\u0275elementEnd()()();
    i02.\u0275\u0275template(54, ProjectsListsComponent_div_54_Template, 8, 7, "div", 35);
    i02.\u0275\u0275elementStart(55, "nz-dropdown-menu", null, 0)(57, "div", 36)(58, "div", 37)(59, "input", 38);
    i02.\u0275\u0275twoWayListener("ngModelChange", function ProjectsListsComponent_Template_input_ngModelChange_59_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.proSearchValue, $event) || (ctx.proSearchValue = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275listener("keydown", function ProjectsListsComponent_Template_input_keydown_59_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeydown("projectName"));
    })("keydown.enter", function ProjectsListsComponent_Template_input_keydown_enter_59_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onEnter("projectName"));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(60, "button", 39);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_Template_button_click_60_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.search("projectName"));
    });
    i02.\u0275\u0275text(61, " Search");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275text(62, "\xA0\xA0\xA0 ");
    i02.\u0275\u0275elementStart(63, "button", 40);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_Template_button_click_63_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.reset());
    });
    i02.\u0275\u0275text(64, " Reset ");
    i02.\u0275\u0275elementEnd()()()();
    i02.\u0275\u0275elementStart(65, "nz-dropdown-menu", null, 1)(67, "div", 36)(68, "div", 37)(69, "input", 41);
    i02.\u0275\u0275twoWayListener("ngModelChange", function ProjectsListsComponent_Template_input_ngModelChange_69_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.nwPlacementNameSearchValue, $event) || (ctx.nwPlacementNameSearchValue = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275listener("keydown", function ProjectsListsComponent_Template_input_keydown_69_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeydown("nwPlacementName"));
    })("keydown.enter", function ProjectsListsComponent_Template_input_keydown_enter_69_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onEnter("nwPlacementName"));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(70, "button", 42);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_Template_button_click_70_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.search("nwPlacementName"));
    });
    i02.\u0275\u0275text(71, " Search");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275text(72, "\xA0\xA0\xA0 ");
    i02.\u0275\u0275elementStart(73, "button", 43);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_Template_button_click_73_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.reset());
    });
    i02.\u0275\u0275text(74, " Reset ");
    i02.\u0275\u0275elementEnd()()()();
    i02.\u0275\u0275elementStart(75, "nz-dropdown-menu", null, 2)(77, "div", 36)(78, "div", 37)(79, "input", 44);
    i02.\u0275\u0275twoWayListener("ngModelChange", function ProjectsListsComponent_Template_input_ngModelChange_79_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.orgSearchValue, $event) || (ctx.orgSearchValue = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275listener("keydown", function ProjectsListsComponent_Template_input_keydown_79_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onKeydown("orgName"));
    })("keydown.enter", function ProjectsListsComponent_Template_input_keydown_enter_79_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onEnter("orgName"));
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(80, "button", 45);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_Template_button_click_80_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.search("orgName"));
    });
    i02.\u0275\u0275text(81, " Search");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275text(82, "\xA0\xA0\xA0 ");
    i02.\u0275\u0275elementStart(83, "button", 46);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_Template_button_click_83_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.reset());
    });
    i02.\u0275\u0275text(84, " Reset ");
    i02.\u0275\u0275elementEnd()()()();
    i02.\u0275\u0275elementStart(85, "nz-dropdown-menu", null, 3)(87, "div", 36)(88, "div", 37)(89, "input", 47, 4);
    i02.\u0275\u0275listener("ngModelChange", function ProjectsListsComponent_Template_input_ngModelChange_89_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.onChange($event));
    });
    i02.\u0275\u0275twoWayListener("ngModelChange", function ProjectsListsComponent_Template_input_ngModelChange_89_listener($event) {
      i02.\u0275\u0275restoreView(_r1);
      i02.\u0275\u0275twoWayBindingSet(ctx.creationDateSearchValue, $event) || (ctx.creationDateSearchValue = $event);
      return i02.\u0275\u0275resetView($event);
    });
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275elementStart(91, "button", 48);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_Template_button_click_91_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.search("creationDate"));
    });
    i02.\u0275\u0275text(92, " Search");
    i02.\u0275\u0275elementEnd();
    i02.\u0275\u0275text(93, "\xA0\xA0\xA0 ");
    i02.\u0275\u0275elementStart(94, "button", 49);
    i02.\u0275\u0275listener("click", function ProjectsListsComponent_Template_button_click_94_listener() {
      i02.\u0275\u0275restoreView(_r1);
      return i02.\u0275\u0275resetView(ctx.reset());
    });
    i02.\u0275\u0275text(95, " Reset ");
    i02.\u0275\u0275elementEnd()()()()()()()();
  }
  if (rf & 2) {
    const projectSearch_r10 = i02.\u0275\u0275reference(56);
    const nwPlacementNameSearch_r11 = i02.\u0275\u0275reference(66);
    const orgSearch_r12 = i02.\u0275\u0275reference(76);
    const headSearch_r13 = i02.\u0275\u0275reference(86);
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275property("ngIf", ctx.canManageProject || ctx.isAdmin);
    i02.\u0275\u0275advance(8);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.pageSize);
    i02.\u0275\u0275advance(11);
    i02.\u0275\u0275property("ngIf", ctx.setOfCheckedId.size > 0);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("nzData", ctx.listOfprojects)("nzShowPagination", false)("nzLoading", ctx.loading)("nzTotal", ctx.totalRecords)("nzPageSize", ctx.pageSize)("nzPageIndex", ctx.pageIndex);
    i02.\u0275\u0275advance(3);
    i02.\u0275\u0275property("ngIf", ctx.canManageProject || ctx.isAdmin);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("nzSortFn", true);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275twoWayProperty("nzVisible", ctx.isproSearchValue);
    i02.\u0275\u0275property("nzActive", ctx.proSearchValue.length > 0)("nzDropdownMenu", projectSearch_r10);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("nzSortFn", true);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275twoWayProperty("nzVisible", ctx.isnwPlacementNameSearchValue);
    i02.\u0275\u0275property("nzActive", ctx.nwPlacementNameSearchValue.length > 0)("nzDropdownMenu", nwPlacementNameSearch_r11);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("nzSortFn", true);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275twoWayProperty("nzVisible", ctx.isOrgSearchValue);
    i02.\u0275\u0275property("nzActive", ctx.orgSearchValue.length > 0)("nzDropdownMenu", orgSearch_r12);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275property("nzSortFn", true);
    i02.\u0275\u0275advance(2);
    i02.\u0275\u0275twoWayProperty("nzVisible", ctx.iscreationDateSearchValue);
    i02.\u0275\u0275property("nzActive", (ctx.creationDateSearchValue == null ? null : ctx.creationDateSearchValue.length) > 0)("nzDropdownMenu", headSearch_r13);
    i02.\u0275\u0275advance(7);
    i02.\u0275\u0275property("ngForOf", ctx.listOfprojects);
    i02.\u0275\u0275advance();
    i02.\u0275\u0275property("ngIf", ctx.listOfprojects.length);
    i02.\u0275\u0275advance(5);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.proSearchValue);
    i02.\u0275\u0275advance(10);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.nwPlacementNameSearchValue);
    i02.\u0275\u0275advance(10);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.orgSearchValue);
    i02.\u0275\u0275advance(10);
    i02.\u0275\u0275twoWayProperty("ngModel", ctx.creationDateSearchValue);
  }
}, dependencies: [i4.NgForOf, i4.NgIf, i7.NgSelectOption, i7.\u0275NgSelectMultipleOption, i7.DefaultValueAccessor, i7.SelectControlValueAccessor, i7.NgControlStatus, i7.NgModel, i8.NzButtonComponent, i9.\u0275NzTransitionPatchDirective, i10.NzWaveDirective, i11.NzIconDirective, i122.NzDropdownMenuComponent, i13.NzInputDirective, i14.NzTableComponent, i14.NzThAddOnComponent, i14.NzTableCellDirective, i14.NzThMeasureDirective, i14.NzTdAddOnComponent, i14.NzTheadComponent, i14.NzTbodyComponent, i14.NzTrDirective, i14.NzFilterTriggerComponent, i14.NzThSelectionComponent, i15.NzTooltipDirective, i16.NzPopconfirmDirective, FeatherIconDirective, i18.NgbInputDatepicker, i18.NgbPagination, i18.NgbPaginationNext, i18.NgbPaginationPrevious, i4.DatePipe], styles: [`

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
/*# sourceMappingURL=projects-lists.component.css.map */`] });
var ProjectsListsComponent = _ProjectsListsComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i02.\u0275setClassDebugInfo(ProjectsListsComponent, { className: "ProjectsListsComponent", filePath: "src/app/modules/projects/projects-lists/projects-lists.component.ts", lineNumber: 15 });
})();

// src/app/modules/projects/projects-update/projects-update.component.ts
import { Component as Component2 } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import { Validators } from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i03 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
import * as i17 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_forms.js?v=ca23e844";
import * as i3 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/ngx-toastr.js?v=ca23e844";
import * as i42 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_router.js?v=ca23e844";
import * as i5 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_common.js?v=ca23e844";
import * as i92 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@ng-select_ng-select.js?v=ca23e844";
import * as i102 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@ng-bootstrap_ng-bootstrap.js?v=ca23e844";
var _c0 = () => ({ standalone: true });
function ProjectsUpdateComponent_div_36_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter your project name! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_36_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 26);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_36_div_1_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("projectName")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
  }
}
function ProjectsUpdateComponent_div_51_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please select organization name! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_51_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 26);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_51_div_1_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("orgName")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
  }
}
function ProjectsUpdateComponent_div_58_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please select network placement! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_58_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 26);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_58_div_1_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("nwPlacementName")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
  }
}
function ProjectsUpdateComponent_div_69_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please select creation date! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_69_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 26);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_69_div_1_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("creationDate")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
  }
}
function ProjectsUpdateComponent_div_80_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter info range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_80_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_80_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " info range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_80_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 54);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_80_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_80_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_80_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("infoMin")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("infoMin")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("infoMin")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
function ProjectsUpdateComponent_div_81_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter info range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_81_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_81_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " info range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_81_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 26);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_81_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_81_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_81_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("infoMax")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("infoMax")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("infoMax")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
function ProjectsUpdateComponent_div_91_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter low range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_91_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_91_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " low range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_91_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 54);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_91_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_91_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_91_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("lowMin")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("lowMin")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("lowMin")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
function ProjectsUpdateComponent_div_92_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter low range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_92_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_92_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " low range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_92_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 26);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_92_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_92_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_92_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("lowMax")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("lowMax")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("lowMax")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
function ProjectsUpdateComponent_div_103_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter info range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_103_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_103_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Medium range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_103_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 54);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_103_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_103_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_103_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("mediumMin")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("mediumMin")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("mediumMin")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
function ProjectsUpdateComponent_div_104_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter info range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_104_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_104_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Medium range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_104_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 26);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_104_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_104_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_104_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("mediumMax")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("mediumMax")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("mediumMax")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
function ProjectsUpdateComponent_div_114_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter info range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_114_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_114_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " High range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_114_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 54);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_114_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_114_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_114_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    //i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("highMin")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    //i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("highMin")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    //i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("highMin")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
function ProjectsUpdateComponent_div_115_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter info range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_115_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_115_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " High range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_115_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 26);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_115_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_115_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_115_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("highMax")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("highMax")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("highMax")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
function ProjectsUpdateComponent_div_126_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter info range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_126_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_126_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Critical range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_126_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 54);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_126_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_126_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_126_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("criticalMin")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("criticalMin")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("criticalMin")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
function ProjectsUpdateComponent_div_127_div_1_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Please enter info range inclusive! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_127_div_2_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Only numbers are allowed ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_127_div_3_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div");
    i03.\u0275\u0275text(1, " Critical range inclusive cannot be negative! ");
    i03.\u0275\u0275elementEnd();
  }
}
function ProjectsUpdateComponent_div_127_Template(rf, ctx) {
  if (rf & 1) {
    i03.\u0275\u0275elementStart(0, "div", 26);
    i03.\u0275\u0275template(1, ProjectsUpdateComponent_div_127_div_1_Template, 2, 0, "div", 53)(2, ProjectsUpdateComponent_div_127_div_2_Template, 2, 0, "div", 53)(3, ProjectsUpdateComponent_div_127_div_3_Template, 2, 0, "div", 53);
    i03.\u0275\u0275elementEnd();
  }
  if (rf & 2) {
    let tmp_2_0;
    let tmp_3_0;
    let tmp_4_0;
    const ctx_r1 = i03.\u0275\u0275nextContext();
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_2_0 = ctx_r1.projectForm.get("criticalMax")) == null ? null : tmp_2_0.errors == null ? null : tmp_2_0.errors["required"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_3_0 = ctx_r1.projectForm.get("criticalMax")) == null ? null : tmp_3_0.errors == null ? null : tmp_3_0.errors["pattern"]);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", ctx_r1.projectForm == null ? null : (tmp_4_0 = ctx_r1.projectForm.get("criticalMax")) == null ? null : tmp_4_0.errors == null ? null : tmp_4_0.errors["min"]);
  }
}
var _ProjectsUpdateComponent = class _ProjectsUpdateComponent {
  constructor(fb, projectsService, toastr, router, location, settingsService, datePipe, CommonService2, loaderService) {
    this.fb = fb;
    this.projectsService = projectsService;
    this.toastr = toastr;
    this.router = router;
    this.location = location;
    this.settingsService = settingsService;
    this.datePipe = datePipe;
    this.CommonService = CommonService2;
    this.loaderService = loaderService;
    this.size = "large";
    this.state = this.location.getState();
    this.orgId = [];
    this.nwPlacementId = [];
    this.isLoading = false;
  }
  ngOnInit() {
    this.projectId = this.state?.projectId;
    this.init();
    this.getOrgList();
    this.getNetwork();
    if (this.state?.orgId) {
      this.orgId = this.state?.orgId;
    }
    if (this.projectId) {
      this.projectDetails(this.projectId);
    }
  }
  onChange(result) {
    //if (result && result.year && result.month && result.day) {
      this.convertDate(result);
    //}
  }
  convertDate(date) {
    //const year = date.year;
    //const month = String(date.month).padStart(2, "0");
    //const day = String(date.day).padStart(2, "0");
    //date = `${year}-${month}-${day}`;
    this.projectForm.get("creationDate")?.setValue(date);
  }
  convertForUpdated(dateString) {
    this.projectForm.get("creationDate")?.setValue(dateString);
    return this.CommonService.convertDateString(dateString);
  }
  init() {
    this.projectForm = this.fb.group({
      projectName: ["", [Validators.required]],
      orgName: ["", [Validators.required]],
      nwPlacementName: ["", [Validators.required]],
      projectShortName: [""],
      projectDesc: [""],
      creationDate: ["", [Validators.required]],
      isSensitive: [false],
      isActive: [true],
      infoMin: [""],
      infoMax: [""],
      lowMin: [""],
      lowMax: [""],
      mediumMin: [""],
      mediumMax: [""],
      highMin: [""],
      highMax: [""],
      criticalMin: [""],
      criticalMax: [""]
    });
  }
  projectDetails(id) {
    this.loaderService.show();
    this.projectsService.ProjectDetails(id).subscribe({
      next: (response) => {
        if (response.status === true) {
          const projectData = response.data[0].project;
          const severityData = response.data[0].severity;
          this.creationDate = this.convertForUpdated(projectData?.creationDate);
          this.projectForm.patchValue({
            projectName: projectData?.projectName,
            projectShortName: projectData?.projectShortName,
            projectDesc: projectData?.projectDesc,
            isSensitive: projectData?.isSensitive,
            orgName: projectData?.orgName,
            infoMin: severityData.infoMin,
            infoMax: severityData.infoMax,
            lowMin: severityData.lowMin,
            lowMax: severityData.lowMax,
            mediumMin: severityData.mediumMin,
            mediumMax: severityData.mediumMax,
            highMin: severityData.highMin,
            highMax: severityData.highMax,
            criticalMin: severityData.criticalMin,
            criticalMax: severityData.criticalMax,
            isActive: severityData.isActive
          });
          this.orgId = projectData.orgId;
          this.nwPlacementId = projectData.nwPlacementId;
          this.loaderService.hide();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Projects Management");
      }
    });
  }
  submitForm() {
    //if (this.projectForm.valid) {
      if (this.projectId) {
        this.updateData();
      } else {
        this.SaveData();
      }
    //} else {
     // Object.values(this.projectForm.controls).forEach((control) => {
       // if (control.invalid) {
         // control.markAsDirty();
         // control.updateValueAndValidity({ onlySelf: true });
      //  }
      //});
    //}
  }
  updateData() {
    this.loaderService.show();
    const data = this.projectForm.value;
    const payload = {
      projectId: this.projectId,
      projectName: data.projectName,
      projectShortName: data.projectShortName,
      projectDesc: data.projectDesc,
      orgId: this.orgId,
      nwPlacementId: this.nwPlacementId,
      languageId: "",
      isSensitive: data.isSensitive,
      isSeverity: false,
      creationDate: data.creationDate,
      isActive: data.isActive,
      severity: {
        infoMin: data.infoMin,
        infoMax: data.infoMax,
        lowMin: data.lowMin,
        lowMax: data.lowMax,
        mediumMin: data.mediumMin,
        mediumMax: data.mediumMax,
        highMin: data.highMin,
        highMax: data.highMax,
        criticalMin: data.criticalMin,
        criticalMax: data.criticalMax
      }
    };
    this.projectsService.ProjectEdit(payload).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Projects Management");
          this.loaderService.hide();
          this.goBack();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Projects Management");
      }
    });
  }
  SaveData() {
    this.loaderService.show();
    const data = this.projectForm.value;
    const payload = {
      projectName: data.projectName,
      projectShortName: data.projectShortName,
      projectDesc: data.projectDesc,
      orgId: this.orgId,
      nwPlacementId: this.nwPlacementId,
      languageId: "",
      isSensitive: data.isSensitive,
      isSeverity: false,
      creationDate: data.creationDate,
      isActive: data.isActive,
      severity: {
        infoMin: data.infoMin,
        infoMax: data.infoMax,
        lowMin: data.lowMin,
        lowMax: data.lowMax,
        mediumMin: data.mediumMin,
        mediumMax: data.mediumMax,
        highMin: data.highMin,
        highMax: data.highMax,
        criticalMin: data.criticalMin,
        criticalMax: data.criticalMax
      }
    };
    this.projectsService.ProjectAdd(payload).subscribe({
      next: (response) => {
        if (response.status === true) {
          this.toastr.success(response.message, "Projects Management");
          this.loaderService.hide();
          this.goBack();
        }
      },
      error: (err) => {
        this.loaderService.hide();
        return this.toastr.error(err.error.message, "Projects Management");
      }
    });
  }
  goBack() {
    this.router.navigate(["/main/projects_management/projects_list"]);
  }
  getOrgList() {
    this.isLoading = true;
    this.settingsService.GetOrgList("ASSIGNED").subscribe({
      next: (response) => {
        if (response.status === true) {
          this.allOrgList = response.data;
          this.isLoading = false;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Projects Management");
      }
    });
  }
  getNetwork() {
    this.isLoading = true;
    this.projectsService.GetNetwork().subscribe({
      next: (response) => {
        if (response.status === true) {
          this.networkList = response.data;
          this.isLoading = false;
        }
      },
      error: (err) => {
        return this.toastr.error(err.error.message, "Projects Management");
      }
    });
  }
  setValue() {
    this.projectForm.patchValue({
      infoMin: 0,
      infoMax: 0,
      lowMin: 0.01,
      lowMax: 3.99,
      mediumMin: 4,
      mediumMax: 6.99,
      highMin: 7,
      highMax: 8.99,
      criticalMin: 9,
      criticalMax: 10
    });
  }
};
_ProjectsUpdateComponent.\u0275fac = function ProjectsUpdateComponent_Factory(t) {
  return new (t || _ProjectsUpdateComponent)(i03.\u0275\u0275directiveInject(i17.NonNullableFormBuilder), i03.\u0275\u0275directiveInject(ProjectsService), i03.\u0275\u0275directiveInject(i3.ToastrService), i03.\u0275\u0275directiveInject(i42.Router), i03.\u0275\u0275directiveInject(i5.Location), i03.\u0275\u0275directiveInject(SettingsService), i03.\u0275\u0275directiveInject(i5.DatePipe), i03.\u0275\u0275directiveInject(CommonService), i03.\u0275\u0275directiveInject(LoadingService));
};
_ProjectsUpdateComponent.\u0275cmp = /* @__PURE__ */ i03.\u0275\u0275defineComponent({ type: _ProjectsUpdateComponent, selectors: [["app-projects-update"]], decls: 133, vars: 26, consts: [["d", "ngbDatepicker"], [1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "page-breadcrumb", "m-0"], [1, "breadcrumb", "mb-0"], [1, "breadcrumb-item"], ["routerLink", "/main/projects_management/projects_list"], ["aria-current", "page", 1, "breadcrumb-item", "active"], [1, "button-container"], [1, "forms-sample", "d-flex", "flex-wrap", "justify-content-center", 3, "formGroup"], [1, "form-check", "form-switch", "me-3"], ["type", "text", "formControlName", "isActive", "id", "Active", 1, "form-check-input"], ["for", "Active", 1, "form-check-label"], [1, "form-check", "form-switch"], ["type", "text", "formControlName", "isSensitive", "id", "ZeroKnowledge", 1, "form-check-input"], ["for", "ZeroKnowledge", 1, "form-check-label"], [1, "btn", "btn-secondary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], [1, "btn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], [1, "row"], [1, "col-md-12", "grid-margin"], [1, "card", "card_padding"], [1, "card-body"], [1, "forms-sample", 3, "formGroup"], [1, "mb-3"], [1, "form-label"], [1, "text-danger"], ["id", "projectName", "formControlName", "projectName", "placeholder", "Enter project name", "required", "", 1, "form-control"], ["class", "text-danger", 4, "ngIf"], ["id", "projectShortName", "formControlName", "projectShortName", "placeholder", "Enter project short name", 1, "form-control"], ["id", "projectDesc", "formControlName", "projectDesc", "placeholder", "Enter project description", "rows", "3", 1, "form-control"], ["id", "allOrgList", "bindLabel", "orgName", "bindValue", "_id", "placeholder", "Select organization", "formControlName", "orgName", 3, "ngModelChange", "items", "ngModel", "loading"], ["id", "networkList", "bindLabel", "nwPlacementName", "bindValue", "_id", "placeholder", "Select network placement", "formControlName", "nwPlacementName", 3, "ngModelChange", "items", "ngModel", "loading"], [1, "input-group"], ["placeholder", "yyyy-mm-dd", "name", "dp", "id", "creationDate", "ngbDatepicker", "", 1, "form-control", "ng-untouched", "ng-pristine", "ng-valid", "date", 3, "ngModelChange", "ngModel", "ngModelOptions"], ["type", "button", 1, "input-group-text", 3, "click"], [1, "feather", "icon-calendar", "icon-md", "text-muted"], [1, "row", "mb-3"], [1, "col-md-6"], [1, "d-flex"], ["type", "text", "id", "infoMin", "formControlName", "infoMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "text", "id", "infoMax", "formControlName", "infoMax", "placeholder", "Max", "min", "0", "required", "", 1, "form-control"], ["class", "text-danger m_r", 4, "ngIf"], [1, "col-md-6", "cssroe"], ["type", "text", "id", "lowMin", "formControlName", "lowMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "text", "id", "lowMax", "formControlName", "lowMax", "placeholder", "Max", "min", "0", "required", "", 1, "form-control"], ["type", "text", "id", "mediumMin", "formControlName", "mediumMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "text", "id", "mediumMax", "formControlName", "mediumMax", "placeholder", "Max", "min", "0", "required", "", 1, "form-control"], ["type", "text", "id", "highMin", "formControlName", "highMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "text", "id", "highMax", "formControlName", "highMax", "placeholder", "Max", "min", "0", "required", "", 1, "form-control"], ["type", "text", "id", "criticalMin", "formControlName", "criticalMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "text", "id", "criticalMax", "formControlName", "criticalMax", "min", "0", "placeholder", "Max", "required", "", 1, "form-control"], ["type", "button", 1, "btn", "btn-outline-primary", "mb-1", "mb-md-0", "infoBtn", 3, "click"], [4, "ngIf"], [1, "text-danger", "m_r"]], template: function ProjectsUpdateComponent_Template(rf, ctx) {
  if (rf & 1) {
    const _r1 = i03.\u0275\u0275getCurrentView();
    i03.\u0275\u0275elementStart(0, "div", 1)(1, "div", 2)(2, "div", 3)(3, "nav", 4)(4, "ol", 5)(5, "li", 6)(6, "a", 7);
    i03.\u0275\u0275text(7, "Project");
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275elementStart(8, "li", 8);
    i03.\u0275\u0275text(9);
    i03.\u0275\u0275elementEnd()()();
    i03.\u0275\u0275elementStart(10, "div", 9)(11, "form", 10)(12, "div", 11);
    i03.\u0275\u0275element(13, "input", 12);
    i03.\u0275\u0275elementStart(14, "label", 13);
    i03.\u0275\u0275text(15, "Active");
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275elementStart(16, "div", 14);
    i03.\u0275\u0275element(17, "input", 15);
    i03.\u0275\u0275elementStart(18, "label", 16);
    i03.\u0275\u0275text(19, "Sensitive Recommendation");
    i03.\u0275\u0275elementEnd()()()();
    i03.\u0275\u0275elementStart(20, "div", 9)(21, "button", 17);
    i03.\u0275\u0275listener("click", function ProjectsUpdateComponent_Template_button_click_21_listener() {
      i03.\u0275\u0275restoreView(_r1);
      return i03.\u0275\u0275resetView(ctx.goBack());
    });
    i03.\u0275\u0275text(22, "Back");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(23, "button", 18);
    i03.\u0275\u0275listener("click", function ProjectsUpdateComponent_Template_button_click_23_listener() {
      i03.\u0275\u0275restoreView(_r1);
      return i03.\u0275\u0275resetView(ctx.submitForm());
    });
    i03.\u0275\u0275text(24, "Submit");
    i03.\u0275\u0275elementEnd()()()()();
    i03.\u0275\u0275elementStart(25, "div", 19)(26, "div", 20)(27, "div", 21)(28, "div", 22)(29, "form", 23)(30, "div", 24)(31, "label", 25);
    i03.\u0275\u0275text(32, "Project Name");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(33, "span", 26);
    i03.\u0275\u0275text(34, " *");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275element(35, "input", 27);
    i03.\u0275\u0275template(36, ProjectsUpdateComponent_div_36_Template, 2, 1, "div", 28);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(37, "div", 24)(38, "label", 25);
    i03.\u0275\u0275text(39, "Project Short Name");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275element(40, "input", 29);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(41, "div", 24)(42, "label", 25);
    i03.\u0275\u0275text(43, "Project Description");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275element(44, "textarea", 30);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(45, "div", 24)(46, "label", 25);
    i03.\u0275\u0275text(47, "Organization");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(48, "span", 26);
    i03.\u0275\u0275text(49, " *");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(50, "ng-select", 31);
    i03.\u0275\u0275twoWayListener("ngModelChange", function ProjectsUpdateComponent_Template_ng_select_ngModelChange_50_listener($event) {
      i03.\u0275\u0275restoreView(_r1);
      i03.\u0275\u0275twoWayBindingSet(ctx.orgId, $event) || (ctx.orgId = $event);
      return i03.\u0275\u0275resetView($event);
    });
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275template(51, ProjectsUpdateComponent_div_51_Template, 2, 1, "div", 28);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(52, "div", 24)(53, "label", 25);
    i03.\u0275\u0275text(54, "Network Placement");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(55, "span", 26);
    i03.\u0275\u0275text(56, " *");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(57, "ng-select", 32);
    i03.\u0275\u0275twoWayListener("ngModelChange", function ProjectsUpdateComponent_Template_ng_select_ngModelChange_57_listener($event) {
      i03.\u0275\u0275restoreView(_r1);
      i03.\u0275\u0275twoWayBindingSet(ctx.nwPlacementId, $event) || (ctx.nwPlacementId = $event);
      return i03.\u0275\u0275resetView($event);
    });
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275template(58, ProjectsUpdateComponent_div_58_Template, 2, 1, "div", 28);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(59, "div", 24)(60, "label", 25);
    i03.\u0275\u0275text(61, "Creation Date");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(62, "span", 26);
    i03.\u0275\u0275text(63, " *");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(64, "div", 33)(65, "input", 34, 0);
    i03.\u0275\u0275twoWayListener("ngModelChange", function ProjectsUpdateComponent_Template_input_ngModelChange_65_listener($event) {
      i03.\u0275\u0275restoreView(_r1);
      i03.\u0275\u0275twoWayBindingSet(ctx.creationDate, $event) || (ctx.creationDate = $event);
      return i03.\u0275\u0275resetView($event);
    });
    i03.\u0275\u0275listener("ngModelChange", function ProjectsUpdateComponent_Template_input_ngModelChange_65_listener($event) {
      i03.\u0275\u0275restoreView(_r1);
      return i03.\u0275\u0275resetView(ctx.onChange($event));
    });
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(67, "button", 35);
    i03.\u0275\u0275listener("click", function ProjectsUpdateComponent_Template_button_click_67_listener() {
      i03.\u0275\u0275restoreView(_r1);
      const d_r3 = i03.\u0275\u0275reference(66);
      return i03.\u0275\u0275resetView(d_r3.toggle());
    });
    i03.\u0275\u0275element(68, "i", 36);
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275template(69, ProjectsUpdateComponent_div_69_Template, 2, 1, "div", 28);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(70, "div", 37)(71, "div", 38)(72, "label", 25);
    i03.\u0275\u0275text(73, "Info range inclusive");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(74, "span", 26);
    i03.\u0275\u0275text(75, " *");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(76, "div", 39);
    i03.\u0275\u0275element(77, "input", 40)(78, "input", 41);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(79, "div", 39);
    i03.\u0275\u0275template(80, ProjectsUpdateComponent_div_80_Template, 4, 3, "div", 42)(81, ProjectsUpdateComponent_div_81_Template, 4, 3, "div", 28);
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275elementStart(82, "div", 43)(83, "label", 25);
    i03.\u0275\u0275text(84, "Low range inclusive");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(85, "span", 26);
    i03.\u0275\u0275text(86, " *");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(87, "div", 39);
    i03.\u0275\u0275element(88, "input", 44)(89, "input", 45);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(90, "div", 39);
    i03.\u0275\u0275template(91, ProjectsUpdateComponent_div_91_Template, 4, 3, "div", 42)(92, ProjectsUpdateComponent_div_92_Template, 4, 3, "div", 28);
    i03.\u0275\u0275elementEnd()()();
    i03.\u0275\u0275elementStart(93, "div", 37)(94, "div", 38)(95, "label", 25);
    i03.\u0275\u0275text(96, "Medium range inclusive");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(97, "span", 26);
    i03.\u0275\u0275text(98, " *");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(99, "div", 39);
    i03.\u0275\u0275element(100, "input", 46)(101, "input", 47);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(102, "div", 39);
    i03.\u0275\u0275template(103, ProjectsUpdateComponent_div_103_Template, 4, 3, "div", 42)(104, ProjectsUpdateComponent_div_104_Template, 4, 3, "div", 28);
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275elementStart(105, "div", 43)(106, "label", 25);
    i03.\u0275\u0275text(107, "High range inclusive");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(108, "span", 26);
    i03.\u0275\u0275text(109, " *");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(110, "div", 39);
    i03.\u0275\u0275element(111, "input", 48)(112, "input", 49);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(113, "div", 39);
    i03.\u0275\u0275template(114, ProjectsUpdateComponent_div_114_Template, 4, 3, "div", 42)(115, ProjectsUpdateComponent_div_115_Template, 4, 3, "div", 28);
    i03.\u0275\u0275elementEnd()()();
    i03.\u0275\u0275elementStart(116, "div", 37)(117, "div", 38)(118, "label", 25);
    i03.\u0275\u0275text(119, "Critical range inclusive");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(120, "span", 26);
    i03.\u0275\u0275text(121, " *");
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(122, "div", 39);
    i03.\u0275\u0275element(123, "input", 50)(124, "input", 51);
    i03.\u0275\u0275elementEnd();
    i03.\u0275\u0275elementStart(125, "div", 39);
    i03.\u0275\u0275template(126, ProjectsUpdateComponent_div_126_Template, 4, 3, "div", 42)(127, ProjectsUpdateComponent_div_127_Template, 4, 3, "div", 28);
    i03.\u0275\u0275elementEnd()();
    i03.\u0275\u0275elementStart(128, "div", 38)(129, "div");
    i03.\u0275\u0275element(130, "label", 25);
    i03.\u0275\u0275elementStart(131, "button", 52);
    i03.\u0275\u0275listener("click", function ProjectsUpdateComponent_Template_button_click_131_listener() {
      i03.\u0275\u0275restoreView(_r1);
      return i03.\u0275\u0275resetView(ctx.setValue());
    });
    i03.\u0275\u0275text(132, "Set default value");
    i03.\u0275\u0275elementEnd()()()()()()()()();
  }
  if (rf & 2) {
    let tmp_4_0;
    let tmp_8_0;
    let tmp_12_0;
    let tmp_15_0;
    let tmp_16_0;
    let tmp_17_0;
    let tmp_18_0;
    let tmp_19_0;
    let tmp_20_0;
    let tmp_21_0;
    let tmp_22_0;
    let tmp_23_0;
    let tmp_24_0;
    let tmp_25_0;
    i03.\u0275\u0275advance(9);
    i03.\u0275\u0275textInterpolate1("", (ctx.state == null ? null : ctx.state.projectId) ? "Update" : "New", " Project");
    i03.\u0275\u0275advance(2);
    i03.\u0275\u0275property("formGroup", ctx.projectForm);
    i03.\u0275\u0275advance(18);
    i03.\u0275\u0275property("formGroup", ctx.projectForm);
    i03.\u0275\u0275advance(7);
    i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_4_0 = ctx.projectForm.get("projectName")) == null ? null : tmp_4_0.dirty) && (ctx.projectForm == null ? null : (tmp_4_0 = ctx.projectForm.get("projectName")) == null ? null : tmp_4_0.errors) || (ctx.projectForm == null ? null : (tmp_4_0 = ctx.projectForm.get("projectName")) == null ? null : tmp_4_0.touched));
    i03.\u0275\u0275advance(14);
    i03.\u0275\u0275property("items", ctx.allOrgList);
    i03.\u0275\u0275twoWayProperty("ngModel", ctx.orgId);
    i03.\u0275\u0275property("loading", ctx.isLoading);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_8_0 = ctx.projectForm.get("orgName")) == null ? null : tmp_8_0.dirty) && (ctx.projectForm == null ? null : (tmp_8_0 = ctx.projectForm.get("orgName")) == null ? null : tmp_8_0.errors) || (ctx.projectForm == null ? null : (tmp_8_0 = ctx.projectForm.get("orgName")) == null ? null : tmp_8_0.touched));
    i03.\u0275\u0275advance(6);
    i03.\u0275\u0275property("items", ctx.networkList);
    i03.\u0275\u0275twoWayProperty("ngModel", ctx.nwPlacementId);
    i03.\u0275\u0275property("loading", ctx.isLoading);
    i03.\u0275\u0275advance();
    i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_12_0 = ctx.projectForm.get("nwPlacementName")) == null ? null : tmp_12_0.dirty) && (ctx.projectForm == null ? null : (tmp_12_0 = ctx.projectForm.get("nwPlacementName")) == null ? null : tmp_12_0.errors) || (ctx.projectForm == null ? null : (tmp_12_0 = ctx.projectForm.get("nwPlacementName")) == null ? null : tmp_12_0.touched));
    i03.\u0275\u0275advance(7);
    i03.\u0275\u0275twoWayProperty("ngModel", ctx.creationDate);
    i03.\u0275\u0275property("ngModelOptions", i03.\u0275\u0275pureFunction0(25, _c0));
    i03.\u0275\u0275advance(4);
    i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_15_0 = ctx.projectForm.get("creationDate")) == null ? null : tmp_15_0.dirty) && (ctx.projectForm == null ? null : (tmp_15_0 = ctx.projectForm.get("creationDate")) == null ? null : tmp_15_0.errors) || (ctx.projectForm == null ? null : (tmp_15_0 = ctx.projectForm.get("creationDate")) == null ? null : tmp_15_0.touched));
    i03.\u0275\u0275advance(11);
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_16_0 = ctx.projectForm.get("infoMin")) == null ? null : tmp_16_0.dirty) && (ctx.projectForm == null ? null : (tmp_16_0 = ctx.projectForm.get("infoMin")) == null ? null : tmp_16_0.errors) || (ctx.projectForm == null ? null : (tmp_16_0 = ctx.projectForm.get("infoMin")) == null ? null : tmp_16_0.touched));
    i03.\u0275\u0275advance();
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_17_0 = ctx.projectForm.get("infoMax")) == null ? null : tmp_17_0.dirty) && (ctx.projectForm == null ? null : (tmp_17_0 = ctx.projectForm.get("infoMax")) == null ? null : tmp_17_0.errors) || (ctx.projectForm == null ? null : (tmp_17_0 = ctx.projectForm.get("infoMax")) == null ? null : tmp_17_0.touched));
    i03.\u0275\u0275advance(10);
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_18_0 = ctx.projectForm.get("lowMin")) == null ? null : tmp_18_0.dirty) && (ctx.projectForm == null ? null : (tmp_18_0 = ctx.projectForm.get("lowMin")) == null ? null : tmp_18_0.errors) || (ctx.projectForm == null ? null : (tmp_18_0 = ctx.projectForm.get("lowMin")) == null ? null : tmp_18_0.touched));
    i03.\u0275\u0275advance();
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_19_0 = ctx.projectForm.get("lowMax")) == null ? null : tmp_19_0.dirty) && (ctx.projectForm == null ? null : (tmp_19_0 = ctx.projectForm.get("lowMax")) == null ? null : tmp_19_0.errors) || (ctx.projectForm == null ? null : (tmp_19_0 = ctx.projectForm.get("lowMax")) == null ? null : tmp_19_0.touched));
    i03.\u0275\u0275advance(11);
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_20_0 = ctx.projectForm.get("mediumMin")) == null ? null : tmp_20_0.dirty) && (ctx.projectForm == null ? null : (tmp_20_0 = ctx.projectForm.get("mediumMin")) == null ? null : tmp_20_0.errors) || (ctx.projectForm == null ? null : (tmp_20_0 = ctx.projectForm.get("mediumMin")) == null ? null : tmp_20_0.touched));
    i03.\u0275\u0275advance();
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_21_0 = ctx.projectForm.get("mediumMax")) == null ? null : tmp_21_0.dirty) && (ctx.projectForm == null ? null : (tmp_21_0 = ctx.projectForm.get("mediumMax")) == null ? null : tmp_21_0.errors) || (ctx.projectForm == null ? null : (tmp_21_0 = ctx.projectForm.get("mediumMax")) == null ? null : tmp_21_0.touched));
    i03.\u0275\u0275advance(10);
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_22_0 = ctx.projectForm.get("highMin")) == null ? null : tmp_22_0.dirty) && (ctx.projectForm == null ? null : (tmp_22_0 = ctx.projectForm.get("highMin")) == null ? null : tmp_22_0.errors) || (ctx.projectForm == null ? null : (tmp_22_0 = ctx.projectForm.get("highMin")) == null ? null : tmp_22_0.touched));
    i03.\u0275\u0275advance();
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_23_0 = ctx.projectForm.get("highMax")) == null ? null : tmp_23_0.dirty) && (ctx.projectForm == null ? null : (tmp_23_0 = ctx.projectForm.get("highMax")) == null ? null : tmp_23_0.errors) || (ctx.projectForm == null ? null : (tmp_23_0 = ctx.projectForm.get("highMax")) == null ? null : tmp_23_0.touched));
    i03.\u0275\u0275advance(11);
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_24_0 = ctx.projectForm.get("criticalMin")) == null ? null : tmp_24_0.dirty) && (ctx.projectForm == null ? null : (tmp_24_0 = ctx.projectForm.get("criticalMin")) == null ? null : tmp_24_0.errors) || (ctx.projectForm == null ? null : (tmp_24_0 = ctx.projectForm.get("criticalMin")) == null ? null : tmp_24_0.touched));
    i03.\u0275\u0275advance();
    //i03.\u0275\u0275property("ngIf", (ctx.projectForm == null ? null : (tmp_25_0 = ctx.projectForm.get("criticalMax")) == null ? null : tmp_25_0.dirty) && (ctx.projectForm == null ? null : (tmp_25_0 = ctx.projectForm.get("criticalMax")) == null ? null : tmp_25_0.errors) || (ctx.projectForm == null ? null : (tmp_25_0 = ctx.projectForm.get("criticalMax")) == null ? null : tmp_25_0.touched));
  }
}, dependencies: [i5.NgIf, i42.RouterLink, i17.\u0275NgNoValidate, i17.DefaultValueAccessor, i17.NumberValueAccessor, i17.CheckboxControlValueAccessor, i17.NgControlStatus, i17.NgControlStatusGroup, i17.RequiredValidator, i17.MinValidator, i17.NgModel, i17.FormGroupDirective, i17.FormControlName, i92.NgSelectComponent, i102.NgbInputDatepicker], styles: ["\n\n.mb[_ngcontent-%COMP%] {\n  margin-bottom: 0rem !important;\n}\n.p[_ngcontent-%COMP%] {\n  margin-bottom: 6px;\n}\n.ant-picker[_ngcontent-%COMP%]:hover, .ant-picker-focused[_ngcontent-%COMP%] {\n  border-color: #ced4da;\n  box-shadow: none !important;\n}\n[_nghost-%COMP%]     .ant-picker-input > input:focus, .ant-picker-input[_ngcontent-%COMP%]    > input-focused[_ngcontent-%COMP%] {\n  border-color: #ced4da;\n  box-shadow: 0 0 0 2px rgba(236, 238, 240, 0.2);\n  border-right-width: 1px;\n  outline: 0;\n}\n[_nghost-%COMP%]     .ant-picker-input > input:placeholder-shown {\n  font-size: 14px !important;\n}\n  .ng-dropdown-panel .ng-dropdown-panel-items .ng-option, .ng-dropdown-panel[_ngcontent-%COMP%]   .ng-dropdown-panel-items[_ngcontent-%COMP%]   .ng-optgroup[_ngcontent-%COMP%] {\n  background-color: #fff;\n  color: var(--bs-body-color);\n}\n@media screen and (max-width: 772px) {\n  .infoBtn[_ngcontent-%COMP%] {\n    margin-top: 20px !important;\n  }\n  .cssroe[_ngcontent-%COMP%] {\n    margin-top: 15px !important;\n  }\n  .infoBtnG[_ngcontent-%COMP%] {\n    text-align: end !important;\n  }\n}\n.infoBtn[_ngcontent-%COMP%] {\n  margin-top: 30px;\n  height: 36px;\n}\n.m_r[_ngcontent-%COMP%] {\n  margin-right: 18%;\n}\n/*# sourceMappingURL=projects-update.component.css.map */"] });
var ProjectsUpdateComponent = _ProjectsUpdateComponent;
(() => {
  (typeof ngDevMode === "undefined" || ngDevMode) && i03.\u0275setClassDebugInfo(ProjectsUpdateComponent, { className: "ProjectsUpdateComponent", filePath: "src/app/modules/projects/projects-update/projects-update.component.ts", lineNumber: 17 });
})();

// src/app/modules/projects/projects-routing.module.ts
import * as i04 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
var routes = [
  {
    path: "projects_list",
    component: ProjectsListsComponent,
    canActivate: [AuthGuard]
  },
  {
    path: "projects_update",
    component: ProjectsUpdateComponent,
    canActivate: [AuthGuard]
  }
];
var _ProjectsRoutingModule = class _ProjectsRoutingModule {
};
_ProjectsRoutingModule.\u0275fac = function ProjectsRoutingModule_Factory(t) {
  return new (t || _ProjectsRoutingModule)();
};
_ProjectsRoutingModule.\u0275mod = /* @__PURE__ */ i04.\u0275\u0275defineNgModule({ type: _ProjectsRoutingModule });
_ProjectsRoutingModule.\u0275inj = /* @__PURE__ */ i04.\u0275\u0275defineInjector({ imports: [RouterModule.forChild(routes), RouterModule] });
var ProjectsRoutingModule = _ProjectsRoutingModule;

// src/app/modules/projects/projects.module.ts
import * as i05 from "/@fs/home/brutegoat/NSTAR/nstar_web/.angular/cache/17.3.8/vite/deps/@angular_core.js?v=ca23e844";
var _ProjectsModule = class _ProjectsModule {
};
_ProjectsModule.\u0275fac = function ProjectsModule_Factory(t) {
  return new (t || _ProjectsModule)();
};
_ProjectsModule.\u0275mod = /* @__PURE__ */ i05.\u0275\u0275defineNgModule({ type: _ProjectsModule });
_ProjectsModule.\u0275inj = /* @__PURE__ */ i05.\u0275\u0275defineInjector({ imports: [
  CommonModule,
  ProjectsRoutingModule,
  SharedModule
] });
var ProjectsModule = _ProjectsModule;
export {
  ProjectsModule
};
