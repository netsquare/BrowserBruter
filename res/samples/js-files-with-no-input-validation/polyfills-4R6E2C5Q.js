var it = globalThis;
function tt(e) {
  return (it.__Zone_symbol_prefix || '__zone_symbol__') + e
}
function _e() {
  let e = it.performance;
  function t(x) {
    e &&
    e.mark &&
    e.mark(x)
  }
  function c(x, r) {
    e &&
    e.measure &&
    e.measure(x, r)
  }
  t('Zone');
  let X = class X {
    static assertZonePatched() {
      if (it.Promise !== O.ZoneAwarePromise) throw new Error(
        'Zone.js has detected that ZoneAwarePromise `(window|global).Promise` has been overwritten.\nMost likely cause is that a Promise polyfill has been loaded after Zone.js (Polyfilling Promise api is not necessary when zone.js is loaded. If you must load one, do so before loading zone.js.)'
      )
    }
    static get root() {
      let r = X.current;
      for (; r.parent; ) r = r.parent;
      return r
    }
    static get current() {
      return y.zone
    }
    static get currentTask() {
      return I
    }
    static __load_patch(r, i, s = !1) {
      if (O.hasOwnProperty(r)) {
        let v = it[tt('forceDuplicateZoneCheck')] === !0;
        if (!s && v) throw Error('Already loaded patch: ' + r)
      } else if (!it['__Zone_disable_' + r]) {
        let v = 'Zone:' + r;
        t(v),
        O[r] = i(it, X, R),
        c(v, v)
      }
    }
    get parent() {
      return this._parent
    }
    get name() {
      return this._name
    }
    constructor(r, i) {
      this._parent = r,
      this._name = i ? i.name ||
      'unnamed' : '<root>',
      this._properties = i &&
      i.properties ||
      {
      },
      this._zoneDelegate = new u(this, this._parent && this._parent._zoneDelegate, i)
    }
    get(r) {
      let i = this.getZoneWith(r);
      if (i) return i._properties[r]
    }
    getZoneWith(r) {
      let i = this;
      for (; i; ) {
        if (i._properties.hasOwnProperty(r)) return i;
        i = i._parent
      }
      return null
    }
    fork(r) {
      if (!r) throw new Error('ZoneSpec required!');
      return this._zoneDelegate.fork(this, r)
    }
    wrap(r, i) {
      if (typeof r != 'function') throw new Error('Expecting function got: ' + r);
      let s = this._zoneDelegate.intercept(this, r, i),
      v = this;
      return function () {
        return v.runGuarded(s, this, arguments, i)
      }
    }
    run(r, i, s, v) {
      y = {
        parent: y,
        zone: this
      };
      try {
        return this._zoneDelegate.invoke(this, r, i, s, v)
      } finally {
        y = y.parent
      }
    }
    runGuarded(r, i = null, s, v) {
      y = {
        parent: y,
        zone: this
      };
      try {
        try {
          return this._zoneDelegate.invoke(this, r, i, s, v)
        } catch ($) {
          if (this._zoneDelegate.handleError(this, $)) throw $
        }
      } finally {
        y = y.parent
      }
    }
    runTask(r, i, s) {
      if (r.zone != this) throw new Error(
        'A task can only be run in the zone of creation! (Creation: ' + (r.zone || nt).name + '; Execution: ' + this.name + ')'
      );
      if (r.state === W && (r.type === U || r.type === E)) return;
      let v = r.state != H;
      v &&
      r._transitionTo(H, d),
      r.runCount++;
      let $ = I;
      I = r,
      y = {
        parent: y,
        zone: this
      };
      try {
        r.type == E &&
        r.data &&
        !r.data.isPeriodic &&
        (r.cancelFn = void 0);
        try {
          return this._zoneDelegate.invokeTask(this, r, i, s)
        } catch (M) {
          if (this._zoneDelegate.handleError(this, M)) throw M
        }
      } finally {
        r.state !== W &&
        r.state !== q &&
        (
          r.type == U ||
          r.data &&
          r.data.isPeriodic ? v &&
          r._transitionTo(d, H) : (
            r.runCount = 0,
            this._updateTaskCount(r, - 1),
            v &&
            r._transitionTo(W, H, W)
          )
        ),
        y = y.parent,
        I = $
      }
    }
    scheduleTask(r) {
      if (r.zone && r.zone !== this) {
        let s = this;
        for (; s; ) {
          if (s === r.zone) throw Error(
            `can not reschedule task to ${ this.name } which is descendants of the original zone ${ r.zone.name }`
          );
          s = s.parent
        }
      }
      r._transitionTo(k, W);
      let i = [];
      r._zoneDelegates = i,
      r._zone = this;
      try {
        r = this._zoneDelegate.scheduleTask(this, r)
      } catch (s) {
        throw r._transitionTo(q, k, W),
        this._zoneDelegate.handleError(this, s),
        s
      }
      return r._zoneDelegates === i &&
      this._updateTaskCount(r, 1),
      r.state == k &&
      r._transitionTo(d, k),
      r
    }
    scheduleMicroTask(r, i, s, v) {
      return this.scheduleTask(new _(B, r, i, s, v, void 0))
    }
    scheduleMacroTask(r, i, s, v, $) {
      return this.scheduleTask(new _(E, r, i, s, v, $))
    }
    scheduleEventTask(r, i, s, v, $) {
      return this.scheduleTask(new _(U, r, i, s, v, $))
    }
    cancelTask(r) {
      if (r.zone != this) throw new Error(
        'A task can only be cancelled in the zone of creation! (Creation: ' + (r.zone || nt).name + '; Execution: ' + this.name + ')'
      );
      if (!(r.state !== d && r.state !== H)) {
        r._transitionTo(V, d, H);
        try {
          this._zoneDelegate.cancelTask(this, r)
        } catch (i) {
          throw r._transitionTo(q, V),
          this._zoneDelegate.handleError(this, i),
          i
        }
        return this._updateTaskCount(r, - 1),
        r._transitionTo(W, V),
        r.runCount = 0,
        r
      }
    }
    _updateTaskCount(r, i) {
      let s = r._zoneDelegates;
      i == - 1 &&
      (r._zoneDelegates = null);
      for (let v = 0; v < s.length; v++) s[v]._updateTaskCount(r.type, i)
    }
  };
  X.__symbol__ = tt;
  let n = X,
  a = {
    name: '',
    onHasTask: (x, r, i, s) => x.hasTask(i, s),
    onScheduleTask: (x, r, i, s) => x.scheduleTask(i, s),
    onInvokeTask: (x, r, i, s, v, $) => x.invokeTask(i, s, v, $),
    onCancelTask: (x, r, i, s) => x.cancelTask(i, s)
  };
  class u {
    get zone() {
      return this._zone
    }
    constructor(r, i, s) {
      this._taskCounts = {
        microTask: 0,
        macroTask: 0,
        eventTask: 0
      },
      this._zone = r,
      this._parentDelegate = i,
      this._forkZS = s &&
      (s && s.onFork ? s : i._forkZS),
      this._forkDlgt = s &&
      (s.onFork ? i : i._forkDlgt),
      this._forkCurrZone = s &&
      (s.onFork ? this._zone : i._forkCurrZone),
      this._interceptZS = s &&
      (s.onIntercept ? s : i._interceptZS),
      this._interceptDlgt = s &&
      (s.onIntercept ? i : i._interceptDlgt),
      this._interceptCurrZone = s &&
      (s.onIntercept ? this._zone : i._interceptCurrZone),
      this._invokeZS = s &&
      (s.onInvoke ? s : i._invokeZS),
      this._invokeDlgt = s &&
      (s.onInvoke ? i : i._invokeDlgt),
      this._invokeCurrZone = s &&
      (s.onInvoke ? this._zone : i._invokeCurrZone),
      this._handleErrorZS = s &&
      (s.onHandleError ? s : i._handleErrorZS),
      this._handleErrorDlgt = s &&
      (s.onHandleError ? i : i._handleErrorDlgt),
      this._handleErrorCurrZone = s &&
      (s.onHandleError ? this._zone : i._handleErrorCurrZone),
      this._scheduleTaskZS = s &&
      (s.onScheduleTask ? s : i._scheduleTaskZS),
      this._scheduleTaskDlgt = s &&
      (s.onScheduleTask ? i : i._scheduleTaskDlgt),
      this._scheduleTaskCurrZone = s &&
      (s.onScheduleTask ? this._zone : i._scheduleTaskCurrZone),
      this._invokeTaskZS = s &&
      (s.onInvokeTask ? s : i._invokeTaskZS),
      this._invokeTaskDlgt = s &&
      (s.onInvokeTask ? i : i._invokeTaskDlgt),
      this._invokeTaskCurrZone = s &&
      (s.onInvokeTask ? this._zone : i._invokeTaskCurrZone),
      this._cancelTaskZS = s &&
      (s.onCancelTask ? s : i._cancelTaskZS),
      this._cancelTaskDlgt = s &&
      (s.onCancelTask ? i : i._cancelTaskDlgt),
      this._cancelTaskCurrZone = s &&
      (s.onCancelTask ? this._zone : i._cancelTaskCurrZone),
      this._hasTaskZS = null,
      this._hasTaskDlgt = null,
      this._hasTaskDlgtOwner = null,
      this._hasTaskCurrZone = null;
      let v = s &&
      s.onHasTask,
      $ = i &&
      i._hasTaskZS;
      (v || $) &&
      (
        this._hasTaskZS = v ? s : a,
        this._hasTaskDlgt = i,
        this._hasTaskDlgtOwner = this,
        this._hasTaskCurrZone = this._zone,
        s.onScheduleTask ||
        (
          this._scheduleTaskZS = a,
          this._scheduleTaskDlgt = i,
          this._scheduleTaskCurrZone = this._zone
        ),
        s.onInvokeTask ||
        (
          this._invokeTaskZS = a,
          this._invokeTaskDlgt = i,
          this._invokeTaskCurrZone = this._zone
        ),
        s.onCancelTask ||
        (
          this._cancelTaskZS = a,
          this._cancelTaskDlgt = i,
          this._cancelTaskCurrZone = this._zone
        )
      )
    }
    fork(r, i) {
      return this._forkZS ? this._forkZS.onFork(this._forkDlgt, this.zone, r, i) : new n(r, i)
    }
    intercept(r, i, s) {
      return this._interceptZS ? this._interceptZS.onIntercept(this._interceptDlgt, this._interceptCurrZone, r, i, s) : i
    }
    invoke(r, i, s, v, $) {
      return this._invokeZS ? this._invokeZS.onInvoke(this._invokeDlgt, this._invokeCurrZone, r, i, s, v, $) : i.apply(s, v)
    }
    handleError(r, i) {
      return this._handleErrorZS ? this._handleErrorZS.onHandleError(this._handleErrorDlgt, this._handleErrorCurrZone, r, i) : !0
    }
    scheduleTask(r, i) {
      let s = i;
      if (this._scheduleTaskZS) this._hasTaskZS &&
      s._zoneDelegates.push(this._hasTaskDlgtOwner),
      s = this._scheduleTaskZS.onScheduleTask(this._scheduleTaskDlgt, this._scheduleTaskCurrZone, r, i),
      s ||
      (s = i);
       else if (i.scheduleFn) i.scheduleFn(i);
       else if (i.type == B) G(i);
       else throw new Error('Task is missing scheduleFn.');
      return s
    }
    invokeTask(r, i, s, v) {
      return this._invokeTaskZS ? this._invokeTaskZS.onInvokeTask(this._invokeTaskDlgt, this._invokeTaskCurrZone, r, i, s, v) : i.callback.apply(s, v)
    }
    cancelTask(r, i) {
      let s;
      if (this._cancelTaskZS) s = this._cancelTaskZS.onCancelTask(this._cancelTaskDlgt, this._cancelTaskCurrZone, r, i);
       else {
        if (!i.cancelFn) throw Error('Task is not cancelable');
        s = i.cancelFn(i)
      }
      return s
    }
    hasTask(r, i) {
      try {
        this._hasTaskZS &&
        this._hasTaskZS.onHasTask(this._hasTaskDlgt, this._hasTaskCurrZone, r, i)
      } catch (s) {
        this.handleError(r, s)
      }
    }
    _updateTaskCount(r, i) {
      let s = this._taskCounts,
      v = s[r],
      $ = s[r] = v + i;
      if ($ < 0) throw new Error('More tasks executed then were scheduled.');
      if (v == 0 || $ == 0) {
        let M = {
          microTask: s.microTask > 0,
          macroTask: s.macroTask > 0,
          eventTask: s.eventTask > 0,
          change: r
        };
        this.hasTask(this._zone, M)
      }
    }
  }
  class _ {
    constructor(r, i, s, v, $, M) {
      if (
        this._zone = null,
        this.runCount = 0,
        this._zoneDelegates = null,
        this._state = 'notScheduled',
        this.type = r,
        this.source = i,
        this.data = v,
        this.scheduleFn = $,
        this.cancelFn = M,
        !s
      ) throw new Error('callback is not defined');
      this.callback = s;
      let dt = this;
      r === U &&
      v &&
      v.useG ? this.invoke = _.invokeTask : this.invoke = function () {
        return _.invokeTask.call(it, dt, this, arguments)
      }
    }
    static invokeTask(r, i, s) {
      r ||
      (r = this),
      J++;
      try {
        return r.runCount++,
        r.zone.runTask(r, i, s)
      } finally {
        J == 1 &&
        j(),
        J--
      }
    }
    get zone() {
      return this._zone
    }
    get state() {
      return this._state
    }
    cancelScheduleRequest() {
      this._transitionTo(W, k)
    }
    _transitionTo(r, i, s) {
      if (this._state === i || this._state === s) this._state = r,
      r == W &&
      (this._zoneDelegates = null);
       else throw new Error(
        `${ this.type } '${ this.source }': can not transition to '${ r }', expecting state '${ i }'${ s ? ' or \'' + s + '\'' : '' }, was '${ this._state }'.`
      )
    }
    toString() {
      return this.data &&
      typeof this.data.handleId < 'u' ? this.data.handleId.toString() : Object.prototype.toString.call(this)
    }
    toJSON() {
      return {
        type: this.type,
        state: this.state,
        source: this.source,
        zone: this.zone.name,
        runCount: this.runCount
      }
    }
  }
  let T = tt('setTimeout'),
  m = tt('Promise'),
  N = tt('then'),
  g = [],
  D = !1,
  P;
  function A(x) {
    if (P || it[m] && (P = it[m].resolve(0)), P) {
      let r = P[N];
      r ||
      (r = P.then),
      r.call(P, x)
    } else it[T](x, 0)
  }
  function G(x) {
    J === 0 &&
    g.length === 0 &&
    A(j),
    x &&
    g.push(x)
  }
  function j() {
    if (!D) {
      for (D = !0; g.length; ) {
        let x = g;
        g = [];
        for (let r = 0; r < x.length; r++) {
          let i = x[r];
          try {
            i.zone.runTask(i, null, null)
          } catch (s) {
            R.onUnhandledError(s)
          }
        }
      }
      R.microtaskDrainDone(),
      D = !1
    }
  }
  let nt = {
    name: 'NO ZONE'
  },
  W = 'notScheduled',
  k = 'scheduling',
  d = 'scheduled',
  H = 'running',
  V = 'canceling',
  q = 'unknown',
  B = 'microTask',
  E = 'macroTask',
  U = 'eventTask',
  O = {},
  R = {
    symbol: tt,
    currentZoneFrame: () => y,
    onUnhandledError: F,
    microtaskDrainDone: F,
    scheduleMicroTask: G,
    showUncaughtError: () => !n[tt('ignoreConsoleErrorUncaughtError')],
    patchEventTarget: () => [],
    patchOnProperties: F,
    patchMethod: () => F,
    bindArguments: () => [],
    patchThen: () => F,
    patchMacroTask: () => F,
    patchEventPrototype: () => F,
    isIEOrEdge: () => !1,
    getGlobalObjects: () => {
    },
    ObjectDefineProperty: () => F,
    ObjectGetOwnPropertyDescriptor: () => {
    },
    ObjectCreate: () => {
    },
    ArraySlice: () => [],
    patchClass: () => F,
    wrapWithCurrentZone: () => F,
    filterProperties: () => [],
    attachOriginToPatched: () => F,
    _redefineProperty: () => F,
    patchCallbacks: () => F,
    nativeScheduleMicroTask: A
  },
  y = {
    parent: null,
    zone: new n(null, null)
  },
  I = null,
  J = 0;
  function F() {
  }
  return c('Zone', 'Zone'),
  n
}
function Te() {
  let e = globalThis,
  t = e[tt('forceDuplicateZoneCheck')] === !0;
  if (e.Zone && (t || typeof e.Zone.__symbol__ != 'function')) throw new Error('Zone already loaded.');
  return e.Zone ??= _e(),
  e.Zone
}
var kt = Object.getOwnPropertyDescriptor,
jt = Object.defineProperty,
xt = Object.getPrototypeOf,
ge = Object.create,
Ee = Array.prototype.slice,
Zt = 'addEventListener',
$t = 'removeEventListener',
Dt = tt(Zt),
Mt = tt($t),
ct = 'true',
at = 'false',
vt = tt('');
function Ht(e, t) {
  return Zone.current.wrap(e, t)
}
function Bt(e, t, c, n, a) {
  return Zone.current.scheduleMacroTask(e, t, c, n, a)
}
var Z = tt,
Nt = typeof window < 'u',
mt = Nt ? window : void 0,
K = Nt &&
mt ||
globalThis,
me = 'removeAttribute';
function Ut(e, t) {
  for (let c = e.length - 1; c >= 0; c--) typeof e[c] == 'function' &&
  (e[c] = Ht(e[c], t + '_' + c));
  return e
}
function pe(e, t) {
  let c = e.constructor.name;
  for (let n = 0; n < t.length; n++) {
    let a = t[n],
    u = e[a];
    if (u) {
      let _ = kt(e, a);
      if (!te(_)) continue;
      e[a] = (
        T => {
          let m = function () {
            return T.apply(this, Ut(arguments, c + '.' + a))
          };
          return ut(m, T),
          m
        }
      ) (u)
    }
  }
}
function te(e) {
  return e ? e.writable === !1 ? !1 : !(typeof e.get == 'function' && typeof e.set > 'u') : !0
}
var ee = typeof WorkerGlobalScope < 'u' &&
self instanceof WorkerGlobalScope,
Ct = !('nw' in K) &&
typeof K.process < 'u' &&
K.process.toString() === '[object process]',
zt = !Ct &&
!ee &&
!!(Nt && mt.HTMLElement),
ne = typeof K.process < 'u' &&
K.process.toString() === '[object process]' &&
!ee &&
!!(Nt && mt.HTMLElement),
Rt = {},
Yt = function (e) {
  if (e = e || K.event, !e) return;
  let t = Rt[e.type];
  t ||
  (t = Rt[e.type] = Z('ON_PROPERTY' + e.type));
  let c = this ||
  e.target ||
  K,
  n = c[t],
  a;
  if (zt && c === mt && e.type === 'error') {
    let u = e;
    a = n &&
    n.call(this, u.message, u.filename, u.lineno, u.colno, u.error),
    a === !0 &&
    e.preventDefault()
  } else a = n &&
  n.apply(this, arguments),
  a != null &&
  !a &&
  e.preventDefault();
  return a
};
function Kt(e, t, c) {
  let n = kt(e, t);
  if (
    !n &&
    c &&
    kt(c, t) &&
    (n = {
      enumerable: !0,
      configurable: !0
    }),
    !n ||
    !n.configurable
  ) return;
  let a = Z('on' + t + 'patched');
  if (e.hasOwnProperty(a) && e[a]) return;
  delete n.writable,
  delete n.value;
  let u = n.get,
  _ = n.set,
  T = t.slice(2),
  m = Rt[T];
  m ||
  (m = Rt[T] = Z('ON_PROPERTY' + T)),
  n.set = function (N) {
    let g = this;
    if (!g && e === K && (g = K), !g) return;
    typeof g[m] == 'function' &&
    g.removeEventListener(T, Yt),
    _ &&
    _.call(g, null),
    g[m] = N,
    typeof N == 'function' &&
    g.addEventListener(T, Yt, !1)
  },
  n.get = function () {
    let N = this;
    if (!N && e === K && (N = K), !N) return null;
    let g = N[m];
    if (g) return g;
    if (u) {
      let D = u.call(this);
      if (D) return n.set.call(this, D),
      typeof N[me] == 'function' &&
      N.removeAttribute(t),
      D
    }
    return null
  },
  jt(e, t, n),
  e[a] = !0
}
function re(e, t, c) {
  if (t) for (let n = 0; n < t.length; n++) Kt(e, 'on' + t[n], c);
   else {
    let n = [];
    for (let a in e) a.slice(0, 2) == 'on' &&
    n.push(a);
    for (let a = 0; a < n.length; a++) Kt(e, n[a], c)
  }
}
var rt = Z('originalInstance');
function yt(e) {
  let t = K[e];
  if (!t) return;
  K[Z(e)] = t,
  K[e] = function () {
    let a = Ut(arguments, e);
    switch (a.length) {
      case 0:
        this[rt] = new t;
        break;
      case 1:
        this[rt] = new t(a[0]);
        break;
      case 2:
        this[rt] = new t(a[0], a[1]);
        break;
      case 3:
        this[rt] = new t(a[0], a[1], a[2]);
        break;
      case 4:
        this[rt] = new t(a[0], a[1], a[2], a[3]);
        break;
      default:
        throw new Error('Arg list too long.')
    }
  },
  ut(K[e], t);
  let c = new t(function () {
  }),
  n;
  for (n in c) e === 'XMLHttpRequest' &&
  n === 'responseBlob' ||
  function (a) {
    typeof c[a] == 'function' ? K[e].prototype[a] = function () {
      return this[rt][a].apply(this[rt], arguments)
    }
     : jt(
      K[e].prototype,
      a,
      {
        set: function (u) {
          typeof u == 'function' ? (this[rt][a] = Ht(u, e + '.' + a), ut(this[rt][a], u)) : this[rt][a] = u
        },
        get: function () {
          return this[rt][a]
        }
      }
    )
  }(n);
  for (n in t) n !== 'prototype' &&
  t.hasOwnProperty(n) &&
  (K[e][n] = t[n])
}
function lt(e, t, c) {
  let n = e;
  for (; n && !n.hasOwnProperty(t); ) n = xt(n);
  !n &&
  e[t] &&
  (n = e);
  let a = Z(t),
  u = null;
  if (n && (!(u = n[a]) || !n.hasOwnProperty(a))) {
    u = n[a] = n[t];
    let _ = n &&
    kt(n, t);
    if (te(_)) {
      let T = c(u, a, t);
      n[t] = function () {
        return T(this, arguments)
      },
      ut(n[t], u)
    }
  }
  return u
}
function ye(e, t, c) {
  let n = null;
  function a(u) {
    let _ = u.data;
    return _.args[_.cbIdx] = function () {
      u.invoke.apply(this, arguments)
    },
    n.apply(_.target, _.args),
    u
  }
  n = lt(
    e,
    t,
    u => function (_, T) {
      let m = c(_, T);
      return m.cbIdx >= 0 &&
      typeof T[m.cbIdx] == 'function' ? Bt(m.name, T[m.cbIdx], m, a) : u.apply(_, T)
    }
  )
}
function ut(e, t) {
  e[Z('OriginalDelegate')] = t
}
var Jt = !1,
Lt = !1;
function ke() {
  try {
    let e = mt.navigator.userAgent;
    if (e.indexOf('MSIE ') !== - 1 || e.indexOf('Trident/') !== - 1) return !0
  } catch {
  }
  return !1
}
function ve() {
  if (Jt) return Lt;
  Jt = !0;
  try {
    let e = mt.navigator.userAgent;
    (
      e.indexOf('MSIE ') !== - 1 ||
      e.indexOf('Trident/') !== - 1 ||
      e.indexOf('Edge/') !== - 1
    ) &&
    (Lt = !0)
  } catch {
  }
  return Lt
}
var Et = !1;
if (typeof window < 'u') try {
  let e = Object.defineProperty({
  }, 'passive', {
    get: function () {
      Et = !0
    }
  });
  window.addEventListener('test', e, e),
  window.removeEventListener('test', e, e)
} catch {
  Et = !1
}
var be = {
  useG: !0
},
et = {},
oe = {},
se = new RegExp('^' + vt + '(\\w+)(true|false)$'),
ie = Z('propagationStopped');
function ce(e, t) {
  let c = (t ? t(e) : e) + at,
  n = (t ? t(e) : e) + ct,
  a = vt + c,
  u = vt + n;
  et[e] = {},
  et[e][at] = a,
  et[e][ct] = u
}
function we(e, t, c, n) {
  let a = n &&
  n.add ||
  Zt,
  u = n &&
  n.rm ||
  $t,
  _ = n &&
  n.listeners ||
  'eventListeners',
  T = n &&
  n.rmAll ||
  'removeAllListeners',
  m = Z(a),
  N = '.' + a + ':',
  g = 'prependListener',
  D = '.' + g + ':',
  P = function (k, d, H) {
    if (k.isRemoved) return;
    let V = k.callback;
    typeof V == 'object' &&
    V.handleEvent &&
    (k.callback = E => V.handleEvent(E), k.originalDelegate = V);
    let q;
    try {
      k.invoke(k, d, [
        H
      ])
    } catch (E) {
      q = E
    }
    let B = k.options;
    if (B && typeof B == 'object' && B.once) {
      let E = k.originalDelegate ? k.originalDelegate : k.callback;
      d[u].call(d, H.type, E, B)
    }
    return q
  };
  function A(k, d, H) {
    let V = k ||
    d.target ||
    e,
    q = V[et[d.type][H ? ct : at]];
    if (q) {
      let B = [];
      if (q.length === 1) {
        let E = P(q[0], V, d);
        E &&
        B.push(E)
      } else {
        let E = q.slice();
        for (let U = 0; U < E.length && !(d && d[ie] === !0); U++) {
          let O = P(E[U], V, d);
          O &&
          B.push(O)
        }
      }
      if (B.length === 1) throw B[0];
      for (let E = 0; E < B.length; E++) {
        let U = B[E];
        t.nativeScheduleMicroTask(() => {
          throw U
        })
      }
    }
  }
  let G = function (k) {
    return A(this, k, !1)
  },
  j = function (k) {
    return A(this, k, !0)
  };
  function nt(k, d) {
    if (!k) return !1;
    let H = !0;
    d &&
    d.useG !== void 0 &&
    (H = d.useG);
    let V = d &&
    d.vh,
    q = !0;
    d &&
    d.chkDup !== void 0 &&
    (q = d.chkDup);
    let B = !1;
    d &&
    d.rt !== void 0 &&
    (B = d.rt);
    let E = k;
    for (; E && !E.hasOwnProperty(a); ) E = xt(E);
    if (!E && k[a] && (E = k), !E || E[m]) return !1;
    let U = d &&
    d.eventNameToString,
    O = {},
    R = E[m] = E[a],
    y = E[Z(u)] = E[u],
    I = E[Z(_)] = E[_],
    J = E[Z(T)] = E[T],
    F;
    d &&
    d.prepend &&
    (F = E[Z(d.prepend)] = E[d.prepend]);
    function X(o, l) {
      return !Et &&
      typeof o == 'object' &&
      o ? !!o.capture : !Et ||
      !l ? o : typeof o == 'boolean' ? {
        capture: o,
        passive: !0
      }
       : o ? typeof o == 'object' &&
      o.passive !== !1 ? {
        ...o,
        passive: !0
      }
       : o : {
        passive: !0
      }
    }
    let x = function (o) {
      if (!O.isExisting) return R.call(O.target, O.eventName, O.capture ? j : G, O.options)
    },
    r = function (o) {
      if (!o.isRemoved) {
        let l = et[o.eventName],
        h;
        l &&
        (h = l[o.capture ? ct : at]);
        let b = h &&
        o.target[h];
        if (b) {
          for (let C = 0; C < b.length; C++) if (b[C] === o) {
            b.splice(C, 1),
            o.isRemoved = !0,
            b.length === 0 &&
            (o.allRemoved = !0, o.target[h] = null);
            break
          }
        }
      }
      if (o.allRemoved) return y.call(o.target, o.eventName, o.capture ? j : G, o.options)
    },
    i = function (o) {
      return R.call(O.target, O.eventName, o.invoke, O.options)
    },
    s = function (o) {
      return F.call(O.target, O.eventName, o.invoke, O.options)
    },
    v = function (o) {
      return y.call(o.target, o.eventName, o.invoke, o.options)
    },
    $ = H ? x : i,
    M = H ? r : v,
    dt = function (o, l) {
      let h = typeof l;
      return h === 'function' &&
      o.callback === l ||
      h === 'object' &&
      o.originalDelegate === l
    },
    pt = d &&
    d.diff ? d.diff : dt,
    ft = Zone[Z('UNPATCHED_EVENTS')],
    bt = e[Z('PASSIVE_EVENTS')],
    f = function (o, l, h, b, C = !1, p = !1) {
      return function () {
        let w = this ||
        e,
        S = arguments[0];
        d &&
        d.transferEventName &&
        (S = d.transferEventName(S));
        let L = arguments[1];
        if (!L) return o.apply(this, arguments);
        if (Ct && S === 'uncaughtException') return o.apply(this, arguments);
        let z = !1;
        if (typeof L != 'function') {
          if (!L.handleEvent) return o.apply(this, arguments);
          z = !0
        }
        if (V && !V(o, L, w, arguments)) return;
        let Y = Et &&
        !!bt &&
        bt.indexOf(S) !== - 1,
        Q = X(arguments[2], Y),
        _t = Q?.signal;
        if (_t?.aborted) return;
        if (ft) {
          for (let st = 0; st < ft.length; st++) if (S === ft[st]) return Y ? o.call(w, S, L, Q) : o.apply(this, arguments)
        }
        let It = Q ? typeof Q == 'boolean' ? !0 : Q.capture : !1,
        Vt = Q &&
        typeof Q == 'object' ? Q.once : !1,
        de = Zone.current,
        Ot = et[S];
        Ot ||
        (ce(S, U), Ot = et[S]);
        let Ft = Ot[It ? ct : at],
        Tt = w[Ft],
        Wt = !1;
        if (Tt) {
          if (Wt = !0, q) {
            for (let st = 0; st < Tt.length; st++) if (pt(Tt[st], L)) return
          }
        } else Tt = w[Ft] = [];
        let wt,
        qt = w.constructor.name,
        Xt = oe[qt];
        Xt &&
        (wt = Xt[S]),
        wt ||
        (wt = qt + l + (U ? U(S) : S)),
        O.options = Q,
        Vt &&
        (O.options.once = !1),
        O.target = w,
        O.capture = It,
        O.eventName = S,
        O.isExisting = Wt;
        let ht = H ? be : void 0;
        ht &&
        (ht.taskData = O),
        _t &&
        (O.options.signal = void 0);
        let ot = de.scheduleEventTask(wt, L, ht, h, b);
        if (_t) {
          O.options.signal = _t;
          let st = () => ot.zone.cancelTask(ot);
          o.call(_t, 'abort', st, {
            once: !0
          }),
          ht &&
          (
            ht.removeAbortListener = () => _t.removeEventListener('abort', st)
          )
        }
        if (
          O.target = null,
          ht &&
          (ht.taskData = null),
          Vt &&
          (Q.once = !0),
          !Et &&
          typeof ot.options == 'boolean' ||
          (ot.options = Q),
          ot.target = w,
          ot.capture = It,
          ot.eventName = S,
          z &&
          (ot.originalDelegate = L),
          p ? Tt.unshift(ot) : Tt.push(ot),
          C
        ) return w
      }
    };
    return E[a] = f(R, N, $, M, B),
    F &&
    (E[g] = f(F, D, s, M, B, !0)),
    E[u] = function () {
      let o = this ||
      e,
      l = arguments[0];
      d &&
      d.transferEventName &&
      (l = d.transferEventName(l));
      let h = arguments[2],
      b = h ? typeof h == 'boolean' ? !0 : h.capture : !1,
      C = arguments[1];
      if (!C) return y.apply(this, arguments);
      if (V && !V(y, C, o, arguments)) return;
      let p = et[l],
      w;
      p &&
      (w = p[b ? ct : at]);
      let S = w &&
      o[w];
      if (S) for (let L = 0; L < S.length; L++) {
        let z = S[L];
        if (pt(z, C)) {
          if (
            S.splice(L, 1),
            z.isRemoved = !0,
            S.length === 0 &&
            (z.allRemoved = !0, o[w] = null, !b && typeof l == 'string')
          ) {
            let Q = vt + 'ON_PROPERTY' + l;
            o[Q] = null
          }
          let Y = z.data;
          return Y?.removeAbortListener &&
          (Y.removeAbortListener(), Y.removeAbortListener = null),
          z.zone.cancelTask(z),
          B ? o : void 0
        }
      }
      return y.apply(this, arguments)
    },
    E[_] = function () {
      let o = this ||
      e,
      l = arguments[0];
      d &&
      d.transferEventName &&
      (l = d.transferEventName(l));
      let h = [],
      b = ae(o, U ? U(l) : l);
      for (let C = 0; C < b.length; C++) {
        let p = b[C],
        w = p.originalDelegate ? p.originalDelegate : p.callback;
        h.push(w)
      }
      return h
    },
    E[T] = function () {
      let o = this ||
      e,
      l = arguments[0];
      if (l) {
        d &&
        d.transferEventName &&
        (l = d.transferEventName(l));
        let h = et[l];
        if (h) {
          let b = h[at],
          C = h[ct],
          p = o[b],
          w = o[C];
          if (p) {
            let S = p.slice();
            for (let L = 0; L < S.length; L++) {
              let z = S[L],
              Y = z.originalDelegate ? z.originalDelegate : z.callback;
              this[u].call(this, l, Y, z.options)
            }
          }
          if (w) {
            let S = w.slice();
            for (let L = 0; L < S.length; L++) {
              let z = S[L],
              Y = z.originalDelegate ? z.originalDelegate : z.callback;
              this[u].call(this, l, Y, z.options)
            }
          }
        }
      } else {
        let h = Object.keys(o);
        for (let b = 0; b < h.length; b++) {
          let C = h[b],
          p = se.exec(C),
          w = p &&
          p[1];
          w &&
          w !== 'removeListener' &&
          this[T].call(this, w)
        }
        this[T].call(this, 'removeListener')
      }
      if (B) return this
    },
    ut(E[a], R),
    ut(E[u], y),
    J &&
    ut(E[T], J),
    I &&
    ut(E[_], I),
    !0
  }
  let W = [];
  for (let k = 0; k < c.length; k++) W[k] = nt(c[k], n);
  return W
}
function ae(e, t) {
  if (!t) {
    let u = [];
    for (let _ in e) {
      let T = se.exec(_),
      m = T &&
      T[1];
      if (m && (!t || m === t)) {
        let N = e[_];
        if (N) for (let g = 0; g < N.length; g++) u.push(N[g])
      }
    }
    return u
  }
  let c = et[t];
  c ||
  (ce(t), c = et[t]);
  let n = e[c[at]],
  a = e[c[ct]];
  return n ? a ? n.concat(a) : n.slice() : a ? a.slice() : []
}
function Pe(e, t) {
  let c = e.Event;
  c &&
  c.prototype &&
  t.patchMethod(
    c.prototype,
    'stopImmediatePropagation',
    n => function (a, u) {
      a[ie] = !0,
      n &&
      n.apply(a, u)
    }
  )
}
function Re(e, t) {
  t.patchMethod(
    e,
    'queueMicrotask',
    c => function (n, a) {
      Zone.current.scheduleMicroTask('queueMicrotask', a[0])
    }
  )
}
var Pt = Z('zoneTask');
function gt(e, t, c, n) {
  let a = null,
  u = null;
  t += n,
  c += n;
  let _ = {};
  function T(N) {
    let g = N.data;
    return g.args[0] = function () {
      return N.invoke.apply(this, arguments)
    },
    g.handleId = a.apply(e, g.args),
    N
  }
  function m(N) {
    return u.call(e, N.data.handleId)
  }
  a = lt(
    e,
    t,
    N => function (g, D) {
      if (typeof D[0] == 'function') {
        let P = {
          isPeriodic: n === 'Interval',
          delay: n === 'Timeout' ||
          n === 'Interval' ? D[1] ||
          0 : void 0,
          args: D
        },
        A = D[0];
        D[0] = function () {
          try {
            return A.apply(this, arguments)
          } finally {
            P.isPeriodic ||
            (
              typeof P.handleId == 'number' ? delete _[P.handleId] : P.handleId &&
              (P.handleId[Pt] = null)
            )
          }
        };
        let G = Bt(t, D[0], P, T, m);
        if (!G) return G;
        let j = G.data.handleId;
        return typeof j == 'number' ? _[j] = G : j &&
        (j[Pt] = G),
        j &&
        j.ref &&
        j.unref &&
        typeof j.ref == 'function' &&
        typeof j.unref == 'function' &&
        (G.ref = j.ref.bind(j), G.unref = j.unref.bind(j)),
        typeof j == 'number' ||
        j ? j : G
      } else return N.apply(e, D)
    }
  ),
  u = lt(
    e,
    c,
    N => function (g, D) {
      let P = D[0],
      A;
      typeof P == 'number' ? A = _[P] : (A = P && P[Pt], A || (A = P)),
      A &&
      typeof A.type == 'string' ? A.state !== 'notScheduled' &&
      (A.cancelFn && A.data.isPeriodic || A.runCount === 0) &&
      (
        typeof P == 'number' ? delete _[P] : P &&
        (P[Pt] = null),
        A.zone.cancelTask(A)
      ) : N.apply(e, D)
    }
  )
}
function Ne(e, t) {
  let {
    isBrowser: c,
    isMix: n
  }
  = t.getGlobalObjects();
  if (!c && !n || !e.customElements || !('customElements' in e)) return;
  let a = [
    'connectedCallback',
    'disconnectedCallback',
    'adoptedCallback',
    'attributeChangedCallback',
    'formAssociatedCallback',
    'formDisabledCallback',
    'formResetCallback',
    'formStateRestoreCallback'
  ];
  t.patchCallbacks(t, e.customElements, 'customElements', 'define', a)
}
function Ce(e, t) {
  if (Zone[t.symbol('patchEventTarget')]) return;
  let {
    eventNames: c,
    zoneSymbolEventNames: n,
    TRUE_STR: a,
    FALSE_STR: u,
    ZONE_SYMBOL_PREFIX: _
  }
  = t.getGlobalObjects();
  for (let m = 0; m < c.length; m++) {
    let N = c[m],
    g = N + u,
    D = N + a,
    P = _ + g,
    A = _ + D;
    n[N] = {},
    n[N][u] = P,
    n[N][a] = A
  }
  let T = e.EventTarget;
  if (!(!T || !T.prototype)) return t.patchEventTarget(e, t, [
    T &&
    T.prototype
  ]),
  !0
}
function Se(e, t) {
  t.patchEventPrototype(e, t)
}
function le(e, t, c) {
  if (!c || c.length === 0) return t;
  let n = c.filter(u => u.target === e);
  if (!n || n.length === 0) return t;
  let a = n[0].ignoreProperties;
  return t.filter(u => a.indexOf(u) === - 1)
}
function Qt(e, t, c, n) {
  if (!e) return;
  let a = le(e, t, c);
  re(e, a, n)
}
function At(e) {
  return Object.getOwnPropertyNames(e).filter(t => t.startsWith('on') && t.length > 2).map(t => t.substring(2))
}
function Ie(e, t) {
  if (Ct && !ne || Zone[e.symbol('patchEvents')]) return;
  let c = t.__Zone_ignore_on_properties,
  n = [];
  if (zt) {
    let a = window;
    n = n.concat(
      ['Document',
      'SVGElement',
      'Element',
      'HTMLElement',
      'HTMLBodyElement',
      'HTMLMediaElement',
      'HTMLFrameSetElement',
      'HTMLFrameElement',
      'HTMLIFrameElement',
      'HTMLMarqueeElement',
      'Worker']
    );
    let u = ke() ? [
      {
        target: a,
        ignoreProperties: [
          'error'
        ]
      }
    ] : [];
    Qt(a, At(a), c && c.concat(u), xt(a))
  }
  n = n.concat(
    ['XMLHttpRequest',
    'XMLHttpRequestEventTarget',
    'IDBIndex',
    'IDBRequest',
    'IDBOpenDBRequest',
    'IDBDatabase',
    'IDBTransaction',
    'IDBCursor',
    'WebSocket']
  );
  for (let a = 0; a < n.length; a++) {
    let u = t[n[a]];
    u &&
    u.prototype &&
    Qt(u.prototype, At(u.prototype), c)
  }
}
function Oe(e) {
  e.__load_patch('legacy', t => {
    let c = t[e.__symbol__('legacyPatch')];
    c &&
    c()
  }),
  e.__load_patch(
    'timers',
    t => {
      let c = 'set',
      n = 'clear';
      gt(t, c, n, 'Timeout'),
      gt(t, c, n, 'Interval'),
      gt(t, c, n, 'Immediate')
    }
  ),
  e.__load_patch(
    'requestAnimationFrame',
    t => {
      gt(t, 'request', 'cancel', 'AnimationFrame'),
      gt(t, 'mozRequest', 'mozCancel', 'AnimationFrame'),
      gt(t, 'webkitRequest', 'webkitCancel', 'AnimationFrame')
    }
  ),
  e.__load_patch(
    'blocking',
    (t, c) => {
      let n = [
        'alert',
        'prompt',
        'confirm'
      ];
      for (let a = 0; a < n.length; a++) {
        let u = n[a];
        lt(t, u, (_, T, m) => function (N, g) {
          return c.current.run(_, t, g, m)
        })
      }
    }
  ),
  e.__load_patch(
    'EventTarget',
    (t, c, n) => {
      Se(t, n),
      Ce(t, n);
      let a = t.XMLHttpRequestEventTarget;
      a &&
      a.prototype &&
      n.patchEventTarget(t, n, [
        a.prototype
      ])
    }
  ),
  e.__load_patch(
    'MutationObserver',
    (t, c, n) => {
      yt('MutationObserver'),
      yt('WebKitMutationObserver')
    }
  ),
  e.__load_patch('IntersectionObserver', (t, c, n) => {
    yt('IntersectionObserver')
  }),
  e.__load_patch('FileReader', (t, c, n) => {
    yt('FileReader')
  }),
  e.__load_patch('on_property', (t, c, n) => {
    Ie(n, t)
  }),
  e.__load_patch('customElements', (t, c, n) => {
    Ne(t, n)
  }),
  e.__load_patch(
    'XHR',
    (t, c) => {
      N(t);
      let n = Z('xhrTask'),
      a = Z('xhrSync'),
      u = Z('xhrListener'),
      _ = Z('xhrScheduled'),
      T = Z('xhrURL'),
      m = Z('xhrErrorBeforeScheduled');
      function N(g) {
        let D = g.XMLHttpRequest;
        if (!D) return;
        let P = D.prototype;
        function A(R) {
          return R[n]
        }
        let G = P[Dt],
        j = P[Mt];
        if (!G) {
          let R = g.XMLHttpRequestEventTarget;
          if (R) {
            let y = R.prototype;
            G = y[Dt],
            j = y[Mt]
          }
        }
        let nt = 'readystatechange',
        W = 'scheduled';
        function k(R) {
          let y = R.data,
          I = y.target;
          I[_] = !1,
          I[m] = !1;
          let J = I[u];
          G ||
          (G = I[Dt], j = I[Mt]),
          J &&
          j.call(I, nt, J);
          let F = I[u] = () => {
            if (I.readyState === I.DONE) if (!y.aborted && I[_] && R.state === W) {
              let x = I[c.__symbol__('loadfalse')];
              if (I.status !== 0 && x && x.length > 0) {
                let r = R.invoke;
                R.invoke = function () {
                  let i = I[c.__symbol__('loadfalse')];
                  for (let s = 0; s < i.length; s++) i[s] === R &&
                  i.splice(s, 1);
                  !y.aborted &&
                  R.state === W &&
                  r.call(R)
                },
                x.push(R)
              } else R.invoke()
            } else !y.aborted &&
            I[_] === !1 &&
            (I[m] = !0)
          };
          return G.call(I, nt, F),
          I[n] ||
          (I[n] = R),
          U.apply(I, y.args),
          I[_] = !0,
          R
        }
        function d() {
        }
        function H(R) {
          let y = R.data;
          return y.aborted = !0,
          O.apply(y.target, y.args)
        }
        let V = lt(
          P,
          'open',
          () => function (R, y) {
            return R[a] = y[2] == !1,
            R[T] = y[1],
            V.apply(R, y)
          }
        ),
        q = 'XMLHttpRequest.send',
        B = Z('fetchTaskAborting'),
        E = Z('fetchTaskScheduling'),
        U = lt(
          P,
          'send',
          () => function (R, y) {
            if (c.current[E] === !0 || R[a]) return U.apply(R, y);
            {
              let I = {
                target: R,
                url: R[T],
                isPeriodic: !1,
                args: y,
                aborted: !1
              },
              J = Bt(q, d, I, k, H);
              R &&
              R[m] === !0 &&
              !I.aborted &&
              J.state === W &&
              J.invoke()
            }
          }
        ),
        O = lt(
          P,
          'abort',
          () => function (R, y) {
            let I = A(R);
            if (I && typeof I.type == 'string') {
              if (I.cancelFn == null || I.data && I.data.aborted) return;
              I.zone.cancelTask(I)
            } else if (c.current[B] === !0) return O.apply(R, y)
          }
        )
      }
    }
  ),
  e.__load_patch(
    'geolocation',
    t => {
      t.navigator &&
      t.navigator.geolocation &&
      pe(
        t.navigator.geolocation,
        [
          'getCurrentPosition',
          'watchPosition'
        ]
      )
    }
  ),
  e.__load_patch(
    'PromiseRejectionEvent',
    (t, c) => {
      function n(a) {
        return function (u) {
          ae(t, a).forEach(
            T => {
              let m = t.PromiseRejectionEvent;
              if (m) {
                let N = new m(a, {
                  promise: u.promise,
                  reason: u.rejection
                });
                T.invoke(N)
              }
            }
          )
        }
      }
      t.PromiseRejectionEvent &&
      (
        c[Z('unhandledPromiseRejectionHandler')] = n('unhandledrejection'),
        c[Z('rejectionHandledHandler')] = n('rejectionhandled')
      )
    }
  ),
  e.__load_patch('queueMicrotask', (t, c, n) => {
    Re(t, n)
  })
}
function De(e) {
  e.__load_patch(
    'ZoneAwarePromise',
    (t, c, n) => {
      let a = Object.getOwnPropertyDescriptor,
      u = Object.defineProperty;
      function _(f) {
        if (f && f.toString === Object.prototype.toString) {
          let o = f.constructor &&
          f.constructor.name;
          return (o || '') + ': ' + JSON.stringify(f)
        }
        return f ? f.toString() : Object.prototype.toString.call(f)
      }
      let T = n.symbol,
      m = [],
      N = t[T('DISABLE_WRAPPING_UNCAUGHT_PROMISE_REJECTION')] !== !1,
      g = T('Promise'),
      D = T('then'),
      P = '__creationTrace__';
      n.onUnhandledError = f => {
        if (n.showUncaughtError()) {
          let o = f &&
          f.rejection;
          o ? console.error(
            'Unhandled Promise rejection:',
            o instanceof Error ? o.message : o,
            '; Zone:',
            f.zone.name,
            '; Task:',
            f.task &&
            f.task.source,
            '; Value:',
            o,
            o instanceof Error ? o.stack : void 0
          ) : console.error(f)
        }
      },
      n.microtaskDrainDone = () => {
        for (; m.length; ) {
          let f = m.shift();
          try {
            f.zone.runGuarded(() => {
              throw f.throwOriginal ? f.rejection : f
            })
          } catch (o) {
            G(o)
          }
        }
      };
      let A = T('unhandledPromiseRejectionHandler');
      function G(f) {
        n.onUnhandledError(f);
        try {
          let o = c[A];
          typeof o == 'function' &&
          o.call(this, f)
        } catch {
        }
      }
      function j(f) {
        return f &&
        f.then
      }
      function nt(f) {
        return f
      }
      function W(f) {
        return M.reject(f)
      }
      let k = T('state'),
      d = T('value'),
      H = T('finally'),
      V = T('parentPromiseValue'),
      q = T('parentPromiseState'),
      B = 'Promise.then',
      E = null,
      U = !0,
      O = !1,
      R = 0;
      function y(f, o) {
        return l => {
          try {
            X(f, o, l)
          } catch (h) {
            X(f, !1, h)
          }
        }
      }
      let I = function () {
        let f = !1;
        return function (l) {
          return function () {
            f ||
            (f = !0, l.apply(null, arguments))
          }
        }
      },
      J = 'Promise resolved with itself',
      F = T('currentTaskTrace');
      function X(f, o, l) {
        let h = I();
        if (f === l) throw new TypeError(J);
        if (f[k] === E) {
          let b = null;
          try {
            (typeof l == 'object' || typeof l == 'function') &&
            (b = l && l.then)
          } catch (C) {
            return h(() => {
              X(f, !1, C)
            }) (),
            f
          }
          if (
            o !== O &&
            l instanceof M &&
            l.hasOwnProperty(k) &&
            l.hasOwnProperty(d) &&
            l[k] !== E
          ) r(l),
          X(f, l[k], l[d]);
           else if (o !== O && typeof b == 'function') try {
            b.call(l, h(y(f, o)), h(y(f, !1)))
          } catch (C) {
            h(() => {
              X(f, !1, C)
            }) ()
          } else {
            f[k] = o;
            let C = f[d];
            if (
              f[d] = l,
              f[H] === H &&
              o === U &&
              (f[k] = f[q], f[d] = f[V]),
              o === O &&
              l instanceof Error
            ) {
              let p = c.currentTask &&
              c.currentTask.data &&
              c.currentTask.data[P];
              p &&
              u(l, F, {
                configurable: !0,
                enumerable: !1,
                writable: !0,
                value: p
              })
            }
            for (let p = 0; p < C.length; ) i(f, C[p++], C[p++], C[p++], C[p++]);
            if (C.length == 0 && o == O) {
              f[k] = R;
              let p = l;
              try {
                throw new Error('Uncaught (in promise): ' + _(l) + (l && l.stack ? `

                ` + l.stack : ''))
              } catch (w) {
                p = w
              }
              N &&
              (p.throwOriginal = !0),
              p.rejection = l,
              p.promise = f,
              p.zone = c.current,
              p.task = c.currentTask,
              m.push(p),
              n.scheduleMicroTask()
            }
          }
        }
        return f
      }
      let x = T('rejectionHandledHandler');
      function r(f) {
        if (f[k] === R) {
          try {
            let o = c[x];
            o &&
            typeof o == 'function' &&
            o.call(this, {
              rejection: f[d],
              promise: f
            })
          } catch {
          }
          f[k] = O;
          for (let o = 0; o < m.length; o++) f === m[o].promise &&
          m.splice(o, 1)
        }
      }
      function i(f, o, l, h, b) {
        r(f);
        let C = f[k],
        p = C ? typeof h == 'function' ? h : nt : typeof b == 'function' ? b : W;
        o.scheduleMicroTask(
          B,
          () => {
            try {
              let w = f[d],
              S = !!l &&
              H === l[H];
              S &&
              (l[V] = w, l[q] = C);
              let L = o.run(p, void 0, S && p !== W && p !== nt ? [] : [
                w
              ]);
              X(l, !0, L)
            } catch (w) {
              X(l, !1, w)
            }
          },
          l
        )
      }
      let s = 'function ZoneAwarePromise() { [native code] }',
      v = function () {
      },
      $ = t.AggregateError;
      class M {
        static toString() {
          return s
        }
        static resolve(o) {
          return o instanceof M ? o : X(new this(null), U, o)
        }
        static reject(o) {
          return X(new this(null), O, o)
        }
        static withResolvers() {
          let o = {};
          return o.promise = new M((l, h) => {
            o.resolve = l,
            o.reject = h
          }),
          o
        }
        static any(o) {
          if (!o || typeof o[Symbol.iterator] != 'function') return Promise.reject(new $([], 'All promises were rejected'));
          let l = [],
          h = 0;
          try {
            for (let p of o) h++,
            l.push(M.resolve(p))
          } catch {
            return Promise.reject(new $([], 'All promises were rejected'))
          }
          if (h === 0) return Promise.reject(new $([], 'All promises were rejected'));
          let b = !1,
          C = [];
          return new M(
            (p, w) => {
              for (let S = 0; S < l.length; S++) l[S].then(
                L => {
                  b ||
                  (b = !0, p(L))
                },
                L => {
                  C.push(L),
                  h--,
                  h === 0 &&
                  (b = !0, w(new $(C, 'All promises were rejected')))
                }
              )
            }
          )
        }
        static race(o) {
          let l,
          h,
          b = new this((w, S) => {
            l = w,
            h = S
          });
          function C(w) {
            l(w)
          }
          function p(w) {
            h(w)
          }
          for (let w of o) j(w) ||
          (w = this.resolve(w)),
          w.then(C, p);
          return b
        }
        static all(o) {
          return M.allWithCallback(o)
        }
        static allSettled(o) {
          return (this && this.prototype instanceof M ? this : M).allWithCallback(
            o,
            {
              thenCallback: h => ({
                status: 'fulfilled',
                value: h
              }),
              errorCallback: h => ({
                status: 'rejected',
                reason: h
              })
            }
          )
        }
        static allWithCallback(o, l) {
          let h,
          b,
          C = new this((L, z) => {
            h = L,
            b = z
          }),
          p = 2,
          w = 0,
          S = [];
          for (let L of o) {
            j(L) ||
            (L = this.resolve(L));
            let z = w;
            try {
              L.then(
                Y => {
                  S[z] = l ? l.thenCallback(Y) : Y,
                  p--,
                  p === 0 &&
                  h(S)
                },
                Y => {
                  l ? (S[z] = l.errorCallback(Y), p--, p === 0 && h(S)) : b(Y)
                }
              )
            } catch (Y) {
              b(Y)
            }
            p++,
            w++
          }
          return p -= 2,
          p === 0 &&
          h(S),
          C
        }
        constructor(o) {
          let l = this;
          if (!(l instanceof M)) throw new Error('Must be an instanceof Promise.');
          l[k] = E,
          l[d] = [];
          try {
            let h = I();
            o &&
            o(h(y(l, U)), h(y(l, O)))
          } catch (h) {
            X(l, !1, h)
          }
        }
        get[Symbol.toStringTag]() {
          return 'Promise'
        }
        get[Symbol.species]() {
          return M
        }
        then(o, l) {
          let h = this.constructor?.[Symbol.species];
          (!h || typeof h != 'function') &&
          (h = this.constructor || M);
          let b = new h(v),
          C = c.current;
          return this[k] == E ? this[d].push(C, b, o, l) : i(this, C, b, o, l),
          b
        } catch (o) {
          return this.then(null, o)
        } finally (o) {
          let l = this.constructor?.[Symbol.species];
          (!l || typeof l != 'function') &&
          (l = M);
          let h = new l(v);
          h[H] = H;
          let b = c.current;
          return this[k] == E ? this[d].push(b, h, o, o) : i(this, b, h, o, o),
          h
        }
      }
      M.resolve = M.resolve,
      M.reject = M.reject,
      M.race = M.race,
      M.all = M.all;
      let dt = t[g] = t.Promise;
      t.Promise = M;
      let pt = T('thenPatched');
      function ft(f) {
        let o = f.prototype,
        l = a(o, 'then');
        if (l && (l.writable === !1 || !l.configurable)) return;
        let h = o.then;
        o[D] = h,
        f.prototype.then = function (b, C) {
          return new M((w, S) => {
            h.call(this, w, S)
          }).then(b, C)
        },
        f[pt] = !0
      }
      n.patchThen = ft;
      function bt(f) {
        return function (o, l) {
          let h = f.apply(o, l);
          if (h instanceof M) return h;
          let b = h.constructor;
          return b[pt] ||
          ft(b),
          h
        }
      }
      return dt &&
      (ft(dt), lt(t, 'fetch', f => bt(f))),
      Promise[c.__symbol__('uncaughtPromiseErrors')] = m,
      M
    }
  )
}
function Me(e) {
  e.__load_patch(
    'toString',
    t => {
      let c = Function.prototype.toString,
      n = Z('OriginalDelegate'),
      a = Z('Promise'),
      u = Z('Error'),
      _ = function () {
        if (typeof this == 'function') {
          let g = this[n];
          if (g) return typeof g == 'function' ? c.call(g) : Object.prototype.toString.call(g);
          if (this === Promise) {
            let D = t[a];
            if (D) return c.call(D)
          }
          if (this === Error) {
            let D = t[u];
            if (D) return c.call(D)
          }
        }
        return c.call(this)
      };
      _[n] = c,
      Function.prototype.toString = _;
      let T = Object.prototype.toString,
      m = '[object Promise]';
      Object.prototype.toString = function () {
        return typeof Promise == 'function' &&
        this instanceof Promise ? m : T.call(this)
      }
    }
  )
}
function Le(e, t, c, n, a) {
  let u = Zone.__symbol__(n);
  if (t[u]) return;
  let _ = t[u] = t[n];
  t[n] = function (T, m, N) {
    return m &&
    m.prototype &&
    a.forEach(
      function (g) {
        let D = `${ c }.${ n }::` + g,
        P = m.prototype;
        try {
          if (P.hasOwnProperty(g)) {
            let A = e.ObjectGetOwnPropertyDescriptor(P, g);
            A &&
            A.value ? (
              A.value = e.wrapWithCurrentZone(A.value, D),
              e._redefineProperty(m.prototype, g, A)
            ) : P[g] &&
            (P[g] = e.wrapWithCurrentZone(P[g], D))
          } else P[g] &&
          (P[g] = e.wrapWithCurrentZone(P[g], D))
        } catch {
        }
      }
    ),
    _.call(t, T, m, N)
  },
  e.attachOriginToPatched(t[n], _)
}
function Ae(e) {
  e.__load_patch(
    'util',
    (t, c, n) => {
      let a = At(t);
      n.patchOnProperties = re,
      n.patchMethod = lt,
      n.bindArguments = Ut,
      n.patchMacroTask = ye;
      let u = c.__symbol__('BLACK_LISTED_EVENTS'),
      _ = c.__symbol__('UNPATCHED_EVENTS');
      t[_] &&
      (t[u] = t[_]),
      t[u] &&
      (c[u] = c[_] = t[u]),
      n.patchEventPrototype = Pe,
      n.patchEventTarget = we,
      n.isIEOrEdge = ve,
      n.ObjectDefineProperty = jt,
      n.ObjectGetOwnPropertyDescriptor = kt,
      n.ObjectCreate = ge,
      n.ArraySlice = Ee,
      n.patchClass = yt,
      n.wrapWithCurrentZone = Ht,
      n.filterProperties = le,
      n.attachOriginToPatched = ut,
      n._redefineProperty = Object.defineProperty,
      n.patchCallbacks = Le,
      n.getGlobalObjects = () => ({
        globalSources: oe,
        zoneSymbolEventNames: et,
        eventNames: a,
        isBrowser: zt,
        isMix: ne,
        isNode: Ct,
        TRUE_STR: ct,
        FALSE_STR: at,
        ZONE_SYMBOL_PREFIX: vt,
        ADD_EVENT_LISTENER_STR: Zt,
        REMOVE_EVENT_LISTENER_STR: $t
      })
    }
  )
}
function je(e) {
  De(e),
  Me(e),
  Ae(e)
}
var ue = Te();
je(ue);
Oe(ue);
var xe = ':';
var Gt = class {
  visitText(t, c) {
    return t.value
  }
  visitContainer(t, c) {
    return `[${ t.children.map(n => n.visit(this)).join(', ') }]`
  }
  visitIcu(t, c) {
    let n = Object.keys(t.cases).map(a => `${ a } {${ t.cases[a].visit(this) }}`);
    return `{${ t.expression }, ${ t.type }, ${ n.join(', ') }}`
  }
  visitTagPlaceholder(t, c) {
    return t.isVoid ? `<ph tag name="${ t.startName }"/>` : `<ph tag name="${ t.startName }">${ t.children.map(n => n.visit(this)).join(', ') }</ph name="${ t.closeName }">`
  }
  visitPlaceholder(t, c) {
    return t.value ? `<ph name="${ t.name }">${ t.value }</ph>` : `<ph name="${ t.name }"/>`
  }
  visitIcuPlaceholder(t, c) {
    return `<ph icu name="${ t.name }">${ t.value.visit(this) }</ph>`
  }
  visitBlockPlaceholder(t, c) {
    return `<ph block name="${ t.startName }">${ t.children.map(n => n.visit(this)).join(', ') }</ph name="${ t.closeName }">`
  }
},
He = new Gt;
var fe;
(function (e) {
  e[e.Little = 0] = 'Little',
  e[e.Big = 1] = 'Big'
}) (fe || (fe = {}));
function Ze(e, t) {
  for (let c = 1, n = 1; c < e.length; c++, n++) if (t[n] === '\\') n++;
   else if (e[c] === xe) return c;
  throw new Error(`Unterminated $localize metadata block in "${ t }".`)
}
var St = function (e, ...t) {
  if (St.translate) {
    let n = St.translate(e, t);
    e = n[0],
    t = n[1]
  }
  let c = he(e[0], e.raw[0]);
  for (let n = 1; n < e.length; n++) c += t[n - 1] + he(e[n], e.raw[n]);
  return c
},
$e = ':';
function he(e, t) {
  return t.charAt(0) === $e ? e.substring(Ze(e, t) + 1) : e
}
globalThis.$localize = St;
