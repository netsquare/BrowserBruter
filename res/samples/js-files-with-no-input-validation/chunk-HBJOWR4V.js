import {a as Le} from "./chunk-4P4XUNAJ.js";
import {a as tt} from "./chunk-DOWJEEJT.js";
import {a as H} from "./chunk-H4CDKMYC.js";
import {a as he, b as ie} from "./chunk-G2AXRP7G.js";
import {d as ue} from "./chunk-XUYHT7WP.js";
import {Aa as le, Ab as Q, B as h, Bb as _e, C as g, Ea as ae, Ec as Re, Fb as Z, Fc as We, Ga as se, Gb as fe, Hb as ve, Hc as Ue, Ic as Ae, Jb as je, Jc as Be, Ka as B, Kc as qe, Ma as ce, Mb as we, Mc as Ke, N as p, Na as q, Nb as Se, Nc as Ge, O as P, Ob as ye, Oc as He, Pb as Ce, Pc as Je, Qa as K, Qb as Pe, Ra as me, Rb as be, Rc as Ye, T as f, V as u, Va as te, Vb as Me, W as ee, Xc as Qe, Ya as de, Zc as Ze, _b as ze, _c as Xe, ad as $e, ba as n, ca as r, da as j, ga as x, ha as _, hb as G, ia as v, ib as pe, jd as et, kb as ne, lc as xe, mb as F, mc as Ve, nc as Te, pa as k, pc as ke, qa as c, qc as Fe, r as re, s as W, sa as V, sc as De, tb as J, tc as Ie, u as oe, va as S, vc as Ee, wa as y, wb as ge, x as U, xa as C, xb as Y, y as A, yc as Ne, zb as b, zc as Oe} from "./chunk-GH2TFUDD.js";
import "./chunk-RVFOIZLJ.js";
var $ = ( () => {
    let d = class d {
        constructor(t) {
            this.http = t
        }
        GetProjectList(t, o, e, a) {
            let s = new te;
            return s = s.set("page", t),
            s = s.set("limit", o),
            e?.length !== 0 && e.key && e.value && (s = s.set("type", "search"),
            s = s.set("key", e.key),
            s = s.set("value", e.value)),
            a && a.key && a.value && (s = s.set("type", "sort"),
            s = s.set("key", a.key),
            s = s.set("value", a.value)),
            this.http.get(`${F.PROJECTS_LIST}?`, {
                params: s
            })
        }
        GetOrgProjectList(t, o, e, a, s) {
            let l = new te;
            return l = l.set("page", o),
            l = l.set("limit", e),
            a?.length !== 0 && a.key && a.value && (l = l.set("type", "search"),
            l = l.set("key", a.key),
            l = l.set("value", a.value)),
            s && s.key && s.value && (l = l.set("type", "sort"),
            l = l.set("key", s.key),
            l = l.set("value", s.value)),
            this.http.get(`${F.PROJECTS_ORG_LIST}/${t}?`, {
                params: l
            })
        }
        ProjectAdd(t) {
            return this.http.post(F.PROJECT_ADD, t)
        }
        ProjectEdit(t) {
            return this.http.put(F.PROJECT_EDIT, t)
        }
        ProjectDetails(t) {
            return this.http.get(`${F.PROJECT_DETAILS}/${t}`)
        }
        ProjectDelete(t) {
            return this.http.post(F.PROJECT_DELETE, t)
        }
        GetNetwork() {
            return this.http.get(`${F.NETWORK}`)
        }
    }
    ;
    d.\u0275fac = function(o) {
        return new (o || d)(oe(de))
    }
    ,
    d.\u0275prov = re({
        token: d,
        factory: d.\u0275fac,
        providedIn: "root"
    });
    let i = d;
    return i
}
)();
function pt(i, d) {
    if (i & 1) {
        let m = x();
        n(0, "button", 59),
        _("click", function() {
            h(m);
            let o = v();
            return g(o.addRow())
        }),
        j(1, "i", 60),
        c(2, " Add Project "),
        r()
    }
}
function ut(i, d) {
    if (i & 1) {
        let m = x();
        n(0, "a", 61),
        _("nzOnConfirm", function() {
            h(m);
            let o = v();
            return g(o.projectDelete())
        }),
        n(1, "button", 62),
        j(2, "span", 63),
        r()()
    }
    if (i & 2) {
        let m = v();
        p(),
        u("nzTooltipColor", m.color)
    }
}
function ht(i, d) {
    if (i & 1) {
        let m = x();
        n(0, "th", 64),
        _("nzCheckedChange", function(o) {
            h(m);
            let e = v();
            return g(e.onAllChecked(o))
        }),
        r()
    }
    if (i & 2) {
        let m = v();
        u("nzChecked", m.listOfprojects.length ? m.checked : !1)("nzIndeterminate", m.indeterminate)
    }
}
function gt(i, d) {
    if (i & 1) {
        let m = x();
        n(0, "td", 72),
        _("nzCheckedChange", function(o) {
            h(m);
            let e = v().$implicit
              , a = v(2);
            return g(a.onItemChecked(e._id, o))
        }),
        r()
    }
    if (i & 2) {
        let m = v().$implicit
          , t = v(2);
        u("nzChecked", t.setOfCheckedId.has(m._id))("nzLabel", m.name)
    }
}
function _t(i, d) {
    if (i & 1) {
        let m = x();
        n(0, "tr", 66),
        _("click", function() {
            let o = h(m).$implicit
              , e = v(2);
            return g((e.canManageProject || e.isAdmin) && e.editRow(o._id))
        }),
        f(1, gt, 1, 2, "td", 67),
        n(2, "td", 68),
        c(3),
        r(),
        n(4, "td", 68),
        c(5),
        r(),
        n(6, "td", 68),
        c(7),
        r(),
        n(8, "td"),
        c(9),
        ae(10, "date"),
        r(),
        n(11, "td", 69),
        _("click", function() {
            let o = h(m).$implicit
              , e = v(2);
            return g(e.getProjectTestList(o._id))
        }),
        c(12),
        r(),
        n(13, "td")(14, "div", 70),
        j(15, "input", 71),
        r()()()
    }
    if (i & 2) {
        let m = d.$implicit
          , t = v(2);
        p(),
        u("ngIf", t.canManageProject || t.isAdmin),
        p(),
        u("nzTooltipTitle", m == null ? null : m.projectName)("nzTooltipColor", t.color),
        p(),
        V(" ", m.projectName, " "),
        p(),
        u("nzTooltipTitle", m == null ? null : m.nwPlacementName)("nzTooltipColor", t.color),
        p(),
        V(" ", m.nwPlacementName, " "),
        p(),
        u("nzTooltipTitle", m == null ? null : m.orgName)("nzTooltipColor", t.color),
        p(),
        V(" ", m == null ? null : m.orgName, " "),
        p(2),
        V(" ", se(10, 13, m.creationDate, "dd-MM-yyyy"), " "),
        p(3),
        V(" ", m.totalTests, " "),
        p(3),
        u("checked", m.isSensitive)
    }
}
function ft(i, d) {
    if (i & 1 && (n(0, "tbody"),
    f(1, _t, 16, 16, "tr", 65),
    r()),
    i & 2) {
        let m = v();
        p(),
        u("ngForOf", m.listOfprojects)
    }
}
function vt(i, d) {
    i & 1 && c(0, "Prev")
}
function jt(i, d) {
    i & 1 && c(0, "Next")
}
function wt(i, d) {
    if (i & 1) {
        let m = x();
        n(0, "div", 11)(1, "div", 73)(2, "div", 74),
        c(3),
        r()(),
        n(4, "div", 75)(5, "ngb-pagination", 76),
        C("pageChange", function(o) {
            h(m);
            let e = v();
            return y(e.pageIndex, o) || (e.pageIndex = o),
            g(o)
        }),
        f(6, vt, 1, 0, "ng-template", 77)(7, jt, 1, 0, "ng-template", 78),
        r()()()
    }
    if (i & 2) {
        let m = v();
        p(3),
        V(" ", m.currentPageRange, " "),
        p(2),
        u("collectionSize", m.totalRecords),
        S("page", m.pageIndex),
        u("pageSize", m.pageSize)("pageSize", m.pageSize)("maxSize", 5)("rotate", !0)("ellipses", !1)("boundaryLinks", !1)
    }
}
var it = ( () => {
    let d = class d {
        constructor(t, o, e, a, s, l, w) {
            this.router = t,
            this.toastr = o,
            this.projectsService = e,
            this.location = a,
            this.userService = s,
            this.loaderService = l,
            this.dateFilterService = w,
            this.totalRecords = 0,
            this.totalPages = 1,
            this.loading = !1,
            this.pageSize = 10,
            this.pageIndex = 1,
            this.onKeyString = "",
            this.currentPageRange = "",
            this.proSearchValue = "",
            this.isproSearchValue = !1,
            this.orgSearchValue = [],
            this.nwPlacementNameSearchValue = [],
            this.isOrgSearchValue = !1,
            this.isnwPlacementNameSearchValue = !1,
            this.iscreationDateSearchValue = !1,
            this.isTotalTests = !1,
            this.listOfprojects = [],
            this.state = this.location.getState(),
            this.startDate = "",
            this.endDate = "",
            this.color = "black",
            this.canManageProject = !1,
            this.isAdmin = !1,
            this.checked = !1,
            this.indeterminate = !1,
            this.searchData = [],
            this.isResizing = !1,
            this.customColumn = [{
                column: "projectName",
                width: "250px"
            }, {
                column: "orgName",
                width: "250px"
            }],
            this.listOfCurrentPageData = [],
            this.setOfCheckedId = new Set
        }
        ngOnInit() {
            this.orgId = this.state?.data,
            this.accsssData()
        }
        accsssData() {
            let t = this.userService.getUserAccessData();
            this.canManageProject = t[0]?.canManageProject
        }
        loadDataFromServer(t, o, e, a, s) {
            this.loading = !0,
            this.projectsService.GetProjectList(t, o, s, a).subscribe({
                next: l => {
                    if (l.status === !0) {
                        if (!l.data.length) {
                            this.listOfprojects = [],
                            this.loading = !1;
                            return
                        }
                        let w = l.data;
                        this.listOfprojects = w,
                        this.totalRecords = l.totalRecords,
                        this.isAdmin = l?.isAdmin,
                        this.onCurrentPageDataChange(this.listOfprojects),
                        this.calculatePageRange(),
                        this.loading = !1
                    }
                }
                ,
                error: l => (this.loading = !1,
                this.toastr.error(l.error.message, "Projects Management"))
            })
        }
        projectByOrg(t, o, e, a, s, l) {
            this.loading = !0,
            this.projectsService.GetOrgProjectList(this.orgId, o, e, l, s).subscribe({
                next: w => {
                    if (w.status === !0) {
                        let M = w.data;
                        this.listOfprojects = M,
                        this.onCurrentPageDataChange(this.listOfprojects),
                        this.calculatePageRange(),
                        this.loading = !1
                    }
                }
                ,
                error: w => (this.loading = !1,
                this.toastr.error(w.error.message, "Projects Management"))
            })
        }
        onQueryParamsChange(t) {
            let {pageSize: o, pageIndex: e, sort: a, filter: s} = t
              , l = a.find(T => T.value !== null)
              , w = l && l.key || null
              , M = l && l.value || null
              , z = this.searchData.key && this.searchData.value !== null ? null : {
                type: "sort",
                key: w,
                value: M
            };
            this.orgId ? this.projectByOrg(this.orgId, e, o, w, z, this.searchData) : this.loadDataFromServer(e, o, w, z, this.searchData)
        }
        resetPageIndex() {
            this.pageIndex = 1
        }
        getProjectTestList(t) {
            this.toastr.success("Test list", "Projects Management"),
            this.router.navigate(["/main/tests_management/test_list"], {
                state: {
                    projectId: t
                }
            })
        }
        reset() {
            this.startDate = "",
            this.endDate = "",
            this.orgSearchValue = "",
            this.nwPlacementNameSearchValue = "",
            this.creationDateSearchValue = "",
            this.proSearchValue = "",
            this.isproSearchValue = !1,
            this.isnwPlacementNameSearchValue = !1,
            this.isOrgSearchValue = !1,
            this.iscreationDateSearchValue = !1,
            this.isTotalTests = !1,
            this.totalTestsValue = "",
            this.searchData = [],
            this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, [])
        }
        onKeyUp(t, o) {
            this.onKeyString += o.key,
            setTimeout( () => {
                this.search(t, this.onKeyString)
            }
            , 1e3)
        }
        onChange(t) {
            t && (this.creationDateSearchValue = t)
        }
        addRow() {
            this.router.navigate(["/main/projects_management/projects_update"], {
                state: {
                    orgId: this.orgId
                }
            })
        }
        editRow(t) {
            this.router.navigate(["/main/projects_management/projects_update"], {
                state: {
                    projectId: t
                }
            })
        }
        projectDelete() {
            this.loading = !0;
            let t = [...this.setOfCheckedId];
            this.projectsService.ProjectDelete({
                projectIds: t
            }).subscribe({
                next: o => {
                    o.status === !0 && (this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, []),
                    this.setOfCheckedId = new Set([...this.setOfCheckedId].filter(e => !t.includes(e))),
                    this.toastr.success(o.message, "Projects Management"),
                    this.loading = !1)
                }
                ,
                error: o => (this.loading = !1,
                this.toastr.error(o.error.message, "Projects Management"))
            })
        }
        updateCheckedSet(t, o) {
            o ? this.setOfCheckedId.add(t) : this.setOfCheckedId.delete(t)
        }
        onCurrentPageDataChange(t) {
            this.listOfCurrentPageData = t,
            this.refreshCheckedStatus()
        }
        refreshCheckedStatus() {
            let t = this.listOfCurrentPageData.filter( ({disabled: o}) => !o);
            this.checked = t.every( ({_id: o}) => this.setOfCheckedId.has(o)),
            this.indeterminate = t.some( ({_id: o}) => this.setOfCheckedId.has(o)) && !this.checked
        }
        onItemChecked(t, o) {
            this.updateCheckedSet(t, o),
            this.refreshCheckedStatus()
        }
        onAllChecked(t) {
            this.listOfCurrentPageData.filter( ({disabled: o}) => !o).forEach( ({_id: o}) => this.updateCheckedSet(o, t)),
            this.refreshCheckedStatus()
        }
        calculatePageRange() {
            let t = (this.pageIndex - 1) * this.pageSize + 1
              , o = Math.min(this.pageIndex * this.pageSize, this.totalRecords);
            this.totalPages = Math.ceil(this.totalRecords / this.pageSize),
            this.currentPageRange = `Showing ${t} to ${o} of ${this.totalRecords} entries`
        }
        changePage(t) {
            t > 0 && t <= this.totalPages && (this.pageIndex = t,
            this.calculatePageRange())
        }
        get pages() {
            let o = [];
            if (this.totalPages <= 2)
                for (let e = 1; e <= this.totalPages; e++)
                    o.push(e);
            else {
                let e = Math.max(this.pageIndex - 2, 1)
                  , a = Math.min(e + 2 - 1, this.totalPages);
                a - e < 1 && (e = Math.max(a - 2 + 1, 1));
                for (let s = e; s <= a; s++)
                    o.push(s);
                e > 1 && (o.unshift("..."),
                o.unshift(1)),
                a < this.totalPages && (o.push("..."),
                o.push(this.totalPages))
            }
            return o
        }
        padWithZero(t) {
            return t.toString().padStart(2, "0")
        }
        search(t, o) {
            this.pageIndex = 1,
            t === "projectName" ? (this.isproSearchValue = !1,
            this.searchData = {
                type: "search",
                key: t,
                value: this.proSearchValue
            },
            this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : t === "nwPlacementName" ? (this.isnwPlacementNameSearchValue = !1,
            this.searchData = {
                type: "search",
                key: t,
                value: this.nwPlacementNameSearchValue
            },
            this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : t === "orgName" ? (this.isOrgSearchValue = !1,
            this.searchData = {
                type: "search",
                key: t,
                value: this.orgSearchValue
            },
            this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : t === "totalTests" ? (this.isTotalTests = !1,
            this.searchData = {
                type: "search",
                key: t,
                value: this.totalTestsValue
            },
            this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : t === "creationDate" ? (this.iscreationDateSearchValue = !1,
            this.creationDateSearchValue = this.startDate,
            this.searchData = {
                type: "search",
                key: t,
                value: `${this.startDate}to${this.endDate}`
            },
            this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, [])
        }
        onEnter(t) {
            this.pageIndex = 1,
            this.search(t)
        }
        onKeydown(t) {
            this.pageIndex = 1,
            this.debounceTimeout && clearTimeout(this.debounceTimeout),
            this.debounceTimeout = setTimeout( () => {
                t === "projectName" ? (this.searchData = {
                    type: "search",
                    key: t,
                    value: this.proSearchValue
                },
                this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : t === "nwPlacementName" ? (this.searchData = {
                    type: "search",
                    key: t,
                    value: this.nwPlacementNameSearchValue
                },
                this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : t === "orgName" ? (this.searchData = {
                    type: "search",
                    key: t,
                    value: this.orgSearchValue
                },
                this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : t === "creationDate" ? (this.searchData = {
                    type: "search",
                    key: t,
                    value: this.creationDateSearchValue
                },
                this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : t === "totalTests" ? (this.searchData = {
                    type: "search",
                    key: t,
                    value: this.totalTestsValue
                },
                this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, this.searchData)) : this.loadDataFromServer(this.pageIndex, this.pageSize, null, null, [])
            }
            , 2e3)
        }
        selectDateRange(t, o) {
            let {startDate: e, endDate: a} = this.dateFilterService.getDateRange(t);
            this.startDate = e,
            this.endDate = a,
            this.search(o)
        }
        updateHoveredDate(t) {
            let {startDate: o, endDate: e} = this.dateFilterService.updateHoveredDate(t);
            this.startDate = o,
            this.endDate = e
        }
        allowOnlyNumbers(t) {
            let o = t.key;
            !/^[0-9]$/.test(o) && o !== "Backspace" && o !== "Delete" && o !== "ArrowLeft" && o !== "ArrowRight" && t.preventDefault()
        }
        getWidthInPixels(t) {
            return parseInt(t, 10)
        }
        onResizeStart() {
            this.isResizing = !0
        }
        onResize(t, o, e, a) {
            if (t.width) {
                let s = Math.max(t.width, e);
                s = Math.min(s, a),
                this.customColumn[o].width = `${s}px`,
                this.customColumn = [...this.customColumn]
            }
        }
        onResizeEnd() {
            this.isResizing = !1
        }
    }
    ;
    d.\u0275fac = function(o) {
        return new (o || d)(P(G),P(J),P($),P(B),P(he),P(H),P(tt))
    }
    ,
    d.\u0275cmp = U({
        type: d,
        selectors: [["app-projects-lists"]],
        decls: 134,
        vars: 48,
        consts: [["projectSearch", "nzDropdownMenu"], ["nwPlacementNameSearch", "nzDropdownMenu"], ["orgSearch", "nzDropdownMenu"], ["totalTests", "nzDropdownMenu"], ["dateFilter", "nzDropdownMenu"], [1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "mb-3", "mb-md-0"], [1, "d-flex", "align-items-center", "flex-wrap", "text-nowrap"], ["type", "button", "class", "btn btn-primary btn-icon-text mb-2 mb-md-0", 3, "click", 4, "ngIf"], [1, "row"], [1, "col-md-12", "stretch-card"], [1, "card"], [1, "card-body"], [1, "dataTable-top"], [1, "dataTable-dropdown"], [1, "dataTable-selector", 3, "ngModelChange", "change", "ngModel"], ["value", "10", "selected", ""], ["value", "15"], ["value", "20"], ["value", "25"], [1, "d-flex", "justify-content-end"], ["nz-popconfirm", "", "nzPopconfirmTitle", "Sure to delete?", 3, "nzOnConfirm", 4, "ngIf"], [1, "table-container", "dataTable"], ["nzShowSizeChanger", "", 3, "nzQueryParams", "nzCurrentPageDataChange", "nzData", "nzShowPagination", "nzLoading", "nzTotal", "nzPageSize", "nzPageIndex"], ["class", "check-Box-Width", "nzLabel", "Select all", 3, "nzChecked", "nzIndeterminate", "nzCheckedChange", 4, "ngIf"], ["id", "1", "nzColumnKey", "projectName", "nzCustomFilter", "", "nz-resizable", "", "nzBounds", "window", 1, "resize-column", 3, "nzResizeStart", "nzResize", "nzResizeEnd", "nzSortFn", "nzSortPriority", "nzWidth", "nzShowSort"], [3, "nzVisibleChange", "nzVisible", "nzActive", "nzDropdownMenu"], ["nz-icon", "", "nzType", "search"], ["nzDirection", "right"], [1, "resize-handle-inner"], ["id", "2", "nzColumnKey", "nwPlacementName", "nzCustomFilter", "", 3, "nzSortFn"], ["id", "1", "nzColumnKey", "orgName", "nzCustomFilter", "", "nz-resizable", "", "nzBounds", "window", 1, "resize-column", 3, "nzResizeStart", "nzResize", "nzResizeEnd", "nzSortFn", "nzSortPriority", "nzWidth", "nzShowSort"], ["id", "3", "nzColumnKey", "creationDate", "nzCustomFilter", "", 3, "nzSortFn"], ["id", "5", "nzColumnKey", "totalTests", "nzCustomFilter", "", 3, "nzSortFn"], [3, "nzVisibleChange", "nzVisible", "nzDropdownMenu"], ["id", "5"], [4, "ngIf"], ["class", "row", 4, "ngIf"], [1, "ant-table-filter-dropdown"], [1, "search-box"], ["type", "text", "nz-input", "", "placeholder", "Search project name", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "button", 1, "btn", "searchbtn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["type", "button", 1, "btn", "searchbtn", "btn-outline-primary", "btn-icon-text", "me-2", "mb-2", "mb-md-0", 3, "click"], ["type", "text", "nz-input", "", "placeholder", "Search network placement", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "text", "nz-input", "", "placeholder", "Search organization name", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], ["type", "text", "nz-input", "", "placeholder", "Enter total tests", 3, "ngModelChange", "keydown", "keydown.enter", "keypress", "ngModel"], [1, "col-md-12"], ["type", "text", "nz-input", "", "placeholder", "Enter date", 1, "clsInput", 3, "ngModelChange", "keydown", "keydown.enter", "ngModel"], [1, "list-group"], ["type", "button", 1, "list-group-item", "list-group-item-action", "dayBtn", 3, "mouseenter", "click"], [1, "my-2", "d-flex"], [1, "col"], [1, "form-label"], ["mask", "d0/M0/yyyy", "placeholder", "dd/mm/yyyy", "readonly", "", 1, "form-control", "mb-4", "me-2", "mb-md-0", "dateSearch", 3, "ngModelChange", "ngModel"], ["mask", "d0/M0/yyyy", "placeholder", "dd/mm/yyyy", "readonly", "", 1, "form-control", "mb-4", "mb-md-0", "dateSearch", 3, "ngModelChange", "ngModel"], [1, "col", "d-flex", "justify-content-end"], ["type", "button", 1, "btn", "searchbtn", "colsureButton", "btn-outline-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["type", "button", 1, "btn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], ["data-feather", "plus", "appFeatherIcon", "", 1, "btn-icon-prepend"], ["nz-popconfirm", "", "nzPopconfirmTitle", "Sure to delete?", 3, "nzOnConfirm"], ["nz-button", "", "nzType", "primary", "nzSize", "large", "nzTooltipTitle", "Delete All Project", "nzTooltipPlacement", "top", "nz-tooltip", "", 3, "nzTooltipColor"], ["nz-icon", "", "nzType", "delete", "nzTheme", "outline"], ["nzLabel", "Select all", 1, "check-Box-Width", 3, "nzCheckedChange", "nzChecked", "nzIndeterminate"], [3, "click", 4, "ngFor", "ngForOf"], [3, "click"], ["class", "check-Box-Width", 3, "nzChecked", "nzLabel", "nzCheckedChange", 4, "ngIf"], ["nz-tooltip", "", "nzTooltipPlacement", "top", "nz-button", "", 1, "ellipsis", 3, "nzTooltipTitle", "nzTooltipColor"], [1, "text-center", 3, "click"], [1, "text-center"], ["type", "checkbox", "id", "isSensitive", "disabled", "", 1, "form-check-input", 3, "checked"], [1, "check-Box-Width", 3, "nzCheckedChange", "nzChecked", "nzLabel"], [1, "col-sm-6", "col-md-5"], ["id", "dataTableExample_info", "role", "status", "aria-live", "polite", 1, "dataTables_info"], [1, "col-sm-6", "col-md-7"], [1, "d-flex", "justify-content-end", 3, "pageChange", "collectionSize", "page", "pageSize", "maxSize", "rotate", "ellipses", "boundaryLinks"], ["ngbPaginationPrevious", ""], ["ngbPaginationNext", ""]],
        template: function(o, e) {
            if (o & 1) {
                let a = x();
                n(0, "div", 5)(1, "div", 6)(2, "div", 7)(3, "div")(4, "h4", 8),
                c(5, "Projects Management"),
                r()(),
                n(6, "div", 9),
                f(7, pt, 3, 0, "button", 10),
                r()()()(),
                n(8, "div", 11)(9, "div", 12)(10, "div", 13)(11, "div", 14)(12, "div", 15)(13, "div", 16)(14, "label")(15, "select", 17),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.pageSize, l) || (e.pageSize = l),
                    g(l)
                }),
                _("change", function() {
                    return h(a),
                    g(e.resetPageIndex())
                }),
                n(16, "option", 18),
                c(17, "10"),
                r(),
                n(18, "option", 19),
                c(19, "15"),
                r(),
                n(20, "option", 20),
                c(21, "20"),
                r(),
                n(22, "option", 21),
                c(23, "25"),
                r()(),
                c(24, " Entries per page"),
                r()(),
                n(25, "div", 22),
                f(26, ut, 3, 1, "a", 23),
                r()(),
                n(27, "div", 24)(28, "nz-table", 25),
                _("nzQueryParams", function(l) {
                    return h(a),
                    g(e.onQueryParamsChange(l))
                })("nzCurrentPageDataChange", function(l) {
                    return h(a),
                    g(e.onCurrentPageDataChange(l))
                }),
                n(29, "thead")(30, "tr"),
                f(31, ht, 1, 2, "th", 26),
                n(32, "th", 27),
                _("nzResizeStart", function() {
                    return h(a),
                    g(e.onResizeStart())
                })("nzResize", function(l) {
                    return h(a),
                    g(e.onResize(l, 0, 100, 850))
                })("nzResizeEnd", function() {
                    return h(a),
                    g(e.onResizeEnd())
                }),
                c(33, " Project "),
                n(34, "nz-filter-trigger", 28),
                C("nzVisibleChange", function(l) {
                    return h(a),
                    y(e.isproSearchValue, l) || (e.isproSearchValue = l),
                    g(l)
                }),
                j(35, "span", 29),
                r(),
                n(36, "nz-resize-handle", 30),
                j(37, "div", 31),
                r()(),
                n(38, "th", 32),
                c(39, " Network Placement "),
                n(40, "nz-filter-trigger", 28),
                C("nzVisibleChange", function(l) {
                    return h(a),
                    y(e.isnwPlacementNameSearchValue, l) || (e.isnwPlacementNameSearchValue = l),
                    g(l)
                }),
                j(41, "span", 29),
                r()(),
                n(42, "th", 33),
                _("nzResizeStart", function() {
                    return h(a),
                    g(e.onResizeStart())
                })("nzResize", function(l) {
                    return h(a),
                    g(e.onResize(l, 1, 100, 850))
                })("nzResizeEnd", function() {
                    return h(a),
                    g(e.onResizeEnd())
                }),
                c(43, " Organization "),
                n(44, "nz-filter-trigger", 28),
                C("nzVisibleChange", function(l) {
                    return h(a),
                    y(e.isOrgSearchValue, l) || (e.isOrgSearchValue = l),
                    g(l)
                }),
                j(45, "span", 29),
                r(),
                n(46, "nz-resize-handle", 30),
                j(47, "div", 31),
                r()(),
                n(48, "th", 34),
                c(49, " Creation Date "),
                n(50, "nz-filter-trigger", 28),
                C("nzVisibleChange", function(l) {
                    return h(a),
                    y(e.iscreationDateSearchValue, l) || (e.iscreationDateSearchValue = l),
                    g(l)
                }),
                j(51, "span", 29),
                r()(),
                n(52, "th", 35),
                c(53, " Total tests "),
                n(54, "nz-filter-trigger", 36),
                C("nzVisibleChange", function(l) {
                    return h(a),
                    y(e.isTotalTests, l) || (e.isTotalTests = l),
                    g(l)
                }),
                j(55, "span", 29),
                r()(),
                n(56, "th", 37),
                c(57, "Sensitive flag"),
                r()()(),
                f(58, ft, 2, 1, "tbody", 38),
                r()(),
                f(59, wt, 8, 9, "div", 39),
                n(60, "nz-dropdown-menu", null, 0)(62, "div", 40)(63, "div", 41)(64, "input", 42),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.proSearchValue, l) || (e.proSearchValue = l),
                    g(l)
                }),
                _("keydown", function() {
                    return h(a),
                    g(e.onKeydown("projectName"))
                })("keydown.enter", function() {
                    return h(a),
                    g(e.onEnter("projectName"))
                }),
                r(),
                n(65, "button", 43),
                _("click", function() {
                    return h(a),
                    g(e.search("projectName"))
                }),
                c(66, " Search"),
                r(),
                c(67, "\xA0\xA0\xA0 "),
                n(68, "button", 44),
                _("click", function() {
                    return h(a),
                    g(e.reset())
                }),
                c(69, " Reset "),
                r()()()(),
                n(70, "nz-dropdown-menu", null, 1)(72, "div", 40)(73, "div", 41)(74, "input", 45),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.nwPlacementNameSearchValue, l) || (e.nwPlacementNameSearchValue = l),
                    g(l)
                }),
                _("keydown", function() {
                    return h(a),
                    g(e.onKeydown("nwPlacementName"))
                })("keydown.enter", function() {
                    return h(a),
                    g(e.onEnter("nwPlacementName"))
                }),
                r(),
                n(75, "button", 43),
                _("click", function() {
                    return h(a),
                    g(e.search("nwPlacementName"))
                }),
                c(76, " Search"),
                r(),
                c(77, "\xA0\xA0\xA0 "),
                n(78, "button", 44),
                _("click", function() {
                    return h(a),
                    g(e.reset())
                }),
                c(79, " Reset "),
                r()()()(),
                n(80, "nz-dropdown-menu", null, 2)(82, "div", 40)(83, "div", 41)(84, "input", 46),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.orgSearchValue, l) || (e.orgSearchValue = l),
                    g(l)
                }),
                _("keydown", function() {
                    return h(a),
                    g(e.onKeydown("orgName"))
                })("keydown.enter", function() {
                    return h(a),
                    g(e.onEnter("orgName"))
                }),
                r(),
                n(85, "button", 43),
                _("click", function() {
                    return h(a),
                    g(e.search("orgName"))
                }),
                c(86, " Search"),
                r(),
                c(87, "\xA0\xA0\xA0 "),
                n(88, "button", 44),
                _("click", function() {
                    return h(a),
                    g(e.reset())
                }),
                c(89, " Reset "),
                r()()()(),
                n(90, "nz-dropdown-menu", null, 3)(92, "div", 40)(93, "div", 41)(94, "input", 47),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.totalTestsValue, l) || (e.totalTestsValue = l),
                    g(l)
                }),
                _("keydown", function() {
                    return h(a),
                    g(e.onKeydown("totalTests"))
                })("keydown.enter", function() {
                    return h(a),
                    g(e.onEnter("totalTests"))
                })("keypress", function(l) {
                    return h(a),
                    g(e.allowOnlyNumbers(l))
                }),
                r(),
                n(95, "button", 43),
                _("click", function() {
                    return h(a),
                    g(e.search("totalTests"))
                }),
                c(96, " Search"),
                r(),
                c(97, "\xA0\xA0\xA0 "),
                n(98, "button", 44),
                _("click", function() {
                    return h(a),
                    g(e.reset())
                }),
                c(99, " Reset "),
                r()()()(),
                n(100, "nz-dropdown-menu", null, 4)(102, "div", 40)(103, "div", 41)(104, "div", 11)(105, "div", 48)(106, "input", 49),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.startDate, l) || (e.startDate = l),
                    g(l)
                }),
                _("keydown", function() {
                    return h(a),
                    g(e.onKeydown("creationDate"))
                })("keydown.enter", function() {
                    return h(a),
                    g(e.onEnter("creationDate"))
                }),
                r(),
                n(107, "div", 50)(108, "button", 51),
                _("mouseenter", function() {
                    return h(a),
                    g(e.updateHoveredDate("Today"))
                })("click", function() {
                    return h(a),
                    g(e.selectDateRange("Today", "creationDate"))
                }),
                c(109, " Today "),
                r(),
                n(110, "button", 51),
                _("mouseenter", function() {
                    return h(a),
                    g(e.updateHoveredDate("Yesterday"))
                })("click", function() {
                    return h(a),
                    g(e.selectDateRange("Yesterday", "creationDate"))
                }),
                c(111, " Yesterday "),
                r(),
                n(112, "button", 51),
                _("mouseenter", function() {
                    return h(a),
                    g(e.updateHoveredDate("Last 7 Days"))
                })("click", function() {
                    return h(a),
                    g(e.selectDateRange("Last 7 Days", "creationDate"))
                }),
                c(113, " Last 7 Days "),
                r(),
                n(114, "button", 51),
                _("mouseenter", function() {
                    return h(a),
                    g(e.updateHoveredDate("Last 30 Days"))
                })("click", function() {
                    return h(a),
                    g(e.selectDateRange("Last 30 Days", "creationDate"))
                }),
                c(115, " Last 30 Days "),
                r(),
                n(116, "button", 51),
                _("mouseenter", function() {
                    return h(a),
                    g(e.updateHoveredDate("This Month"))
                })("click", function() {
                    return h(a),
                    g(e.selectDateRange("This Month", "creationDate"))
                }),
                c(117, " This Month "),
                r(),
                n(118, "button", 51),
                _("mouseenter", function() {
                    return h(a),
                    g(e.updateHoveredDate("Last Month"))
                })("click", function() {
                    return h(a),
                    g(e.selectDateRange("Last Month", "creationDate"))
                }),
                c(119, " Last Month "),
                r(),
                n(120, "button", 51),
                _("mouseenter", function() {
                    return h(a),
                    g(e.updateHoveredDate("Last Year"))
                })("click", function() {
                    return h(a),
                    g(e.selectDateRange("Last Year", "creationDate"))
                }),
                c(121, " Last Year "),
                r()()()(),
                n(122, "div", 52)(123, "div", 53)(124, "label", 54),
                c(125, "From"),
                r(),
                n(126, "input", 55),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.startDate, l) || (e.startDate = l),
                    g(l)
                }),
                r()(),
                n(127, "div", 53)(128, "label", 54),
                c(129, "To"),
                r(),
                n(130, "input", 56),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.endDate, l) || (e.endDate = l),
                    g(l)
                }),
                r()()(),
                n(131, "div", 57)(132, "button", 58),
                _("click", function() {
                    return h(a),
                    g(e.reset())
                }),
                c(133, " Reset "),
                r()()()()()()()()()
            }
            if (o & 2) {
                let a = k(61)
                  , s = k(71)
                  , l = k(81)
                  , w = k(91)
                  , M = k(101);
                p(7),
                u("ngIf", e.canManageProject || e.isAdmin),
                p(8),
                S("ngModel", e.pageSize),
                p(11),
                u("ngIf", e.setOfCheckedId.size > 0),
                p(2),
                u("nzData", e.listOfprojects)("nzShowPagination", !1)("nzLoading", e.loading)("nzTotal", e.totalRecords)("nzPageSize", e.pageSize)("nzPageIndex", e.pageIndex),
                p(3),
                u("ngIf", e.canManageProject || e.isAdmin),
                p(),
                ee("width", e.customColumn[0].width),
                u("nzSortFn", !0)("nzSortPriority", !0)("nzWidth", e.getWidthInPixels(e.customColumn[0].width))("nzShowSort", !e.isResizing),
                p(2),
                S("nzVisible", e.isproSearchValue),
                u("nzActive", e.proSearchValue.length > 0)("nzDropdownMenu", a),
                p(4),
                u("nzSortFn", !0),
                p(2),
                S("nzVisible", e.isnwPlacementNameSearchValue),
                u("nzActive", e.nwPlacementNameSearchValue.length > 0)("nzDropdownMenu", s),
                p(2),
                ee("width", e.customColumn[1].width),
                u("nzSortFn", !0)("nzSortPriority", !0)("nzWidth", e.getWidthInPixels(e.customColumn[1].width))("nzShowSort", !e.isResizing),
                p(2),
                S("nzVisible", e.isOrgSearchValue),
                u("nzActive", e.orgSearchValue.length > 0)("nzDropdownMenu", l),
                p(4),
                u("nzSortFn", !0),
                p(2),
                S("nzVisible", e.iscreationDateSearchValue),
                u("nzActive", (e.creationDateSearchValue == null ? null : e.creationDateSearchValue.length) > 0)("nzDropdownMenu", M),
                p(2),
                u("nzSortFn", !0),
                p(2),
                S("nzVisible", e.isTotalTests),
                u("nzDropdownMenu", w),
                p(4),
                u("ngIf", !e.loading),
                p(),
                u("ngIf", e.listOfprojects.length),
                p(5),
                S("ngModel", e.proSearchValue),
                p(10),
                S("ngModel", e.nwPlacementNameSearchValue),
                p(10),
                S("ngModel", e.orgSearchValue),
                p(10),
                S("ngModel", e.totalTestsValue),
                p(12),
                S("ngModel", e.startDate),
                p(20),
                S("ngModel", e.startDate),
                p(4),
                S("ngModel", e.endDate)
            }
        },
        dependencies: [ce, q, ye, Ce, Y, Se, Q, Z, Ie, Fe, De, ke, Oe, Ye, Ge, Ae, We, Be, Ue, Je, Ke, He, Re, qe, Ee, Qe, Ze, Xe, Ne, Te, xe, Ve, K],
        styles: [`.dataTable-top[_ngcontent-%COMP%]   .dataTable-dropdown[_ngcontent-%COMP%]   label[_ngcontent-%COMP%]{display:flex;align-items:center}.dayBtn[_ngcontent-%COMP%]{width:200px}.search-box[_ngcontent-%COMP%]   .colsureButton[_ngcontent-%COMP%]{width:100px}.list-group-item[_ngcontent-%COMP%]:hover, .list-group-item.active[_ngcontent-%COMP%]{background-color:#5660d9;color:#fff;cursor:pointer}.list-group[_ngcontent-%COMP%]{--bs-list-group-border-color: none;--bs-list-group-item-padding-y: 5px}.dateSearch[_ngcontent-%COMP%]{height:30px;width:100px;font-size:12px;font-weight:400}.clsInput[_ngcontent-%COMP%]{width:200px}.dataTable-top[_ngcontent-%COMP%]   .dataTable-dropdown[_ngcontent-%COMP%]   label[_ngcontent-%COMP%]   select[_ngcontent-%COMP%]{display:block;width:auto;margin-right:.5rem;padding:.469rem 2.4rem .469rem .8rem;-moz-padding-start:calc(.8rem - 3px);font-size:.875rem;font-weight:400;line-height:1.5;color:#000;background-color:#fff;background-repeat:no-repeat;background-position:right .8rem center;background-size:16px 12px;border:1px solid #e9ecef;border-radius:.25rem;transition:border-color .15s ease-in-out,box-shadow .15s ease-in-out;-webkit-appearance:none;appearance:none;outline:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath fill='none' stroke='%237987a1' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/%3E%3C/svg%3E")}`]
    });
    let i = d;
    return i
}
)();
var St = () => ({
    standalone: !0
});
function yt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter your project name! "),
    r())
}
function Ct(i, d) {
    if (i & 1 && (n(0, "div", 26),
    f(1, yt, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t = v();
        p(),
        u("ngIf", t.projectForm == null || (m = t.projectForm.get("projectName")) == null || m.errors == null ? null : m.errors.required)
    }
}
function Pt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please select organization name! "),
    r())
}
function bt(i, d) {
    if (i & 1 && (n(0, "div", 26),
    f(1, Pt, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t = v();
        p(),
        u("ngIf", t.projectForm == null || (m = t.projectForm.get("orgName")) == null || m.errors == null ? null : m.errors.required)
    }
}
function Mt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please select network placement! "),
    r())
}
function zt(i, d) {
    if (i & 1 && (n(0, "div", 26),
    f(1, Mt, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t = v();
        p(),
        u("ngIf", t.projectForm == null || (m = t.projectForm.get("nwPlacementName")) == null || m.errors == null ? null : m.errors.required)
    }
}
function xt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please select creation date! "),
    r())
}
function Vt(i, d) {
    if (i & 1 && (n(0, "div", 26),
    f(1, xt, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t = v();
        p(),
        u("ngIf", t.projectForm == null || (m = t.projectForm.get("creationDate")) == null || m.errors == null ? null : m.errors.required)
    }
}
function Tt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter info range inclusive! "),
    r())
}
function kt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function Ft(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " info range inclusive cannot be negative! "),
    r())
}
function Dt(i, d) {
    if (i & 1 && (n(0, "div", 54),
    f(1, Tt, 2, 0, "div", 53)(2, kt, 2, 0, "div", 53)(3, Ft, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("infoMin")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("infoMin")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("infoMin")) == null || o.errors == null ? null : o.errors.min)
    }
}
function It(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter info range inclusive! "),
    r())
}
function Et(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function Lt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " info range inclusive cannot be negative! "),
    r())
}
function Nt(i, d) {
    if (i & 1 && (n(0, "div", 26),
    f(1, It, 2, 0, "div", 53)(2, Et, 2, 0, "div", 53)(3, Lt, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("infoMax")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("infoMax")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("infoMax")) == null || o.errors == null ? null : o.errors.min)
    }
}
function Ot(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter low range inclusive! "),
    r())
}
function Rt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function Wt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " low range inclusive cannot be negative! "),
    r())
}
function Ut(i, d) {
    if (i & 1 && (n(0, "div", 54),
    f(1, Ot, 2, 0, "div", 53)(2, Rt, 2, 0, "div", 53)(3, Wt, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("lowMin")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("lowMin")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("lowMin")) == null || o.errors == null ? null : o.errors.min)
    }
}
function At(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter low range inclusive! "),
    r())
}
function Bt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function qt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " low range inclusive cannot be negative! "),
    r())
}
function Kt(i, d) {
    if (i & 1 && (n(0, "div", 26),
    f(1, At, 2, 0, "div", 53)(2, Bt, 2, 0, "div", 53)(3, qt, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("lowMax")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("lowMax")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("lowMax")) == null || o.errors == null ? null : o.errors.min)
    }
}
function Gt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter info range inclusive! "),
    r())
}
function Ht(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function Jt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Medium range inclusive cannot be negative! "),
    r())
}
function Yt(i, d) {
    if (i & 1 && (n(0, "div", 54),
    f(1, Gt, 2, 0, "div", 53)(2, Ht, 2, 0, "div", 53)(3, Jt, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("mediumMin")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("mediumMin")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("mediumMin")) == null || o.errors == null ? null : o.errors.min)
    }
}
function Qt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter info range inclusive! "),
    r())
}
function Zt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function Xt(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Medium range inclusive cannot be negative! "),
    r())
}
function $t(i, d) {
    if (i & 1 && (n(0, "div", 26),
    f(1, Qt, 2, 0, "div", 53)(2, Zt, 2, 0, "div", 53)(3, Xt, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("mediumMax")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("mediumMax")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("mediumMax")) == null || o.errors == null ? null : o.errors.min)
    }
}
function en(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter info range inclusive! "),
    r())
}
function tn(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function nn(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " High range inclusive cannot be negative! "),
    r())
}
function rn(i, d) {
    if (i & 1 && (n(0, "div", 54),
    f(1, en, 2, 0, "div", 53)(2, tn, 2, 0, "div", 53)(3, nn, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("highMin")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("highMin")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("highMin")) == null || o.errors == null ? null : o.errors.min)
    }
}
function on(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter info range inclusive! "),
    r())
}
function ln(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function an(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " High range inclusive cannot be negative! "),
    r())
}
function sn(i, d) {
    if (i & 1 && (n(0, "div", 26),
    f(1, on, 2, 0, "div", 53)(2, ln, 2, 0, "div", 53)(3, an, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("highMax")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("highMax")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("highMax")) == null || o.errors == null ? null : o.errors.min)
    }
}
function cn(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter info range inclusive! "),
    r())
}
function mn(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function dn(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Critical range inclusive cannot be negative! "),
    r())
}
function pn(i, d) {
    if (i & 1 && (n(0, "div", 54),
    f(1, cn, 2, 0, "div", 53)(2, mn, 2, 0, "div", 53)(3, dn, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("criticalMin")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("criticalMin")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("criticalMin")) == null || o.errors == null ? null : o.errors.min)
    }
}
function un(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Please enter info range inclusive! "),
    r())
}
function hn(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Only numbers are allowed "),
    r())
}
function gn(i, d) {
    i & 1 && (n(0, "div"),
    c(1, " Critical range inclusive cannot be negative! "),
    r())
}
function _n(i, d) {
    if (i & 1 && (n(0, "div", 26),
    f(1, un, 2, 0, "div", 53)(2, hn, 2, 0, "div", 53)(3, gn, 2, 0, "div", 53),
    r()),
    i & 2) {
        let m, t, o, e = v();
        p(),
        u("ngIf", e.projectForm == null || (m = e.projectForm.get("criticalMax")) == null || m.errors == null ? null : m.errors.required),
        p(),
        u("ngIf", e.projectForm == null || (t = e.projectForm.get("criticalMax")) == null || t.errors == null ? null : t.errors.pattern),
        p(),
        u("ngIf", e.projectForm == null || (o = e.projectForm.get("criticalMax")) == null || o.errors == null ? null : o.errors.min)
    }
}
var rt = ( () => {
    let d = class d {
        constructor(t, o, e, a, s, l, w, M, z) {
            this.fb = t,
            this.projectsService = o,
            this.toastr = e,
            this.router = a,
            this.location = s,
            this.settingsService = l,
            this.datePipe = w,
            this.CommonService = M,
            this.loaderService = z,
            this.size = "large",
            this.state = this.location.getState(),
            this.orgId = [],
            this.nwPlacementId = [],
            this.isLoading = !1
        }
        ngOnInit() {
            this.projectId = this.state?.projectId,
            this.init(),
            this.getOrgList(),
            this.getNetwork(),
            this.state?.orgId && (this.orgId = this.state?.orgId),
            this.projectId && this.projectDetails(this.projectId)
        }
        onChange(t) {
            t && t.year && t.month && t.day && this.convertDate(t)
        }
        convertDate(t) {
            let o = t.year
              , e = String(t.month).padStart(2, "0")
              , a = String(t.day).padStart(2, "0");
            t = `${o}-${e}-${a}`,
            this.projectForm.get("creationDate")?.setValue(t)
        }
        convertForUpdated(t) {
            return this.projectForm.get("creationDate")?.setValue(t),
            this.CommonService.convertDateString(t)
        }
        init() {
            this.projectForm = this.fb.group({
                projectName: ["", [b.required]],
                orgName: ["", [b.required]],
                nwPlacementName: ["", [b.required]],
                projectShortName: [""],
                projectDesc: [""],
                creationDate: ["", [b.required]],
                isSensitive: [!1],
                isActive: [!0],
                infoMin: ["", b.pattern("^[0-9]*(.[0-9]*)?$")],
                infoMax: ["", b.pattern("^[0-9]*(.[0-9]*)?$")],
                lowMin: ["", b.pattern("^[0-9]*(.[0-9]*)?$")],
                lowMax: ["", b.pattern("^[0-9]*(.[0-9]*)?$")],
                mediumMin: ["", b.pattern("^[0-9]*(.[0-9]*)?$")],
                mediumMax: ["", b.pattern("^[0-9]*(.[0-9]*)?$")],
                highMin: ["", b.pattern("^[0-9]*(.[0-9]*)?$")],
                highMax: ["", b.pattern("^[0-9]*(.[0-9]*)?$")],
                criticalMin: ["", b.pattern("^[0-9]*(.[0-9]*)?$")],
                criticalMax: ["", b.pattern("^[0-9]*(.[0-9]*)?$")]
            })
        }
        projectDetails(t) {
            this.loaderService.show(),
            this.projectsService.ProjectDetails(t).subscribe({
                next: o => {
                    if (o.status === !0) {
                        let e = o.data[0].project
                          , a = o.data[0].severity;
                        this.creationDate = this.convertForUpdated(e?.creationDate),
                        this.projectForm.patchValue({
                            projectName: e?.projectName,
                            projectShortName: e?.projectShortName,
                            projectDesc: e?.projectDesc,
                            isSensitive: e?.isSensitive,
                            isActive: e?.isActive,
                            orgName: e?.orgName,
                            infoMin: a.infoMin,
                            infoMax: a.infoMax,
                            lowMin: a.lowMin,
                            lowMax: a.lowMax,
                            mediumMin: a.mediumMin,
                            mediumMax: a.mediumMax,
                            highMin: a.highMin,
                            highMax: a.highMax,
                            criticalMin: a.criticalMin,
                            criticalMax: a.criticalMax
                        }),
                        this.orgId = e.orgId,
                        this.nwPlacementId = e.nwPlacementId,
                        this.loaderService.hide()
                    }
                }
                ,
                error: o => (this.loaderService.hide(),
                this.toastr.error(o.error.message, "Projects Management"))
            })
        }
        submitForm() {
            this.SaveData();
        }
        updateData() {
            this.loaderService.show();
            let t = this.projectForm.value
              , o = {
                projectId: this.projectId,
                projectName: t.projectName,
                projectShortName: t.projectShortName,
                projectDesc: t.projectDesc,
                orgId: this.orgId,
                nwPlacementId: this.nwPlacementId,
                languageId: "",
                isSensitive: t.isSensitive,
                isSeverity: !1,
                creationDate: t.creationDate ? t.creationDate : this.state.data.creationDate,
                isActive: t.isActive,
                severity: {
                    infoMin: t.infoMin,
                    infoMax: t.infoMax,
                    lowMin: t.lowMin,
                    lowMax: t.lowMax,
                    mediumMin: t.mediumMin,
                    mediumMax: t.mediumMax,
                    highMin: t.highMin,
                    highMax: t.highMax,
                    criticalMin: t.criticalMin,
                    criticalMax: t.criticalMax
                }
            };
            this.projectsService.ProjectEdit(o).subscribe({
                next: e => {
                    e.status === !0 && (this.toastr.success(e.message, "Projects Management"),
                    this.loaderService.hide(),
                    this.goBack())
                }
                ,
                error: e => (this.loaderService.hide(),
                this.toastr.error(e.error.message, "Projects Management"))
            })
        }
        SaveData() {
            this.loaderService.show();
            let t = this.projectForm.value
              , o = {
                projectName: t.projectName,
                projectShortName: t.projectShortName,
                projectDesc: t.projectDesc,
                orgId: this.orgId,
                nwPlacementId: this.nwPlacementId,
                languageId: "",
                isSensitive: t.isSensitive,
                isSeverity: !1,
                creationDate: t.creationDate,
                isActive: t.isActive,
                severity: {
                    infoMin: t.infoMin,
                    infoMax: t.infoMax,
                    lowMin: t.lowMin,
                    lowMax: t.lowMax,
                    mediumMin: t.mediumMin,
                    mediumMax: t.mediumMax,
                    highMin: t.highMin,
                    highMax: t.highMax,
                    criticalMin: t.criticalMin,
                    criticalMax: t.criticalMax
                }
            };
            this.projectsService.ProjectAdd(o).subscribe({
                next: e => {
                    e.status === !0 && (this.toastr.success(e.message, "Projects Management"),
                    this.loaderService.hide(),
                    this.goBack())
                }
                ,
                error: e => (this.loaderService.hide(),
                this.toastr.error(e.error.message, "Projects Management"))
            })
        }
        goBack() {
            this.router.navigate(["/main/projects_management/projects_list"])
        }
        getOrgList() {
            this.isLoading = !0,
            this.settingsService.GetOrgList("ACTIVE").subscribe({
                next: t => {
                    t.status === !0 && (this.allOrgList = t.data,
                    this.isLoading = !1)
                }
                ,
                error: t => this.toastr.error(t.error.message, "Projects Management")
            })
        }
        getNetwork() {
            this.isLoading = !0,
            this.projectsService.GetNetwork().subscribe({
                next: t => {
                    t.status === !0 && (this.networkList = t.data,
                    this.isLoading = !1)
                }
                ,
                error: t => this.toastr.error(t.error.message, "Projects Management")
            })
        }
        setValue() {
            this.projectForm.patchValue({
                infoMin: 0,
                infoMax: 0,
                lowMin: .01,
                lowMax: 3.99,
                mediumMin: 4,
                mediumMax: 6.99,
                highMin: 7,
                highMax: 8.99,
                criticalMin: 9,
                criticalMax: 10
            })
        }
    }
    ;
    d.\u0275fac = function(o) {
        return new (o || d)(P(Me),P($),P(J),P(G),P(B),P(Le),P(K),P(ue),P(H))
    }
    ,
    d.\u0275cmp = U({
        type: d,
        selectors: [["app-projects-update"]],
        decls: 133,
        vars: 26,
        consts: [["d", "ngbDatepicker"], [1, "sticky-header"], [1, "mt-4"], [1, "d-flex", "align-items-center", "justify-content-between", "flex-wrap"], [1, "page-breadcrumb", "m-0"], [1, "breadcrumb", "mb-0"], [1, "breadcrumb-item"], ["routerLink", "/main/projects_management/projects_list"], ["aria-current", "page", 1, "breadcrumb-item", "active"], [1, "button-container"], [1, "forms-sample", "d-flex", "flex-wrap", "justify-content-center", 3, "formGroup"], [1, "form-check", "form-switch", "me-3"], ["type", "checkbox", "formControlName", "isActive", "id", "Active", 1, "form-check-input"], ["for", "Active", 1, "form-check-label"], [1, "form-check", "form-switch"], ["type", "checkbox", "formControlName", "isSensitive", "id", "ZeroKnowledge", 1, "form-check-input"], ["for", "ZeroKnowledge", 1, "form-check-label"], [1, "btn", "btn-secondary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], [1, "btn", "btn-primary", "btn-icon-text", "mb-2", "mb-md-0", 3, "click"], [1, "row"], [1, "col-md-12", "grid-margin"], [1, "card", "card_padding"], [1, "card-body"], [1, "forms-sample", 3, "formGroup"], [1, "mb-3"], [1, "form-label"], [1, "text-danger"], ["formControlName", "projectName", "placeholder", "Enter project name", "required", "", 1, "form-control"], ["class", "text-danger", 4, "ngIf"], ["formControlName", "projectShortName", "placeholder", "Enter project short name", 1, "form-control"], ["formControlName", "projectDesc", "placeholder", "Enter project description", "rows", "3", 1, "form-control"], ["bindLabel", "orgName", "bindValue", "_id", "placeholder", "Select organization", "formControlName", "orgName", 3, "ngModelChange", "items", "ngModel", "loading"], ["bindLabel", "nwPlacementName", "bindValue", "_id", "placeholder", "Select network placement", "formControlName", "nwPlacementName", 3, "ngModelChange", "items", "ngModel", "loading"], [1, "input-group"], ["placeholder", "dd-mm-yyyy", "name", "dp", "ngbDatepicker", "", 1, "form-control", "ng-untouched", "ng-pristine", "ng-valid", "date", 3, "ngModelChange", "ngModel", "ngModelOptions"], ["type", "button", 1, "input-group-text", 3, "click"], [1, "feather", "icon-calendar", "icon-md", "text-muted"], [1, "row", "mb-3"], [1, "col-md-6"], [1, "d-flex"], ["type", "number", "formControlName", "infoMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "number", "formControlName", "infoMax", "placeholder", "Max", "min", "0", "required", "", 1, "form-control"], ["class", "text-danger m_r", 4, "ngIf"], [1, "col-md-6", "cssroe"], ["type", "number", "formControlName", "lowMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "number", "formControlName", "lowMax", "placeholder", "Max", "min", "0", "required", "", 1, "form-control"], ["type", "number", "formControlName", "mediumMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "number", "formControlName", "mediumMax", "placeholder", "Max", "min", "0", "required", "", 1, "form-control"], ["type", "number", "formControlName", "highMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "number", "formControlName", "highMax", "placeholder", "Max", "min", "0", "required", "", 1, "form-control"], ["type", "number", "formControlName", "criticalMin", "min", "0", "placeholder", "Min", "required", "", 1, "form-control", "me-2"], ["type", "number", "formControlName", "criticalMax", "min", "0", "placeholder", "Max", "required", "", 1, "form-control"], ["type", "button", 1, "btn", "btn-outline-primary", "mb-1", "mb-md-0", "infoBtn", 3, "click"], [4, "ngIf"], [1, "text-danger", "m_r"]],
        template: function(o, e) {
            if (o & 1) {
                let a = x();
                n(0, "div", 1)(1, "div", 2)(2, "div", 3)(3, "nav", 4)(4, "ol", 5)(5, "li", 6)(6, "a", 7),
                c(7, "Project"),
                r()(),
                n(8, "li", 8),
                c(9),
                r()()(),
                n(10, "div", 9)(11, "form", 10)(12, "div", 11),
                j(13, "input", 12),
                n(14, "label", 13),
                c(15, "Active"),
                r()(),
                n(16, "div", 14),
                j(17, "input", 15),
                n(18, "label", 16),
                c(19, "Sensitive Recommendation"),
                r()()()(),
                n(20, "div", 9)(21, "button", 17),
                _("click", function() {
                    return h(a),
                    g(e.goBack())
                }),
                c(22, "Back"),
                r(),
                n(23, "button", 18),
                _("click", function() {
                    return h(a),
                    g(e.submitForm())
                }),
                c(24, "Submit"),
                r()()()()(),
                n(25, "div", 19)(26, "div", 20)(27, "div", 21)(28, "div", 22)(29, "form", 23)(30, "div", 24)(31, "label", 25),
                c(32, "Project Name"),
                r(),
                n(33, "span", 26),
                c(34, " *"),
                r(),
                j(35, "input", 27),
                f(36, Ct, 2, 1, "div", 28),
                r(),
                n(37, "div", 24)(38, "label", 25),
                c(39, "Project Short Name"),
                r(),
                j(40, "input", 29),
                r(),
                n(41, "div", 24)(42, "label", 25),
                c(43, "Project Description"),
                r(),
                j(44, "textarea", 30),
                r(),
                n(45, "div", 24)(46, "label", 25),
                c(47, "Organization"),
                r(),
                n(48, "span", 26),
                c(49, " *"),
                r(),
                n(50, "ng-select", 31),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.orgId, l) || (e.orgId = l),
                    g(l)
                }),
                r(),
                f(51, bt, 2, 1, "div", 28),
                r(),
                n(52, "div", 24)(53, "label", 25),
                c(54, "Network Placement"),
                r(),
                n(55, "span", 26),
                c(56, " *"),
                r(),
                n(57, "ng-select", 32),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.nwPlacementId, l) || (e.nwPlacementId = l),
                    g(l)
                }),
                r(),
                f(58, zt, 2, 1, "div", 28),
                r(),
                n(59, "div", 24)(60, "label", 25),
                c(61, "Creation Date"),
                r(),
                n(62, "span", 26),
                c(63, " *"),
                r(),
                n(64, "div", 33)(65, "input", 34, 0),
                C("ngModelChange", function(l) {
                    return h(a),
                    y(e.creationDate, l) || (e.creationDate = l),
                    g(l)
                }),
                _("ngModelChange", function(l) {
                    return h(a),
                    g(e.onChange(l))
                }),
                r(),
                n(67, "button", 35),
                _("click", function() {
                    h(a);
                    let l = k(66);
                    return g(l.toggle())
                }),
                j(68, "i", 36),
                r()(),
                f(69, Vt, 2, 1, "div", 28),
                r(),
                n(70, "div", 37)(71, "div", 38)(72, "label", 25),
                c(73, "Info range inclusive"),
                r(),
                n(74, "span", 26),
                c(75, " *"),
                r(),
                n(76, "div", 39),
                j(77, "input", 40)(78, "input", 41),
                r(),
                n(79, "div", 39),
                f(80, Dt, 4, 3, "div", 42)(81, Nt, 4, 3, "div", 28),
                r()(),
                n(82, "div", 43)(83, "label", 25),
                c(84, "Low range inclusive"),
                r(),
                n(85, "span", 26),
                c(86, " *"),
                r(),
                n(87, "div", 39),
                j(88, "input", 44)(89, "input", 45),
                r(),
                n(90, "div", 39),
                f(91, Ut, 4, 3, "div", 42)(92, Kt, 4, 3, "div", 28),
                r()()(),
                n(93, "div", 37)(94, "div", 38)(95, "label", 25),
                c(96, "Medium range inclusive"),
                r(),
                n(97, "span", 26),
                c(98, " *"),
                r(),
                n(99, "div", 39),
                j(100, "input", 46)(101, "input", 47),
                r(),
                n(102, "div", 39),
                f(103, Yt, 4, 3, "div", 42)(104, $t, 4, 3, "div", 28),
                r()(),
                n(105, "div", 43)(106, "label", 25),
                c(107, "High range inclusive"),
                r(),
                n(108, "span", 26),
                c(109, " *"),
                r(),
                n(110, "div", 39),
                j(111, "input", 48)(112, "input", 49),
                r(),
                n(113, "div", 39),
                f(114, rn, 4, 3, "div", 42)(115, sn, 4, 3, "div", 28),
                r()()(),
                n(116, "div", 37)(117, "div", 38)(118, "label", 25),
                c(119, "Critical range inclusive"),
                r(),
                n(120, "span", 26),
                c(121, " *"),
                r(),
                n(122, "div", 39),
                j(123, "input", 50)(124, "input", 51),
                r(),
                n(125, "div", 39),
                f(126, pn, 4, 3, "div", 42)(127, _n, 4, 3, "div", 28),
                r()(),
                n(128, "div", 38)(129, "div"),
                j(130, "label", 25),
                n(131, "button", 52),
                _("click", function() {
                    return h(a),
                    g(e.setValue())
                }),
                c(132, "Set default value"),
                r()()()()()()()()()
            }
            if (o & 2) {
                let a, s, l, w, M, z, T, D, I, E, L, N, O, R;
                p(9),
                V("", e.state != null && e.state.projectId ? "Update" : "New", " Project"),
                p(2),
                u("formGroup", e.projectForm),
                p(18),
                u("formGroup", e.projectForm),
                p(7),
                u("ngIf", (e.projectForm == null || (a = e.projectForm.get("projectName")) == null ? null : a.dirty) && (e.projectForm == null || (a = e.projectForm.get("projectName")) == null ? null : a.errors) || (e.projectForm == null || (a = e.projectForm.get("projectName")) == null ? null : a.touched)),
                p(14),
                u("items", e.allOrgList),
                S("ngModel", e.orgId),
                u("loading", e.isLoading),
                p(),
                u("ngIf", (e.projectForm == null || (s = e.projectForm.get("orgName")) == null ? null : s.dirty) && (e.projectForm == null || (s = e.projectForm.get("orgName")) == null ? null : s.errors) || (e.projectForm == null || (s = e.projectForm.get("orgName")) == null ? null : s.touched)),
                p(6),
                u("items", e.networkList),
                S("ngModel", e.nwPlacementId),
                u("loading", e.isLoading),
                p(),
                u("ngIf", (e.projectForm == null || (l = e.projectForm.get("nwPlacementName")) == null ? null : l.dirty) && (e.projectForm == null || (l = e.projectForm.get("nwPlacementName")) == null ? null : l.errors) || (e.projectForm == null || (l = e.projectForm.get("nwPlacementName")) == null ? null : l.touched)),
                p(7),
                S("ngModel", e.creationDate),
                u("ngModelOptions", le(25, St)),
                p(4),
                u("ngIf", (e.projectForm == null || (w = e.projectForm.get("creationDate")) == null ? null : w.dirty) && (e.projectForm == null || (w = e.projectForm.get("creationDate")) == null ? null : w.errors) || (e.projectForm == null || (w = e.projectForm.get("creationDate")) == null ? null : w.touched)),
                p(11),
                u("ngIf", (e.projectForm == null || (M = e.projectForm.get("infoMin")) == null ? null : M.dirty) && (e.projectForm == null || (M = e.projectForm.get("infoMin")) == null ? null : M.errors) || (e.projectForm == null || (M = e.projectForm.get("infoMin")) == null ? null : M.touched)),
                p(),
                u("ngIf", (e.projectForm == null || (z = e.projectForm.get("infoMax")) == null ? null : z.dirty) && (e.projectForm == null || (z = e.projectForm.get("infoMax")) == null ? null : z.errors) || (e.projectForm == null || (z = e.projectForm.get("infoMax")) == null ? null : z.touched)),
                p(10),
                u("ngIf", (e.projectForm == null || (T = e.projectForm.get("lowMin")) == null ? null : T.dirty) && (e.projectForm == null || (T = e.projectForm.get("lowMin")) == null ? null : T.errors) || (e.projectForm == null || (T = e.projectForm.get("lowMin")) == null ? null : T.touched)),
                p(),
                u("ngIf", (e.projectForm == null || (D = e.projectForm.get("lowMax")) == null ? null : D.dirty) && (e.projectForm == null || (D = e.projectForm.get("lowMax")) == null ? null : D.errors) || (e.projectForm == null || (D = e.projectForm.get("lowMax")) == null ? null : D.touched)),
                p(11),
                u("ngIf", (e.projectForm == null || (I = e.projectForm.get("mediumMin")) == null ? null : I.dirty) && (e.projectForm == null || (I = e.projectForm.get("mediumMin")) == null ? null : I.errors) || (e.projectForm == null || (I = e.projectForm.get("mediumMin")) == null ? null : I.touched)),
                p(),
                u("ngIf", (e.projectForm == null || (E = e.projectForm.get("mediumMax")) == null ? null : E.dirty) && (e.projectForm == null || (E = e.projectForm.get("mediumMax")) == null ? null : E.errors) || (e.projectForm == null || (E = e.projectForm.get("mediumMax")) == null ? null : E.touched)),
                p(10),
                u("ngIf", (e.projectForm == null || (L = e.projectForm.get("highMin")) == null ? null : L.dirty) && (e.projectForm == null || (L = e.projectForm.get("highMin")) == null ? null : L.errors) || (e.projectForm == null || (L = e.projectForm.get("highMin")) == null ? null : L.touched)),
                p(),
                u("ngIf", (e.projectForm == null || (N = e.projectForm.get("highMax")) == null ? null : N.dirty) && (e.projectForm == null || (N = e.projectForm.get("highMax")) == null ? null : N.errors) || (e.projectForm == null || (N = e.projectForm.get("highMax")) == null ? null : N.touched)),
                p(11),
                u("ngIf", (e.projectForm == null || (O = e.projectForm.get("criticalMin")) == null ? null : O.dirty) && (e.projectForm == null || (O = e.projectForm.get("criticalMin")) == null ? null : O.errors) || (e.projectForm == null || (O = e.projectForm.get("criticalMin")) == null ? null : O.touched)),
                p(),
                u("ngIf", (e.projectForm == null || (R = e.projectForm.get("criticalMax")) == null ? null : R.dirty) && (e.projectForm == null || (R = e.projectForm.get("criticalMax")) == null ? null : R.errors) || (e.projectForm == null || (R = e.projectForm.get("criticalMax")) == null ? null : R.touched))
            }
        },
        dependencies: [q, pe, fe, Y, ve, ge, Q, _e, be, Pe, Z, je, we, $e, ze],
        styles: [".mb[_ngcontent-%COMP%]{margin-bottom:0rem!important}.p[_ngcontent-%COMP%]{margin-bottom:6px}.ant-picker[_ngcontent-%COMP%]:hover, .ant-picker-focused[_ngcontent-%COMP%]{border-color:#ced4da;box-shadow:none!important}[_nghost-%COMP%]     .ant-picker-input>input:focus, .ant-picker-input[_ngcontent-%COMP%] > input-focused[_ngcontent-%COMP%]{border-color:#ced4da;box-shadow:0 0 0 2px #eceef033;border-right-width:1px;outline:0}[_nghost-%COMP%]     .ant-picker-input>input:placeholder-shown{font-size:14px!important}  .ng-dropdown-panel .ng-dropdown-panel-items .ng-option, .ng-dropdown-panel[_ngcontent-%COMP%]   .ng-dropdown-panel-items[_ngcontent-%COMP%]   .ng-optgroup[_ngcontent-%COMP%]{background-color:#fff;color:var(--bs-body-color)}@media screen and (max-width: 772px){.infoBtn[_ngcontent-%COMP%]{margin-top:20px!important}.cssroe[_ngcontent-%COMP%]{margin-top:15px!important}.infoBtnG[_ngcontent-%COMP%]{text-align:end!important}}.infoBtn[_ngcontent-%COMP%]{margin-top:30px;height:36px}.m_r[_ngcontent-%COMP%]{margin-right:18%}"]
    });
    let i = d;
    return i
}
)();
var fn = [{
    path: "projects_list",
    component: it,
    canActivate: [ie]
}, {
    path: "projects_update",
    component: rt,
    canActivate: [ie]
}]
  , ot = ( () => {
    let d = class d {
    }
    ;
    d.\u0275fac = function(o) {
        return new (o || d)
    }
    ,
    d.\u0275mod = A({
        type: d
    }),
    d.\u0275inj = W({
        imports: [ne.forChild(fn), ne]
    });
    let i = d;
    return i
}
)();
var Xn = ( () => {
    let d = class d {
    }
    ;
    d.\u0275fac = function(o) {
        return new (o || d)
    }
    ,
    d.\u0275mod = A({
        type: d
    }),
    d.\u0275inj = W({
        imports: [me, ot, et]
    });
    let i = d;
    return i
}
)();
export {Xn as ProjectsModule};

