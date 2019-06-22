var Gitment=function(e){function t(r){if(n[r])return n[r].exports
    var i=n[r]={i:r,l:!1,exports:{}}
    return e[r].call(i.exports,i,i.exports,t),i.l=!0,i.exports}var n={}
    return t.m=e,t.c=n,t.i=function(e){return e},t.d=function(e,n,r){t.o(e,n)||Object.defineProperty(e,n,{configurable:!1,enumerable:!0,get:r})},t.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e}
    return t.d(n,"a",n),n},t.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},t.p="",t(t.s=5)}([function(e,t,n){"use strict"
    Object.defineProperty(t,"__esModule",{value:!0})
    t.LS_ACCESS_TOKEN_KEY="gitment-comments-token",t.LS_USER_KEY="gitment-user-info",t.NOT_INITIALIZED_ERROR=Error("评论未初始化")},function(e,t,n){"use strict";(function(n){function r(e){return function(t,n,r){return r&&"function"==typeof r.value?(r.value=V(e,r.value),r.enumerable=!1,r.configurable=!0,r):Wt(e).apply(this,arguments)}}function i(e,t,n){var r="string"==typeof e?e:e.name||"<unnamed action>",i="function"==typeof e?e:t,o="function"==typeof e?t:n
    return xt("function"==typeof i,bt("m002")),xt(0===i.length,bt("m003")),xt("string"==typeof r&&r.length>0,"actions should have valid names, got: '"+r+"'"),$(r,i,o,void 0)}function o(e){return"function"==typeof e&&e.isMobxAction===!0}function a(e,t,n){var r=function(){return $(t,n,e,arguments)}
    r.isMobxAction=!0,Rt(e,t,r)}function s(e,t,n){function r(){a(u)}var i,a,s
    "string"==typeof e?(i=e,a=t,s=n):(i=e.name||"Autorun@"+wt(),a=e,s=t),xt("function"==typeof a,bt("m004")),xt(o(a)===!1,bt("m005")),s&&(a=a.bind(s))
    var u=new gn(i,function(){this.track(r)})
    return u.schedule(),u.getDisposer()}function u(e,t,n,r){var i,o,a,u
    "string"==typeof e?(i=e,o=t,a=n,u=r):(i="When@"+wt(),o=e,a=t,u=n)
    var c=s(i,function(e){if(o.call(u)){e.dispose()
    var t=te()
    a.call(u),ne(t)}})
    return c}function c(e,t,n,r){function i(){s(h)}var a,s,u,c
    "string"==typeof e?(a=e,s=t,u=n,c=r):(a=e.name||"AutorunAsync@"+wt(),s=e,u=t,c=n),xt(o(s)===!1,bt("m006")),void 0===u&&(u=1),c&&(s=s.bind(c))
    var l=!1,h=new gn(a,function(){l||(l=!0,setTimeout(function(){l=!1,h.isDisposed||h.track(i)},u))})
    return h.schedule(),h.getDisposer()}function l(e,t,n){function r(){if(!u.isDisposed){var n=!1
    u.track(function(){var t=e(u)
    n=Lt(i.compareStructural,o,t),o=t}),a&&i.fireImmediately&&t(o,u),a||n!==!0||t(o,u),a&&(a=!1)}}arguments.length>3&&_t(bt("m007")),$e(e)&&_t(bt("m008"))
    var i
    i="object"===(void 0===n?"undefined":Gt(n))?n:{},i.name=i.name||e.name||t.name||"Reaction@"+wt(),i.fireImmediately=n===!0||i.fireImmediately===!0,i.delay=i.delay||0,i.compareStructural=i.compareStructural||i.struct||!1,t=Jt(i.name,i.context?t.bind(i.context):t),i.context&&(e=e.bind(i.context))
    var o,a=!0,s=!1,u=new gn(i.name,function(){a||i.delay<1?r():s||(s=!0,setTimeout(function(){s=!1,r()},i.delay))})
    return u.schedule(),u.getDisposer()}function h(e){return ht(function(t,n,r,i,o){xt(void 0!==o,bt("m009")),xt("function"==typeof o.get,bt("m010"))
    var a=Qe(t,"")
    tt(a,n,o.get,o.set,e,!1)},function(e){var t=this.$mobx.values[e]
    if(void 0!==t)return t.get()},function(e,t){this.$mobx.values[e].set(t)},!1,!1)}function d(e,t){xt("function"==typeof e&&e.length<2,"createTransformer expects a function that accepts one argument")
    var n={},r=vn.resetId,i=function(r){function i(t,n){var i=r.call(this,function(){return e(n)},void 0,!1,"Transformer-"+e.name+"-"+t,void 0)||this
    return i.sourceIdentifier=t,i.sourceObject=n,i}return Yt(i,r),i.prototype.onBecomeUnobserved=function(){var e=this.value
    r.prototype.onBecomeUnobserved.call(this),delete n[this.sourceIdentifier],t&&t(e,this.sourceObject)},i}(ln)
    return function(e){r!==vn.resetId&&(n={},r=vn.resetId)
    var t=p(e),o=n[t]
    return o?o.get():(o=n[t]=new i(t,e),o.get())}}function p(e){if(null===e||"object"!==(void 0===e?"undefined":Gt(e)))throw Error("[mobx] transform expected some kind of object, got: "+e)
    var t=e.$transformId
    return void 0===t&&(t=wt(),Rt(e,"$transformId",t)),t}function f(e,t){return J()||console.warn(bt("m013")),Qt(e,{context:t}).get()}function m(e){for(var t=[],n=1;n<arguments.length;n++)t[n-1]=arguments[n]
    return g(e,Be,t)}function v(e){for(var t=[],n=1;n<arguments.length;n++)t[n-1]=arguments[n]
    return g(e,He,t)}function g(e,t,n){xt(arguments.length>=2,bt("m014")),xt("object"===(void 0===e?"undefined":Gt(e)),bt("m015")),xt(!Cn(e),bt("m016")),n.forEach(function(e){xt("object"===(void 0===e?"undefined":Gt(e)),bt("m017")),xt(!A(e),bt("m018"))})
    for(var r=Qe(e),i={},o=n.length-1;o>=0;o--){var a=n[o]
    for(var s in a)if(i[s]!==!0&&jt(a,s)){if(i[s]=!0,e===a&&!Pt(e,s))continue
    var u=Object.getOwnPropertyDescriptor(a,s)
    Ze(r,s,u,t)}}return e}function b(e,t){return y(ut(e,t))}function y(e){var t={name:e.name}
    return e.observing&&e.observing.length>0&&(t.dependencies=kt(e.observing).map(y)),t}function w(e,t){return _(ut(e,t))}function _(e){var t={name:e.name}
    return ue(e)&&(t.observers=ce(e).map(_)),t}function x(e,t,n){return"function"==typeof n?O(e,t,n):S(e,t)}function S(e,t){return ct(e).intercept(t)}function O(e,t,n){return ct(e,t).intercept(n)}function k(e,t){if(null===e||void 0===e)return!1
    if(void 0!==t){if(st(e)===!1)return!1
    var n=ut(e,t)
    return dn(n)}return dn(e)}function A(e,t){if(null===e||void 0===e)return!1
    if(void 0!==t){if(Fe(e)||Cn(e))throw Error(bt("m019"))
    if(st(e)){var n=e.$mobx
    return n.values&&!!n.values[t]}return!1}return st(e)||!!e.$mobx||cn(e)||wn(e)||dn(e)}function E(e){if(void 0===e&&(e=void 0),"string"==typeof arguments[1])return Zt.apply(null,arguments)
    if(xt(arguments.length<=1,bt("m021")),xt(!$e(e),bt("m020")),A(e))return e
    var t=Be(e,void 0,void 0)
    return t!==e?t:an.box(e)}function T(e){_t("Expected one or two arguments to observable."+e+". Did you accidentally try to use observable."+e+" as decorator?")}function I(e){return xt(!!e,":("),ht(function(t,n,r,i,o){Dt(t,n),xt(!o||!o.get,bt("m022"))
    var a=Qe(t,void 0)
    et(a,n,r,e)},function(e){var t=this.$mobx.values[e]
    if(void 0!==t)return t.get()},function(e,t){ot(this,e,t)},!0,!1)}function L(e,t,n,r){return"function"==typeof n?C(e,t,n,r):j(e,t,n)}function j(e,t,n){return ct(e).observe(t,n)}function C(e,t,n,r){return ct(e,t).observe(n,r)}function R(e,t,n){function r(r){return t&&n.push([e,r]),r}if(void 0===t&&(t=!0),void 0===n&&(n=[]),A(e)){if(t&&null===n&&(n=[]),t&&null!==e&&"object"===(void 0===e?"undefined":Gt(e)))for(var i=0,o=n.length;o>i;i++)if(n[i][0]===e)return n[i][1]
    if(Fe(e)){var a=r([]),s=e.map(function(e){return R(e,t,n)})
    a.length=s.length
    for(var i=0,o=s.length;o>i;i++)a[i]=s[i]
    return a}if(st(e)){var a=r({})
    for(var u in e)a[u]=R(e[u],t,n)
    return a}if(Cn(e)){var c=r({})
    return e.forEach(function(e,r){return c[r]=R(e,t,n)}),c}if($n(e))return R(e.get(),t,n)}return e}function M(e,t){return void 0===t&&(t=void 0),St(bt("m023")),P.apply(void 0,arguments)}function P(e,t){return void 0===t&&(t=void 0),$("",e)}function D(e){return console.log(e),e}function N(e,t){switch(arguments.length){case 0:if(e=vn.trackingDerivation,!e)return D(bt("m024"))
    break
    case 2:e=ut(e,t)}return e=ut(e),dn(e)?D(e.whyRun()):wn(e)?D(e.whyRun()):_t(bt("m025"))}function V(e,t){xt("function"==typeof t,bt("m026")),xt("string"==typeof e&&e.length>0,"actions should have valid names, got: '"+e+"'")
    var n=function(){return $(e,t,this,arguments)}
    return n.originalFn=t,n.isMobxAction=!0,n}function $(e,t,n,r){var i=z(e,t,n,r)
    try{return t.apply(n,r)}finally{B(i)}}function z(e,t,n,r){var i=Oe()&&!!e,o=0
    if(i){o=Date.now()
    var a=r&&r.length||0,s=Array(a)
    if(a>0)for(var u=0;a>u;u++)s[u]=r[u]
    Ae({type:"action",name:e,fn:t,object:n,arguments:s})}var c=te()
    pe()
    var l=G(!0)
    return{prevDerivation:c,prevAllowStateChanges:l,notifySpy:i,startTime:o}}function B(e){Y(e.prevAllowStateChanges),fe(),ne(e.prevDerivation),e.notifySpy&&Ee({time:Date.now()-e.startTime})}function U(e){xt(null===vn.trackingDerivation,bt("m028")),vn.strictMode=e,vn.allowStateChanges=!e}function H(){return vn.strictMode}function K(e,t){var n,r=G(e)
    try{n=t()}finally{Y(r)}return n}function G(e){var t=vn.allowStateChanges
    return vn.allowStateChanges=e,t}function Y(e){vn.allowStateChanges=e}function W(e){return e instanceof pn}function q(e){switch(e.dependenciesState){case hn.UP_TO_DATE:return!1
    case hn.NOT_TRACKING:case hn.STALE:return!0
    case hn.POSSIBLY_STALE:for(var t=te(),n=e.observing,r=n.length,i=0;r>i;i++){var o=n[i]
    if(dn(o)){try{o.get()}catch(a){return ne(t),!0}if(e.dependenciesState===hn.STALE)return ne(t),!0}}return re(e),ne(t),!1}}function J(){return null!==vn.trackingDerivation}function F(e){var t=e.observers.length>0
    vn.computationDepth>0&&t&&_t(bt("m031")+e.name),!vn.allowStateChanges&&t&&_t(bt(vn.strictMode?"m030a":"m030b")+e.name)}function X(e,t,n){re(e),e.newObserving=Array(e.observing.length+100),e.unboundDepsCount=0,e.runId=++vn.runId
    var r=vn.trackingDerivation
    vn.trackingDerivation=e
    var i
    try{i=t.call(n)}catch(o){i=new pn(o)}return vn.trackingDerivation=r,Q(e),i}function Q(e){var t=e.observing,n=e.observing=e.newObserving
    e.newObserving=null
    for(var r=0,i=e.unboundDepsCount,o=0;i>o;o++){var a=n[o]
    0===a.diffValue&&(a.diffValue=1,r!==o&&(n[r]=a),r++)}for(n.length=r,i=t.length;i--;){var a=t[i]
    0===a.diffValue&&he(a,e),a.diffValue=0}for(;r--;){var a=n[r]
    1===a.diffValue&&(a.diffValue=0,le(a,e))}}function Z(e){for(var t=e.observing,n=t.length;n--;)he(t[n],e)
    e.dependenciesState=hn.NOT_TRACKING,t.length=0}function ee(e){var t=te(),n=e()
    return ne(t),n}function te(){var e=vn.trackingDerivation
    return vn.trackingDerivation=null,e}function ne(e){vn.trackingDerivation=e}function re(e){if(e.dependenciesState!==hn.UP_TO_DATE){e.dependenciesState=hn.UP_TO_DATE
    for(var t=e.observing,n=t.length;n--;)t[n].lowestObserverState=hn.UP_TO_DATE}}function ie(){var e=yt(),t=vn
    if(e.__mobservableTrackingStack||e.__mobservableViewStack)throw Error("[mobx] An incompatible version of mobservable is already loaded.")
    if(e.__mobxGlobal&&e.__mobxGlobal.version!==t.version)throw Error("[mobx] An incompatible version of mobx is already loaded.")
    e.__mobxGlobal?vn=e.__mobxGlobal:e.__mobxGlobal=t}function oe(){return vn}function ae(){}function se(){vn.resetId++
    var e=new mn
    for(var t in e)-1===fn.indexOf(t)&&(vn[t]=e[t])
    vn.allowStateChanges=!vn.strictMode}function ue(e){return e.observers&&e.observers.length>0}function ce(e){return e.observers}function le(e,t){var n=e.observers.length
    n&&(e.observersIndexes[t.__mapid]=n),e.observers[n]=t,e.lowestObserverState>t.dependenciesState&&(e.lowestObserverState=t.dependenciesState)}function he(e,t){if(1===e.observers.length)e.observers.length=0,de(e)
    else{var n=e.observers,r=e.observersIndexes,i=n.pop()
    if(i!==t){var o=r[t.__mapid]||0
    o?r[i.__mapid]=o:delete r[i.__mapid],n[o]=i}delete r[t.__mapid]}}function de(e){e.isPendingUnobservation||(e.isPendingUnobservation=!0,vn.pendingUnobservations.push(e))}function pe(){vn.inBatch++}function fe(){if(0===--vn.inBatch){_e()
    for(var e=vn.pendingUnobservations,t=0;t<e.length;t++){var n=e[t]
    n.isPendingUnobservation=!1,0===n.observers.length&&n.onBecomeUnobserved()}vn.pendingUnobservations=[]}}function me(e){var t=vn.trackingDerivation
    null!==t?t.runId!==e.lastAccessedBy&&(e.lastAccessedBy=t.runId,t.newObserving[t.unboundDepsCount++]=e):0===e.observers.length&&de(e)}function ve(e){if(e.lowestObserverState!==hn.STALE){e.lowestObserverState=hn.STALE
    for(var t=e.observers,n=t.length;n--;){var r=t[n]
    r.dependenciesState===hn.UP_TO_DATE&&r.onBecomeStale(),r.dependenciesState=hn.STALE}}}function ge(e){if(e.lowestObserverState!==hn.STALE){e.lowestObserverState=hn.STALE
    for(var t=e.observers,n=t.length;n--;){var r=t[n]
    r.dependenciesState===hn.POSSIBLY_STALE?r.dependenciesState=hn.STALE:r.dependenciesState===hn.UP_TO_DATE&&(e.lowestObserverState=hn.UP_TO_DATE)}}}function be(e){if(e.lowestObserverState===hn.UP_TO_DATE){e.lowestObserverState=hn.POSSIBLY_STALE
    for(var t=e.observers,n=t.length;n--;){var r=t[n]
    r.dependenciesState===hn.UP_TO_DATE&&(r.dependenciesState=hn.POSSIBLY_STALE,r.onBecomeStale())}}}function ye(e){xt(this&&this.$mobx&&wn(this.$mobx),"Invalid `this`"),xt(!this.$mobx.errorHandler,"Only one onErrorHandler can be registered"),this.$mobx.errorHandler=e}function we(e){return vn.globalReactionErrorHandlers.push(e),function(){var t=vn.globalReactionErrorHandlers.indexOf(e)
    t>=0&&vn.globalReactionErrorHandlers.splice(t,1)}}function _e(){vn.inBatch>0||vn.isRunningReactions||yn(xe)}function xe(){vn.isRunningReactions=!0
    for(var e=vn.pendingReactions,t=0;e.length>0;){++t===bn&&(console.error("Reaction doesn't converge to a stable state after "+bn+" iterations. Probably there is a cycle in the reactive function: "+e[0]),e.splice(0))
    for(var n=e.splice(0),r=0,i=n.length;i>r;r++)n[r].runReaction()}vn.isRunningReactions=!1}function Se(e){var t=yn
    yn=function(n){return e(function(){return t(n)})}}function Oe(){return!!vn.spyListeners.length}function ke(e){if(vn.spyListeners.length)for(var t=vn.spyListeners,n=0,r=t.length;r>n;n++)t[n](e)}function Ae(e){var t=It({},e,{spyReportStart:!0})
    ke(t)}function Ee(e){ke(e?It({},e,_n):_n)}function Te(e){return vn.spyListeners.push(e),Ot(function(){var t=vn.spyListeners.indexOf(e);-1!==t&&vn.spyListeners.splice(t,1)})}function Ie(e){return e.interceptors&&e.interceptors.length>0}function Le(e,t){var n=e.interceptors||(e.interceptors=[])
    return n.push(t),Ot(function(){var e=n.indexOf(t);-1!==e&&n.splice(e,1)})}function je(e,t){var n=te()
    try{var r=e.interceptors
    if(r)for(var i=0,o=r.length;o>i&&(t=r[i](t),xt(!t||t.type,"Intercept handlers should return nothing or a change object"),t);i++);return t}finally{ne(n)}}function Ce(e){return e.changeListeners&&e.changeListeners.length>0}function Re(e,t){var n=e.changeListeners||(e.changeListeners=[])
    return n.push(t),Ot(function(){var e=n.indexOf(t);-1!==e&&n.splice(e,1)})}function Me(e,t){var n=te(),r=e.changeListeners
    if(r){r=r.slice()
    for(var i=0,o=r.length;o>i;i++)r[i](t)
    ne(n)}}function Pe(e){return St("asReference is deprecated, use observable.ref instead"),an.ref(e)}function De(e){return St("asStructure is deprecated. Use observable.struct, computed.struct or reaction options instead."),an.struct(e)}function Ne(e){return St("asFlat is deprecated, use observable.shallow instead"),an.shallow(e)}function Ve(e){return St("asMap is deprecated, use observable.map or observable.shallowMap instead"),an.map(e||{})}function $e(e){return"object"===(void 0===e?"undefined":Gt(e))&&null!==e&&e.isMobxModifierDescriptor===!0}function ze(e,t){return xt(!$e(t),"Modifiers cannot be nested"),{isMobxModifierDescriptor:!0,initialValue:t,enhancer:e}}function Be(e,t,n){return $e(e)&&_t("You tried to assign a modifier wrapped value to a collection, please define modifiers when creating the collection, not when modifying it"),A(e)?e:Array.isArray(e)?an.array(e,n):Tt(e)?an.object(e,n):Ut(e)?an.map(e,n):e}function Ue(e,t,n){return $e(e)&&_t("You tried to assign a modifier wrapped value to a collection, please define modifiers when creating the collection, not when modifying it"),void 0===e||null===e?e:st(e)||Fe(e)||Cn(e)?e:Array.isArray(e)?an.shallowArray(e,n):Tt(e)?an.shallowObject(e,n):Ut(e)?an.shallowMap(e,n):_t("The shallow modifier / decorator can only used in combination with arrays, objects and maps")}function He(e){return e}function Ke(e,t,n){if(Vt(e,t))return t
    if(A(e))return e
    if(Array.isArray(e))return new En(e,Ke,n)
    if(Ut(e))return new jn(e,Ke,n)
    if(Tt(e)){var r={}
    return Qe(r,n),g(r,Ke,[e]),r}return e}function Ge(e,t,n){return Vt(e,t)?t:e}function Ye(e){var t=We(e),n=qe(e)
    Object.defineProperty(En.prototype,""+e,{enumerable:!1,configurable:!0,set:t,get:n})}function We(e){return function(t){var n=this.$mobx,r=n.values
    if(e<r.length){F(n.atom)
    var i=r[e]
    if(Ie(n)){var o=je(n,{type:"update",object:n.array,index:e,newValue:t})
    if(!o)return
    t=o.newValue}t=n.enhancer(t,i)
    var a=t!==i
    a&&(r[e]=t,n.notifyArrayChildUpdate(e,t,i))}else{if(e!==r.length)throw Error("[mobx.array] Index out of bounds, "+e+" is larger than "+r.length)
    n.spliceWithArray(e,0,[t])}}}function qe(e){return function(){var t=this.$mobx
    if(t){if(e<t.values.length)return t.atom.reportObserved(),t.values[e]
    console.warn("[mobx.array] Attempt to read an array index ("+e+") that is out of bounds ("+t.values.length+"). Please check length first. Out of bound indices will not be tracked by MobX")}}}function Je(e){for(var t=On;e>t;t++)Ye(t)
    On=e}function Fe(e){return Et(e)&&In(e.$mobx)}function Xe(e){return St("`mobx.map` is deprecated, use `new ObservableMap` or `mobx.observable.map` instead"),an.map(e)}function Qe(e,t){if(st(e))return e.$mobx
    xt(Object.isExtensible(e),bt("m035")),Tt(e)||(t=(e.constructor.name||"ObservableObject")+"@"+wt()),t||(t="ObservableObject@"+wt())
    var n=new Rn(e,t)
    return Mt(e,"$mobx",n),n}function Ze(e,t,n,r){if(e.values[t])return xt("value"in n,"The property "+t+" in "+e.name+" is already observable, cannot redefine it as computed property"),void(e.target[t]=n.value)
    if("value"in n)if($e(n.value)){var i=n.value
    et(e,t,i.initialValue,i.enhancer)}else o(n.value)&&n.value.autoBind===!0?a(e.target,t,n.value.originalFn):dn(n.value)?nt(e,t,n.value):et(e,t,n.value,r)
    else tt(e,t,n.get,n.set,!1,!0)}function et(e,t,n,r){if(Dt(e.target,t),Ie(e)){var i=je(e,{object:e.target,name:t,type:"add",newValue:n})
    if(!i)return
    n=i.newValue}var o=e.values[t]=new Vn(n,r,e.name+"."+t,!1)
    n=o.value,Object.defineProperty(e.target,t,rt(t)),at(e,e.target,t,n)}function tt(e,t,n,r,i,o){o&&Dt(e.target,t),e.values[t]=new ln(n,e.target,i,e.name+"."+t,r),o&&Object.defineProperty(e.target,t,it(t))}function nt(e,t,n){var r=e.name+"."+t
    n.name=r,n.scope||(n.scope=e.target),e.values[t]=n,Object.defineProperty(e.target,t,it(t))}function rt(e){return Mn[e]||(Mn[e]={configurable:!0,enumerable:!0,get:function(){return this.$mobx.values[e].get()},set:function(t){ot(this,e,t)}})}function it(e){return Pn[e]||(Pn[e]={configurable:!0,enumerable:!1,get:function(){return this.$mobx.values[e].get()},set:function(t){return this.$mobx.values[e].set(t)}})}function ot(e,t,n){var r=e.$mobx,i=r.values[t]
    if(Ie(r)){var o=je(r,{type:"update",object:e,name:t,newValue:n})
    if(!o)return
    n=o.newValue}if(n=i.prepareNewValue(n),n!==Nn){var a=Ce(r),s=Oe(),o=a||s?{type:"update",object:e,oldValue:i.value,name:t,newValue:n}:null
    s&&Ae(o),i.setNewValue(n),a&&Me(r,o),s&&Ee()}}function at(e,t,n,r){var i=Ce(e),o=Oe(),a=i||o?{type:"add",object:t,name:n,newValue:r}:null
    o&&Ae(a),i&&Me(e,a),o&&Ee()}function st(e){return Et(e)?(pt(e),Dn(e.$mobx)):!1}function ut(e,t){if("object"===(void 0===e?"undefined":Gt(e))&&null!==e){if(Fe(e))return xt(void 0===t,bt("m036")),e.$mobx.atom
    if(Cn(e)){var n=e
    if(void 0===t)return ut(n._keys)
    var r=n._data[t]||n._hasMap[t]
    return xt(!!r,"the entry '"+t+"' does not exist in the observable map '"+lt(e)+"'"),r}if(pt(e),st(e)){if(!t)return _t("please specify a property")
    var i=e.$mobx.values[t]
    return xt(!!i,"no observable property '"+t+"' found on the observable object '"+lt(e)+"'"),i}if(cn(e)||dn(e)||wn(e))return e}else if("function"==typeof e&&wn(e.$mobx))return e.$mobx
    return _t("Cannot obtain atom from "+e)}function ct(e,t){return xt(e,"Expecting some object"),void 0!==t?ct(ut(e,t)):cn(e)||dn(e)||wn(e)?e:Cn(e)?e:(pt(e),e.$mobx?e.$mobx:void xt(!1,"Cannot obtain administration from "+e))}function lt(e,t){var n
    return n=void 0!==t?ut(e,t):st(e)||Cn(e)?ct(e):ut(e),n.name}function ht(e,t,n,r,i){function o(o,a,s,u,c){if(void 0===c&&(c=0),xt(i||ft(arguments),"This function is a decorator, but it wasn't invoked like a decorator"),s){jt(o,"__mobxLazyInitializers")||Rt(o,"__mobxLazyInitializers",o.__mobxLazyInitializers&&o.__mobxLazyInitializers.slice()||[])
    var l=s.value,h=s.initializer
    return o.__mobxLazyInitializers.push(function(t){e(t,a,h?h.call(t):l,u,s)}),{enumerable:r,configurable:!0,get:function(){return this.__mobxDidRunLazyInitializers!==!0&&pt(this),t.call(this,a)},set:function(e){this.__mobxDidRunLazyInitializers!==!0&&pt(this),n.call(this,a,e)}}}var d={enumerable:r,configurable:!0,get:function(){return this.__mobxInitializedProps&&this.__mobxInitializedProps[a]===!0||dt(this,a,void 0,e,u,s),t.call(this,a)},set:function(t){this.__mobxInitializedProps&&this.__mobxInitializedProps[a]===!0?n.call(this,a,t):dt(this,a,t,e,u,s)}}
    return(arguments.length<3||5===arguments.length&&3>c)&&Object.defineProperty(o,a,d),d}return i?function(){if(ft(arguments))return o.apply(null,arguments)
    var e=arguments,t=arguments.length
    return function(n,r,i){return o(n,r,i,e,t)}}:o}function dt(e,t,n,r,i,o){jt(e,"__mobxInitializedProps")||Rt(e,"__mobxInitializedProps",{}),e.__mobxInitializedProps[t]=!0,r(e,t,n,i,o)}function pt(e){e.__mobxDidRunLazyInitializers!==!0&&e.__mobxLazyInitializers&&(Rt(e,"__mobxDidRunLazyInitializers",!0),e.__mobxDidRunLazyInitializers&&e.__mobxLazyInitializers.forEach(function(t){return t(e)}))}function ft(e){return(2===e.length||3===e.length)&&"string"==typeof e[1]}function mt(){return"function"==typeof Symbol&&Symbol.iterator||"@@iterator"}function vt(e){xt(e[zn]!==!0,"Illegal state: cannot recycle array as iterator"),Mt(e,zn,!0)
    var t=-1
    return Mt(e,"next",function(){return t++,{done:t>=this.length,value:t<this.length?this[t]:void 0}}),e}function gt(e,t){Mt(e,mt(),t)}function bt(e){return Bn[e]}function yt(){return n}function wt(){return++vn.mobxGuid}function _t(e,t){throw xt(!1,e,t),"X"}function xt(e,t,n){if(!e)throw Error("[mobx] Invariant failed: "+t+(n?" in '"+n+"'":""))}function St(e){return-1!==Hn.indexOf(e)?!1:(Hn.push(e),console.error("[mobx] Deprecated: "+e),!0)}function Ot(e){var t=!1
    return function(){return t?void 0:(t=!0,e.apply(this,arguments))}}function kt(e){var t=[]
    return e.forEach(function(e){-1===t.indexOf(e)&&t.push(e)}),t}function At(e,t,n){if(void 0===t&&(t=100),void 0===n&&(n=" - "),!e)return""
    var r=e.slice(0,t)
    return""+r.join(n)+(e.length>t?" (... and "+(e.length-t)+"more)":"")}function Et(e){return null!==e&&"object"===(void 0===e?"undefined":Gt(e))}function Tt(e){if(null===e||"object"!==(void 0===e?"undefined":Gt(e)))return!1
    var t=Object.getPrototypeOf(e)
    return t===Object.prototype||null===t}function It(){for(var e=arguments[0],t=1,n=arguments.length;n>t;t++){var r=arguments[t]
    for(var i in r)jt(r,i)&&(e[i]=r[i])}return e}function Lt(e,t,n){return"number"==typeof t&&isNaN(t)?"number"!=typeof n||!isNaN(n):e?!Vt(t,n):t!==n}function jt(e,t){return Gn.call(e,t)}function Ct(e,t){for(var n=0;n<t.length;n++)Rt(e,t[n],e[t[n]])}function Rt(e,t,n){Object.defineProperty(e,t,{enumerable:!1,writable:!0,configurable:!0,value:n})}function Mt(e,t,n){Object.defineProperty(e,t,{enumerable:!1,writable:!1,configurable:!0,value:n})}function Pt(e,t){var n=Object.getOwnPropertyDescriptor(e,t)
    return!n||n.configurable!==!1&&n.writable!==!1}function Dt(e,t){xt(Pt(e,t),"Cannot make property '"+t+"' observable, it is not configurable and writable in the target object")}function Nt(e){var t=[]
    for(var n in e)t.push(n)
    return t}function Vt(e,t){if(null===e&&null===t)return!0
    if(void 0===e&&void 0===t)return!0
    if("object"!==(void 0===e?"undefined":Gt(e)))return e===t
    var n=zt(e),r=Bt(e)
    if(n!==zt(t))return!1
    if(r!==Bt(t))return!1
    if(n){if(e.length!==t.length)return!1
    for(var i=e.length-1;i>=0;i--)if(!Vt(e[i],t[i]))return!1
    return!0}if(r){if(e.size!==t.size)return!1
    var o=!0
    return e.forEach(function(e,n){o=o&&Vt(t.get(n),e)}),o}if("object"===(void 0===e?"undefined":Gt(e))&&"object"===(void 0===t?"undefined":Gt(t))){if(null===e||null===t)return!1
    if(Bt(e)&&Bt(t))return e.size!==t.size?!1:Vt(an.shallowMap(e).entries(),an.shallowMap(t).entries())
    if(Nt(e).length!==Nt(t).length)return!1
    for(var a in e){if(!(a in t))return!1
    if(!Vt(e[a],t[a]))return!1}return!0}return!1}function $t(e,t){var n="isMobX"+e
    return t.prototype[n]=!0,function(e){return Et(e)&&e[n]===!0}}function zt(e){return Array.isArray(e)||Fe(e)}function Bt(e){return Ut(e)||Cn(e)}function Ut(e){return void 0!==yt().Map&&e instanceof yt().Map?!0:!1}function Ht(){return"function"==typeof Symbol&&Symbol.toPrimitive||"@@toPrimitive"}function Kt(e){return null===e?null:"object"===(void 0===e?"undefined":Gt(e))?""+e:e}var Gt="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},Yt=function(){var e=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)t.hasOwnProperty(n)&&(e[n]=t[n])}
    return function(t,n){function r(){this.constructor=t}e(t,n),t.prototype=null===n?Object.create(n):(r.prototype=n.prototype,new r)}}()
    Object.defineProperty(t,"__esModule",{value:!0}),ae(),t.extras={allowStateChanges:K,deepEqual:Vt,getAtom:ut,getDebugName:lt,getDependencyTree:b,getAdministration:ct,getGlobalState:oe,getObserverTree:w,isComputingDerivation:J,isSpyEnabled:Oe,onReactionError:we,resetGlobalState:se,shareGlobalState:ie,spyReport:ke,spyReportEnd:Ee,spyReportStart:Ae,setReactionScheduler:Se},"object"===("undefined"==typeof __MOBX_DEVTOOLS_GLOBAL_HOOK__?"undefined":Gt(__MOBX_DEVTOOLS_GLOBAL_HOOK__))&&__MOBX_DEVTOOLS_GLOBAL_HOOK__.injectMobx(e.exports),e.exports["default"]=e.exports
    var Wt=ht(function(e,t,n,r,i){var o=r&&1===r.length?r[0]:n.name||t||"<unnamed action>",a=Jt(o,n)
    Rt(e,t,a)},function(e){return this[e]},function(){xt(!1,bt("m001"))},!1,!0),qt=ht(function(e,t,n){a(e,t,n)},function(e){return this[e]},function(){xt(!1,bt("m001"))},!1,!1),Jt=function(e,t,n,i){return 1===arguments.length&&"function"==typeof e?V(e.name||"<unnamed action>",e):2===arguments.length&&"function"==typeof t?V(e,t):1===arguments.length&&"string"==typeof e?r(e):r(t).apply(null,arguments)}
    t.action=Jt,Jt.bound=function(e,t,n){if("function"==typeof e){var r=V("<not yet bound action>",e)
    return r.autoBind=!0,r}return qt.apply(null,arguments)},t.runInAction=i,t.isAction=o,t.autorun=s,t.when=u,t.autorunAsync=c,t.reaction=l
    var Ft=h(!1),Xt=h(!0),Qt=function(e,t,n){if("string"==typeof t)return Ft.apply(null,arguments)
    xt("function"==typeof e,bt("m011")),xt(arguments.length<3,bt("m012"))
    var r="object"===(void 0===t?"undefined":Gt(t))?t:{}
    return r.setter="function"==typeof t?t:r.setter,new ln(e,r.context,r.compareStructural||r.struct||!1,r.name||e.name||"",r.setter)}
    t.computed=Qt,Qt.struct=Xt,t.createTransformer=d,t.expr=f,t.extendObservable=m,t.extendShallowObservable=v,t.intercept=x,t.isComputed=k,t.isObservable=A
    var Zt=I(Be),en=I(Ue),tn=I(He),nn=I(Ke),rn=I(Ge),on=function(){function e(){}return e.prototype.box=function(e,t){return arguments.length>2&&T("box"),new Vn(e,Be,t)},e.prototype.shallowBox=function(e,t){return arguments.length>2&&T("shallowBox"),new Vn(e,He,t)},e.prototype.array=function(e,t){return arguments.length>2&&T("array"),new En(e,Be,t)},e.prototype.shallowArray=function(e,t){return arguments.length>2&&T("shallowArray"),new En(e,He,t)},e.prototype.map=function(e,t){return arguments.length>2&&T("map"),new jn(e,Be,t)},e.prototype.shallowMap=function(e,t){return arguments.length>2&&T("shallowMap"),new jn(e,He,t)},e.prototype.object=function(e,t){arguments.length>2&&T("object")
    var n={}
    return Qe(n,t),m(n,e),n},e.prototype.shallowObject=function(e,t){arguments.length>2&&T("shallowObject")
    var n={}
    return Qe(n,t),v(n,e),n},e.prototype.ref=function(){return arguments.length<2?ze(He,arguments[0]):tn.apply(null,arguments)},e.prototype.shallow=function(){return arguments.length<2?ze(Ue,arguments[0]):en.apply(null,arguments)},e.prototype.deep=function(){return arguments.length<2?ze(Be,arguments[0]):Zt.apply(null,arguments)},e.prototype.struct=function(){return arguments.length<2?ze(Ke,arguments[0]):nn.apply(null,arguments)},e}()
    t.IObservableFactories=on
    var an=E
    t.observable=an,Object.keys(on.prototype).forEach(function(e){return an[e]=on.prototype[e]}),an.deep.struct=an.struct,an.ref.struct=function(){return arguments.length<2?ze(Ge,arguments[0]):rn.apply(null,arguments)},t.observe=L,t.toJS=R,t.transaction=M,t.whyRun=N,t.useStrict=U,t.isStrictModeEnabled=H
    var sn=function(){function e(e){void 0===e&&(e="Atom@"+wt()),this.name=e,this.isPendingUnobservation=!0,this.observers=[],this.observersIndexes={},this.diffValue=0,this.lastAccessedBy=0,this.lowestObserverState=hn.NOT_TRACKING}return e.prototype.onBecomeUnobserved=function(){},e.prototype.reportObserved=function(){me(this)},e.prototype.reportChanged=function(){pe(),ve(this),fe()},e.prototype.toString=function(){return this.name},e}()
    t.BaseAtom=sn
    var un=function(e){function t(t,n,r){void 0===t&&(t="Atom@"+wt()),void 0===n&&(n=Kn),void 0===r&&(r=Kn)
    var i=e.call(this,t)||this
    return i.name=t,i.onBecomeObservedHandler=n,i.onBecomeUnobservedHandler=r,i.isPendingUnobservation=!1,i.isBeingTracked=!1,i}return Yt(t,e),t.prototype.reportObserved=function(){return pe(),e.prototype.reportObserved.call(this),this.isBeingTracked||(this.isBeingTracked=!0,this.onBecomeObservedHandler()),fe(),!!vn.trackingDerivation},t.prototype.onBecomeUnobserved=function(){this.isBeingTracked=!1,this.onBecomeUnobservedHandler()},t}(sn)
    t.Atom=un
    var cn=$t("Atom",sn),ln=function(){function e(e,t,n,r,i){this.derivation=e,this.scope=t,this.compareStructural=n,this.dependenciesState=hn.NOT_TRACKING,this.observing=[],this.newObserving=null,this.isPendingUnobservation=!1,this.observers=[],this.observersIndexes={},this.diffValue=0,this.runId=0,this.lastAccessedBy=0,this.lowestObserverState=hn.UP_TO_DATE,this.unboundDepsCount=0,this.__mapid="#"+wt(),this.value=void 0,this.isComputing=!1,this.isRunningSetter=!1,this.name=r||"ComputedValue@"+wt(),i&&(this.setter=V(r+"-setter",i))}return e.prototype.onBecomeStale=function(){be(this)},e.prototype.onBecomeUnobserved=function(){xt(this.dependenciesState!==hn.NOT_TRACKING,bt("m029")),Z(this),this.value=void 0},e.prototype.get=function(){xt(!this.isComputing,"Cycle detected in computation "+this.name,this.derivation),0===vn.inBatch?(pe(),q(this)&&(this.value=this.computeValue(!1)),fe()):(me(this),q(this)&&this.trackAndCompute()&&ge(this))
    var e=this.value
    if(W(e))throw e.cause
    return e},e.prototype.peek=function(){var e=this.computeValue(!1)
    if(W(e))throw e.cause
    return e},e.prototype.set=function(e){if(this.setter){xt(!this.isRunningSetter,"The setter of computed value '"+this.name+"' is trying to update itself. Did you intend to update an _observable_ value, instead of the computed property?"),this.isRunningSetter=!0
    try{this.setter.call(this.scope,e)}finally{this.isRunningSetter=!1}}else xt(!1,"[ComputedValue '"+this.name+"'] It is not possible to assign a new value to a computed value.")},e.prototype.trackAndCompute=function(){Oe()&&ke({object:this.scope,type:"compute",fn:this.derivation})
    var e=this.value,t=this.value=this.computeValue(!0)
    return W(t)||Lt(this.compareStructural,t,e)},e.prototype.computeValue=function(e){this.isComputing=!0,vn.computationDepth++
    var t
    if(e)t=X(this,this.derivation,this.scope)
    else try{t=this.derivation.call(this.scope)}catch(n){t=new pn(n)}return vn.computationDepth--,this.isComputing=!1,t},e.prototype.observe=function(e,t){var n=this,r=!0,i=void 0
    return s(function(){var o=n.get()
    if(!r||t){var a=te()
    e({type:"update",object:n,newValue:o,oldValue:i}),ne(a)}r=!1,i=o})},e.prototype.toJSON=function(){return this.get()},e.prototype.toString=function(){return this.name+"["+this.derivation+"]"},e.prototype.valueOf=function(){return Kt(this.get())},e.prototype.whyRun=function(){var e=!!vn.trackingDerivation,t=kt(this.isComputing?this.newObserving:this.observing).map(function(e){return e.name}),n=kt(ce(this).map(function(e){return e.name}))
    return"\nWhyRun? computation '"+this.name+"':\n * Running because: "+(e?"[active] the value of this computation is needed by a reaction":this.isComputing?"[get] The value of this computed was requested outside a reaction":"[idle] not running at the moment")+"\n"+(this.dependenciesState===hn.NOT_TRACKING?bt("m032"):" * This computation will re-run if any of the following observables changes:\n    "+At(t)+"\n    "+(this.isComputing&&e?" (... or any observable accessed during the remainder of the current run)":"")+"\n	"+bt("m038")+"\n\n  * If the outcome of this computation changes, the following observers will be re-run:\n    "+At(n)+"\n")},e}()
    ln.prototype[Ht()]=ln.prototype.valueOf
    var hn,dn=$t("ComputedValue",ln)
    !function(e){e[e.NOT_TRACKING=-1]="NOT_TRACKING",e[e.UP_TO_DATE=0]="UP_TO_DATE",e[e.POSSIBLY_STALE=1]="POSSIBLY_STALE",e[e.STALE=2]="STALE"}(hn||(hn={})),t.IDerivationState=hn
    var pn=function(){function e(e){this.cause=e}return e}()
    t.untracked=ee
    var fn=["mobxGuid","resetId","spyListeners","strictMode","runId"],mn=function(){function e(){this.version=5,this.trackingDerivation=null,this.computationDepth=0,this.runId=0,this.mobxGuid=0,this.inBatch=0,this.pendingUnobservations=[],this.pendingReactions=[],this.isRunningReactions=!1,this.allowStateChanges=!0,this.strictMode=!1,this.resetId=0,this.spyListeners=[],this.globalReactionErrorHandlers=[]}return e}(),vn=new mn,gn=function(){function e(e,t){void 0===e&&(e="Reaction@"+wt()),this.name=e,this.onInvalidate=t,this.observing=[],this.newObserving=[],this.dependenciesState=hn.NOT_TRACKING,this.diffValue=0,this.runId=0,this.unboundDepsCount=0,this.__mapid="#"+wt(),this.isDisposed=!1,this._isScheduled=!1,this._isTrackPending=!1,this._isRunning=!1}return e.prototype.onBecomeStale=function(){this.schedule()},e.prototype.schedule=function(){this._isScheduled||(this._isScheduled=!0,vn.pendingReactions.push(this),_e())},e.prototype.isScheduled=function(){return this._isScheduled},e.prototype.runReaction=function(){this.isDisposed||(pe(),this._isScheduled=!1,q(this)&&(this._isTrackPending=!0,this.onInvalidate(),this._isTrackPending&&Oe()&&ke({object:this,type:"scheduled-reaction"})),fe())},e.prototype.track=function(e){pe()
    var t,n=Oe()
    n&&(t=Date.now(),Ae({object:this,type:"reaction",fn:e})),this._isRunning=!0
    var r=X(this,e,void 0)
    this._isRunning=!1,this._isTrackPending=!1,this.isDisposed&&Z(this),W(r)&&this.reportExceptionInDerivation(r.cause),n&&Ee({time:Date.now()-t}),fe()},e.prototype.reportExceptionInDerivation=function(e){var t=this
    if(this.errorHandler)return void this.errorHandler(e,this)
    var n="[mobx] Encountered an uncaught exception that was thrown by a reaction or observer component, in: '"+this,r=bt("m037")
    console.error(n||r,e),Oe()&&ke({type:"error",message:n,error:e,object:this}),vn.globalReactionErrorHandlers.forEach(function(n){return n(e,t)})},e.prototype.dispose=function(){this.isDisposed||(this.isDisposed=!0,this._isRunning||(pe(),Z(this),fe()))},e.prototype.getDisposer=function(){var e=this.dispose.bind(this)
    return e.$mobx=this,e.onError=ye,e},e.prototype.toString=function(){return"Reaction["+this.name+"]"},e.prototype.whyRun=function(){var e=kt(this._isRunning?this.newObserving:this.observing).map(function(e){return e.name})
    return"\nWhyRun? reaction '"+this.name+"':\n * Status: ["+(this.isDisposed?"stopped":this._isRunning?"running":this.isScheduled()?"scheduled":"idle")+"]\n * This reaction will re-run if any of the following observables changes:\n    "+At(e)+"\n    "+(this._isRunning?" (... or any observable accessed during the remainder of the current run)":"")+"\n	"+bt("m038")+"\n"},e}()
    t.Reaction=gn
    var bn=100,yn=function(e){return e()},wn=$t("Reaction",gn),_n={spyReportEnd:!0}
    t.spy=Te,t.asReference=Pe,t.asStructure=De,t.asFlat=Ne,t.asMap=Ve,t.isModifierDescriptor=$e
    var xn=1e4,Sn=function(){var e=!1,t={}
    return Object.defineProperty(t,"0",{set:function(){e=!0}}),Object.create(t)[0]=1,e===!1}(),On=0,kn=function(){function e(){}return e}()
    kn.prototype=[]
    var An=function(){function e(e,t,n,r){this.array=n,this.owned=r,this.lastKnownLength=0,this.interceptors=null,this.changeListeners=null,this.atom=new sn(e||"ObservableArray@"+wt()),this.enhancer=function(n,r){return t(n,r,e+"[..]")}}return e.prototype.intercept=function(e){return Le(this,e)},e.prototype.observe=function(e,t){return void 0===t&&(t=!1),t&&e({object:this.array,type:"splice",index:0,added:this.values.slice(),addedCount:this.values.length,removed:[],removedCount:0}),Re(this,e)},e.prototype.getArrayLength=function(){return this.atom.reportObserved(),this.values.length},e.prototype.setArrayLength=function(e){if("number"!=typeof e||0>e)throw Error("[mobx.array] Out of range: "+e)
    var t=this.values.length
    if(e!==t)if(e>t){for(var n=Array(e-t),r=0;e-t>r;r++)n[r]=void 0
    this.spliceWithArray(t,0,n)}else this.spliceWithArray(e,t-e)},e.prototype.updateArrayLength=function(e,t){if(e!==this.lastKnownLength)throw Error("[mobx] Modification exception: the internal structure of an observable array was changed. Did you use peek() to change it?")
    this.lastKnownLength+=t,t>0&&e+t+1>On&&Je(e+t+1)},e.prototype.spliceWithArray=function(e,t,n){var r=this
    F(this.atom)
    var i=this.values.length
    if(void 0===e?e=0:e>i?e=i:0>e&&(e=Math.max(0,i+e)),t=1===arguments.length?i-e:void 0===t||null===t?0:Math.max(0,Math.min(t,i-e)),void 0===n&&(n=[]),Ie(this)){var o=je(this,{object:this.array,type:"splice",index:e,removedCount:t,added:n})
    if(!o)return Un
    t=o.removedCount,n=o.added}n=n.map(function(e){return r.enhancer(e,void 0)})
    var a=n.length-t
    this.updateArrayLength(i,a)
    var s=this.spliceItemsIntoValues(e,t,n)
    return(0!==t||0!==n.length)&&this.notifyArraySplice(e,n,s),s},e.prototype.spliceItemsIntoValues=function(e,t,n){if(n.length<xn)return(i=this.values).splice.apply(i,[e,t].concat(n))
    var r=this.values.slice(e,e+t)
    return this.values=this.values.slice(0,e).concat(n,this.values.slice(e+t)),r
    var i},e.prototype.notifyArrayChildUpdate=function(e,t,n){var r=!this.owned&&Oe(),i=Ce(this),o=i||r?{object:this.array,type:"update",index:e,newValue:t,oldValue:n}:null
    r&&Ae(o),this.atom.reportChanged(),i&&Me(this,o),r&&Ee()},e.prototype.notifyArraySplice=function(e,t,n){var r=!this.owned&&Oe(),i=Ce(this),o=i||r?{object:this.array,type:"splice",index:e,removed:n,added:t,removedCount:n.length,addedCount:t.length}:null
    r&&Ae(o),this.atom.reportChanged(),i&&Me(this,o),r&&Ee()},e}(),En=function(e){function t(t,n,r,i){void 0===r&&(r="ObservableArray@"+wt()),void 0===i&&(i=!1)
    var o=e.call(this)||this,a=new An(r,n,o,i)
    return Mt(o,"$mobx",a),t&&t.length?(a.updateArrayLength(0,t.length),a.values=t.map(function(e){return n(e,void 0,r+"[..]")}),a.notifyArraySplice(0,a.values.slice(),Un)):a.values=[],Sn&&Object.defineProperty(a.array,"0",Tn),o}return Yt(t,e),t.prototype.intercept=function(e){return this.$mobx.intercept(e)},t.prototype.observe=function(e,t){return void 0===t&&(t=!1),this.$mobx.observe(e,t)},t.prototype.clear=function(){return this.splice(0)},t.prototype.concat=function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t]
    return this.$mobx.atom.reportObserved(),Array.prototype.concat.apply(this.peek(),e.map(function(e){return Fe(e)?e.peek():e}))},t.prototype.replace=function(e){return this.$mobx.spliceWithArray(0,this.$mobx.values.length,e)},t.prototype.toJS=function(){return this.slice()},t.prototype.toJSON=function(){return this.toJS()},t.prototype.peek=function(){return this.$mobx.values},t.prototype.find=function(e,t,n){void 0===n&&(n=0),this.$mobx.atom.reportObserved()
    for(var r=this.$mobx.values,i=r.length,o=n;i>o;o++)if(e.call(t,r[o],o,this))return r[o]},t.prototype.splice=function(e,t){for(var n=[],r=2;r<arguments.length;r++)n[r-2]=arguments[r]
    switch(arguments.length){case 0:return[]
    case 1:return this.$mobx.spliceWithArray(e)
    case 2:return this.$mobx.spliceWithArray(e,t)}return this.$mobx.spliceWithArray(e,t,n)},t.prototype.spliceWithArray=function(e,t,n){return this.$mobx.spliceWithArray(e,t,n)},t.prototype.push=function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t]
    var n=this.$mobx
    return n.spliceWithArray(n.values.length,0,e),n.values.length},t.prototype.pop=function(){return this.splice(Math.max(this.$mobx.values.length-1,0),1)[0]},t.prototype.shift=function(){return this.splice(0,1)[0]},t.prototype.unshift=function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t]
    var n=this.$mobx
    return n.spliceWithArray(0,0,e),n.values.length},t.prototype.reverse=function(){this.$mobx.atom.reportObserved()
    var e=this.slice()
    return e.reverse.apply(e,arguments)},t.prototype.sort=function(e){this.$mobx.atom.reportObserved()
    var t=this.slice()
    return t.sort.apply(t,arguments)},t.prototype.remove=function(e){var t=this.$mobx.values.indexOf(e)
    return t>-1?(this.splice(t,1),!0):!1},t.prototype.move=function(e,t){function n(e){if(0>e)throw Error("[mobx.array] Index out of bounds: "+e+" is negative")
    var t=this.$mobx.values.length
    if(e>=t)throw Error("[mobx.array] Index out of bounds: "+e+" is not smaller than "+t)}if(n.call(this,e),n.call(this,t),e!==t){var r,i=this.$mobx.values
    r=t>e?i.slice(0,e).concat(i.slice(e+1,t+1),[i[e]],i.slice(t+1)):i.slice(0,t).concat([i[e]],i.slice(t,e),i.slice(e+1)),this.replace(r)}},t.prototype.toString=function(){return this.$mobx.atom.reportObserved(),Array.prototype.toString.apply(this.$mobx.values,arguments)},t.prototype.toLocaleString=function(){return this.$mobx.atom.reportObserved(),Array.prototype.toLocaleString.apply(this.$mobx.values,arguments)},t}(kn)
    gt(En.prototype,function(){return vt(this.slice())}),Ct(En.prototype,["constructor","intercept","observe","clear","concat","replace","toJS","toJSON","peek","find","splice","spliceWithArray","push","pop","shift","unshift","reverse","sort","remove","move","toString","toLocaleString"]),Object.defineProperty(En.prototype,"length",{enumerable:!1,configurable:!0,get:function(){return this.$mobx.getArrayLength()},set:function(e){this.$mobx.setArrayLength(e)}}),["every","filter","forEach","indexOf","join","lastIndexOf","map","reduce","reduceRight","slice","some"].forEach(function(e){var t=Array.prototype[e]
    xt("function"==typeof t,"Base function not defined on Array prototype: '"+e+"'"),Rt(En.prototype,e,function(){return this.$mobx.atom.reportObserved(),t.apply(this.$mobx.values,arguments)})})
    var Tn={configurable:!0,enumerable:!1,set:We(0),get:qe(0)}
    Je(1e3)
    var In=$t("ObservableArrayAdministration",An)
    t.isObservableArray=Fe
    var Ln={},jn=function(){function e(e,t,n){void 0===t&&(t=Be),void 0===n&&(n="ObservableMap@"+wt()),this.enhancer=t,this.name=n,this.$mobx=Ln,this._data={},this._hasMap={},this._keys=new En(void 0,He,this.name+".keys()",!0),this.interceptors=null,this.changeListeners=null,this.merge(e)}return e.prototype._has=function(e){return void 0!==this._data[e]},e.prototype.has=function(e){return this.isValidKey(e)?(e=""+e,this._hasMap[e]?this._hasMap[e].get():this._updateHasMapEntry(e,!1).get()):!1},e.prototype.set=function(e,t){this.assertValidKey(e),e=""+e
    var n=this._has(e)
    if(Ie(this)){var r=je(this,{type:n?"update":"add",object:this,newValue:t,name:e})
    if(!r)return this
    t=r.newValue}return n?this._updateValue(e,t):this._addValue(e,t),this},e.prototype["delete"]=function(e){var t=this
    if(this.assertValidKey(e),e=""+e,Ie(this)){var n=je(this,{type:"delete",object:this,name:e})
    if(!n)return!1}if(this._has(e)){var r=Oe(),i=Ce(this),n=i||r?{type:"delete",object:this,oldValue:this._data[e].value,name:e}:null
    return r&&Ae(n),P(function(){t._keys.remove(e),t._updateHasMapEntry(e,!1)
    var n=t._data[e]
    n.setNewValue(void 0),t._data[e]=void 0}),i&&Me(this,n),r&&Ee(),!0}return!1},e.prototype._updateHasMapEntry=function(e,t){var n=this._hasMap[e]
    return n?n.setNewValue(t):n=this._hasMap[e]=new Vn(t,He,this.name+"."+e+"?",!1),n},e.prototype._updateValue=function(e,t){var n=this._data[e]
    if(t=n.prepareNewValue(t),t!==Nn){var r=Oe(),i=Ce(this),o=i||r?{type:"update",object:this,oldValue:n.value,name:e,newValue:t}:null
    r&&Ae(o),n.setNewValue(t),i&&Me(this,o),r&&Ee()}},e.prototype._addValue=function(e,t){var n=this
    P(function(){var r=n._data[e]=new Vn(t,n.enhancer,n.name+"."+e,!1)
    t=r.value,n._updateHasMapEntry(e,!0),n._keys.push(e)})
    var r=Oe(),i=Ce(this),o=i||r?{type:"add",object:this,name:e,newValue:t}:null
    r&&Ae(o),i&&Me(this,o),r&&Ee()},e.prototype.get=function(e){return e=""+e,this.has(e)?this._data[e].get():void 0},e.prototype.keys=function(){return vt(this._keys.slice())},e.prototype.values=function(){return vt(this._keys.map(this.get,this))},e.prototype.entries=function(){var e=this
    return vt(this._keys.map(function(t){return[t,e.get(t)]}))},e.prototype.forEach=function(e,t){var n=this
    this.keys().forEach(function(r){return e.call(t,n.get(r),r,n)})},e.prototype.merge=function(e){var t=this
    return Cn(e)&&(e=e.toJS()),P(function(){Tt(e)?Object.keys(e).forEach(function(n){return t.set(n,e[n])}):Array.isArray(e)?e.forEach(function(e){var n=e[0],r=e[1]
    return t.set(n,r)}):Ut(e)?e.forEach(function(e,n){return t.set(n,e)}):null!==e&&void 0!==e&&_t("Cannot initialize map from "+e)}),this},e.prototype.clear=function(){var e=this
    P(function(){ee(function(){e.keys().forEach(e["delete"],e)})})},e.prototype.replace=function(e){var t=this
    return P(function(){t.clear(),t.merge(e)}),this},Object.defineProperty(e.prototype,"size",{get:function(){return this._keys.length},enumerable:!0,configurable:!0}),e.prototype.toJS=function(){var e=this,t={}
    return this.keys().forEach(function(n){return t[n]=e.get(n)}),t},e.prototype.toJSON=function(){return this.toJS()},e.prototype.isValidKey=function(e){return null===e||void 0===e?!1:"string"==typeof e||"number"==typeof e||"boolean"==typeof e?!0:!1},e.prototype.assertValidKey=function(e){if(!this.isValidKey(e))throw Error("[mobx.map] Invalid key: '"+e+"', only strings, numbers and booleans are accepted as key in observable maps.")},e.prototype.toString=function(){var e=this
    return this.name+"[{ "+this.keys().map(function(t){return t+": "+e.get(t)}).join(", ")+" }]"},e.prototype.observe=function(e,t){return xt(t!==!0,bt("m033")),Re(this,e)},e.prototype.intercept=function(e){return Le(this,e)},e}()
    t.ObservableMap=jn,gt(jn.prototype,function(){return this.entries()}),t.map=Xe
    var Cn=$t("ObservableMap",jn)
    t.isObservableMap=Cn
    var Rn=function(){function e(e,t){this.target=e,this.name=t,this.values={},this.changeListeners=null,this.interceptors=null}return e.prototype.observe=function(e,t){return xt(t!==!0,"`observe` doesn't support the fire immediately property for observable objects."),Re(this,e)},e.prototype.intercept=function(e){return Le(this,e)},e}(),Mn={},Pn={},Dn=$t("ObservableObjectAdministration",Rn)
    t.isObservableObject=st
    var Nn={},Vn=function(e){function t(t,n,r,i){void 0===r&&(r="ObservableValue@"+wt()),void 0===i&&(i=!0)
    var o=e.call(this,r)||this
    return o.enhancer=n,o.hasUnreportedChange=!1,o.value=n(t,void 0,r),i&&Oe()&&ke({type:"create",object:o,newValue:o.value}),o}return Yt(t,e),t.prototype.set=function(e){var t=this.value
    if(e=this.prepareNewValue(e),e!==Nn){var n=Oe()
    n&&Ae({type:"update",object:this,newValue:e,oldValue:t}),this.setNewValue(e),n&&Ee()}},t.prototype.prepareNewValue=function(e){if(F(this),Ie(this)){var t=je(this,{object:this,type:"update",newValue:e})
    if(!t)return Nn
    e=t.newValue}return e=this.enhancer(e,this.value,this.name),this.value!==e?e:Nn},t.prototype.setNewValue=function(e){var t=this.value
    this.value=e,this.reportChanged(),Ce(this)&&Me(this,{type:"update",object:this,newValue:e,oldValue:t})},t.prototype.get=function(){return this.reportObserved(),this.value},t.prototype.intercept=function(e){return Le(this,e)},t.prototype.observe=function(e,t){return t&&e({object:this,type:"update",newValue:this.value,oldValue:void 0}),Re(this,e)},t.prototype.toJSON=function(){return this.get()},t.prototype.toString=function(){return this.name+"["+this.value+"]"},t.prototype.valueOf=function(){return Kt(this.get())},t}(sn)
    Vn.prototype[Ht()]=Vn.prototype.valueOf
    var $n=$t("ObservableValue",Vn)
    t.isBoxedObservable=$n
    var zn="__$$iterating",Bn={m001:"It is not allowed to assign new values to @action fields",m002:"`runInAction` expects a function",m003:"`runInAction` expects a function without arguments",m004:"autorun expects a function",m005:"Warning: attempted to pass an action to autorun. Actions are untracked and will not trigger on state changes. Use `reaction` or wrap only your state modification code in an action.",m006:"Warning: attempted to pass an action to autorunAsync. Actions are untracked and will not trigger on state changes. Use `reaction` or wrap only your state modification code in an action.",m007:"reaction only accepts 2 or 3 arguments. If migrating from MobX 2, please provide an options object",m008:"wrapping reaction expression in `asReference` is no longer supported, use options object instead",m009:"@computed can only be used on getter functions, like: '@computed get myProps() { return ...; }'. It looks like it was used on a property.",m010:"@computed can only be used on getter functions, like: '@computed get myProps() { return ...; }'",m011:"First argument to `computed` should be an expression. If using computed as decorator, don't pass it arguments",m012:"computed takes one or two arguments if used as function",m013:"[mobx.expr] 'expr' should only be used inside other reactive functions.",m014:"extendObservable expected 2 or more arguments",m015:"extendObservable expects an object as first argument",m016:"extendObservable should not be used on maps, use map.merge instead",m017:"all arguments of extendObservable should be objects",m018:"extending an object with another observable (object) is not supported. Please construct an explicit propertymap, using `toJS` if need. See issue #540",m019:"[mobx.isObservable] isObservable(object, propertyName) is not supported for arrays and maps. Use map.has or array.length instead.",m020:"modifiers can only be used for individual object properties",m021:"observable expects zero or one arguments",m022:"@observable can not be used on getters, use @computed instead",m023:"Using `transaction` is deprecated, use `runInAction` or `(@)action` instead.",m024:"whyRun() can only be used if a derivation is active, or by passing an computed value / reaction explicitly. If you invoked whyRun from inside a computation; the computation is currently suspended but re-evaluating because somebody requested its value.",m025:"whyRun can only be used on reactions and computed values",m026:"`action` can only be invoked on functions",m028:"It is not allowed to set `useStrict` when a derivation is running",m029:"INTERNAL ERROR only onBecomeUnobserved shouldn't be called twice in a row",m030a:"Since strict-mode is enabled, changing observed observable values outside actions is not allowed. Please wrap the code in an `action` if this change is intended. Tried to modify: ",m030b:"Side effects like changing state are not allowed at this point. Are you trying to modify state from, for example, the render function of a React component? Tried to modify: ",m031:"Computed values are not allowed to not cause side effects by changing observables that are already being observed. Tried to modify: ",m032:"* This computation is suspended (not in use by any reaction) and won't run automatically.\n	Didn't expect this computation to be suspended at this point?\n	  1. Make sure this computation is used by a reaction (reaction, autorun, observer).\n	  2. Check whether you are using this computation synchronously (in the same stack as they reaction that needs it).",m033:"`observe` doesn't support the fire immediately property for observable maps.",m034:"`mobx.map` is deprecated, use `new ObservableMap` or `mobx.observable.map` instead",m035:"Cannot make the designated object observable; it is not extensible",m036:"It is not possible to get index atoms from arrays",m037:'Hi there! I\'m sorry you have just run into an exception.\nIf your debugger ends up here, know that some reaction (like the render() of an observer component, autorun or reaction)\nthrew an exception and that mobx caught it, to avoid that it brings the rest of your application down.\nThe original cause of the exception (the code that caused this reaction to run (again)), is still in the stack.\n\nHowever, more interesting is the actual stack trace of the error itself.\nHopefully the error is an instanceof Error, because in that case you can inspect the original stack of the error from where it was thrown.\nSee `error.stack` property, or press the very subtle "(...)" link you see near the console.error message that probably brought you here.\nThat stack is more interesting than the stack of this console.error itself.\n\nIf the exception you see is an exception you created yourself, make sure to use `throw new Error("Oops")` instead of `throw "Oops"`,\nbecause the javascript environment will only preserve the original stack trace in the first form.\n\nYou can also make sure the debugger pauses the next time this very same exception is thrown by enabling "Pause on caught exception".\n(Note that it might pause on many other, unrelated exception as well).\n\nIf that all doesn\'t help you out, feel free to open an issue https://github.com/mobxjs/mobx/issues!\n',m038:"Missing items in this list?\n    1. Check whether all used values are properly marked as observable (use isObservable to verify)\n    2. Make sure you didn't dereference values too early. MobX observes props, not primitives. E.g: use 'person.name' instead of 'name' in your computation.\n"},Un=[]
    Object.freeze(Un)
    var Hn=[],Kn=function(){},Gn=Object.prototype.hasOwnProperty
    t.isArrayLike=zt}).call(t,n(4))},function(e,t,n){"use strict"
    function r(e,t){var n=e.meta,r=e.user,i=e.reactions,o=document.createElement("div")
    o.lang="en-US",o.className="gitment-container gitment-header-container"
    var a=document.createElement("span"),s=i.find(function(e){return"heart"===e.content&&e.user.login===r.login})
    a.className="gitment-header-like-btn",a.innerHTML="\n    "+c.heart+"\n    "+(s?"取消赞":"赞")+"\n    "+(n.reactions&&n.reactions.heart?" • <strong>"+n.reactions.heart+"</strong> 人点赞":"")+"\n  ",s?(a.classList.add("liked"),a.onclick=function(){return t.unlike()}):(a.classList.remove("liked"),a.onclick=function(){return t.like()}),o.appendChild(a)
    var u=document.createElement("span")
    u.innerHTML="\n    "+(n.comments?" • <strong>"+n.comments+"</strong> 条评论":"")+"\n  ",o.appendChild(u)
    var l=document.createElement("a")
    return l.className="gitment-header-issue-link",l.href=n.html_url,l.target="_blank",l.innerText="Issue 页面",o.appendChild(l),o}function i(e,t){var n=e.meta,r=e.comments,i=e.commentReactions,o=e.currentPage,a=e.user,s=e.error,u=document.createElement("div")
    if(u.lang="en-US",u.className="gitment-container gitment-comments-container",s){var h=document.createElement("div")
    if(h.className="gitment-comments-error",s===l.NOT_INITIALIZED_ERROR&&a.login&&a.login.toLowerCase()===t.owner.toLowerCase()){var d=document.createElement("div"),p=document.createElement("button")
    p.className="gitment-comments-init-btn",p.onclick=function(){p.setAttribute("disabled",!0),t.init()["catch"](function(e){p.removeAttribute("disabled"),alert(e)})},p.innerText="初始化评论",d.appendChild(p),h.appendChild(d)}else h.innerText=s
    return u.appendChild(h),u}if(void 0===r){var f=document.createElement("div")
    return f.innerText="加载中......",f.className="gitment-comments-loading",u.appendChild(f),u}if(!r.length){var m=document.createElement("div")
    return m.className="gitment-comments-empty",m.innerText="# NULL #",u.appendChild(m),u}var v=document.createElement("ul")
    if(v.className="gitment-comments-list",r.forEach(function(e){var n=new Date(e.created_at),r=new Date(e.updated_at),o=document.createElement("li")
    o.className="gitment-comment",o.innerHTML='\n      <a class="gitment-comment-avatar" href="'+e.user.html_url+'" target="_blank">\n        <img class="gitment-comment-avatar-img" src="'+e.user.avatar_url+'"/>\n      </a>\n      <div class="gitment-comment-main">\n        <div class="gitment-comment-header">\n          <a class="gitment-comment-name" href="'+e.user.html_url+'" target="_blank">\n            '+e.user.login+'\n          </a>\n          发表于\n          <span title="'+n+'">'+n.toDateString()+"</span>\n          "+(""+n!=""+r?' • <span title="最后修改 '+r+'">有修改</span>':"")+'\n          <div class="gitment-comment-like-btn">'+c.heart+" "+(e.reactions.heart||"")+'</div>\n        </div>\n        <div class="gitment-comment-body gitment-markdown">'+e.body_html+"</div>\n      </div>\n    "
    var s=o.querySelector(".gitment-comment-like-btn"),u=i[e.id]&&i[e.id].find(function(e){return"heart"===e.content&&e.user.login===a.login})
    u?(s.classList.add("liked"),s.onclick=function(){return t.unlikeAComment(e.id)}):(s.classList.remove("liked"),s.onclick=function(){return t.likeAComment(e.id)})
    var l=document.createElement("img"),h=o.querySelector(".gitment-comment-body")
    l.className="gitment-hidden",l.src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",l.onload=function(){h.clientHeight>t.maxCommentHeight&&(h.classList.add("gitment-comment-body-folded"),h.style.maxHeight=t.maxCommentHeight+"px",h.title="点击展开",h.onclick=function(){h.classList.remove("gitment-comment-body-folded"),h.style.maxHeight="",h.title="",h.onclick=null})},o.appendChild(l),v.appendChild(o)}),u.appendChild(v),n){var g=Math.ceil(n.comments/t.perPage)
    if(g>1){var b=document.createElement("ul")
    if(b.className="gitment-comments-pagination",o>1){var y=document.createElement("li")
    y.className="gitment-comments-page-item",y.innerText="上页",y.onclick=function(){return t["goto"](o-1)},b.appendChild(y)}for(var w=function(e){var n=document.createElement("li")
    n.className="gitment-comments-page-item",n.innerText=e,n.onclick=function(){return t["goto"](e)},o===e&&n.classList.add("gitment-selected"),b.appendChild(n)},_=1;g>=_;_++)w(_)
    if(g>o){var x=document.createElement("li")
    x.className="gitment-comments-page-item",x.innerText="下页",x.onclick=function(){return t["goto"](o+1)},b.appendChild(x)}u.appendChild(b)}}return u}function o(e,t){var n=e.user,r=e.error,i=document.createElement("div")
    i.lang="en-US",i.className="gitment-container gitment-editor-container"
    var o=n.login&&!r?"":"disabled",a=n.login?"":"登录后评论"
    i.innerHTML="\n      "+(n.login?'<a class="gitment-editor-avatar" href="'+n.html_url+'" target="_blank">\n            <img class="gitment-editor-avatar-img" src="'+n.avatar_url+'"/>\n          </a>':n.isLoggingIn?'<div class="gitment-editor-avatar">'+c.spinner+"</div>":'<a class="gitment-editor-avatar" href="'+t.loginLink+'" title="login with GitHub">\n              '+c.github+"\n            </a>")+'\n    </a>\n    <div class="gitment-editor-main">\n      <div class="gitment-editor-header">\n        <nav class="gitment-editor-tabs">\n          <button class="gitment-editor-tab gitment-selected">编辑</button>\n          <button class="gitment-editor-tab">预览</button>\n        </nav>\n        <div class="gitment-editor-login">\n          '+(n.login?'<a class="gitment-editor-logout-link">登出</a>':n.isLoggingIn?"正在登录......":'<a class="gitment-editor-login-link" href="'+t.loginLink+'">GitHub 登录</a>')+'\n        </div>\n      </div>\n      <div class="gitment-editor-body">\n        <div class="gitment-editor-write-field">\n          <textarea placeholder="可以D人了......" title="'+a+'" '+o+'></textarea>\n        </div>\n        <div class="gitment-editor-preview-field gitment-hidden">\n          <div class="gitment-editor-preview gitment-markdown"></div>\n        </div>\n      </div>\n    </div>\n    <div class="gitment-editor-footer">\n      <a class="gitment-editor-footer-tip" href="https://guides.github.com/features/mastering-markdown/" target="_blank">\n        可以使用 Markdown 编辑\n      </a>\n      <button class="gitment-editor-submit" title="'+a+'" '+o+">评论</button>\n    </div>\n  ",n.login&&(i.querySelector(".gitment-editor-logout-link").onclick=function(){return t.logout()})
    var s=i.querySelector(".gitment-editor-write-field"),l=i.querySelector(".gitment-editor-preview-field"),h=s.querySelector("textarea")
    h.oninput=function(){h.style.height="auto"
    var e=window.getComputedStyle(h,null),t=parseInt(e.height,10),n=h.clientHeight,r=h.scrollHeight
    r>n&&(h.style.height=t+r-n+"px")}
    var d=i.querySelectorAll(".gitment-editor-tab"),p=u(d,2),f=p[0],m=p[1]
    f.onclick=function(){f.classList.add("gitment-selected"),m.classList.remove("gitment-selected"),s.classList.remove("gitment-hidden"),l.classList.add("gitment-hidden"),h.focus()},m.onclick=function(){m.classList.add("gitment-selected"),f.classList.remove("gitment-selected"),l.classList.remove("gitment-hidden"),s.classList.add("gitment-hidden")
    var e=l.querySelector(".gitment-editor-preview"),n=h.value.trim()
    return n?(e.innerText="预览加载中......",void t.markdown(n).then(function(t){return e.innerHTML=t,e.innerHTML})):void(e.innerText="无可奉告")}
    var v=i.querySelector(".gitment-editor-submit")
    return v.onclick=function(){v.innerText="提交中......",v.setAttribute("disabled",!0),t.post(h.value.trim()).then(function(e){h.value="",h.style.height="auto",v.removeAttribute("disabled"),v.innerText="评论"})["catch"](function(e){alert(e),v.removeAttribute("disabled"),v.innerText="评论"})},i}function a(){var e=document.createElement("div")
    return e.lang="en-US",e.className="gitment-container gitment-footer-container",e.innerHTML='\n    Powered by\n    <a class="gitment-footer-project-link" href="https://github.com/imsun/gitment" target="_blank">\n      Gitment\n    </a>\n  ',e}function s(e,t){var n=document.createElement("div")
    return n.lang="en-US",n.className="gitment-container gitment-root-container",n.appendChild(t.renderHeader(e,t)),n.appendChild(t.renderComments(e,t)),n.appendChild(t.renderEditor(e,t)),n.appendChild(t.renderFooter(e,t)),n}Object.defineProperty(t,"__esModule",{value:!0})
    var u=function(){function e(e,t){var n=[],r=!0,i=!1,o=void 0
    try{for(var a,s=e[Symbol.iterator]();!(r=(a=s.next()).done)&&(n.push(a.value),!t||n.length!==t);r=!0);}catch(u){i=!0,o=u}finally{try{!r&&s["return"]&&s["return"]()}finally{if(i)throw o}}return n}return function(t,n){if(Array.isArray(t))return t
    if(Symbol.iterator in Object(t))return e(t,n)
    throw new TypeError("Invalid attempt to destructure non-iterable instance")}}(),c=n(6),l=n(0)
    t["default"]={render:s,renderHeader:r,renderComments:i,renderEditor:o,renderFooter:a}},function(e,t,n){"use strict"
    function r(e){var t=void 0
    return t=e instanceof Element?e:s(e)?document.getElementById(e):document.createElement("div")}function i(e){return function(t){var n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"https://api.github.com",i=new XMLHttpRequest,o=localStorage.getItem(a.LS_ACCESS_TOKEN_KEY),s=""+r+t,c=null;("GET"===e||"DELETE"===e)&&(s+=u.stringify(n))
    var l=new Promise(function(e,t){i.addEventListener("load",function(){var n=i.getResponseHeader("content-type"),r=i.responseText
    if(!/json/.test(n))return void e(r)
    var o=i.responseText?JSON.parse(r):{}
    o.message?t(Error(o.message)):e(o)}),i.addEventListener("error",function(e){return t(e)})})
    return i.open(e,s,!0),i.setRequestHeader("Accept","application/vnd.github.squirrel-girl-preview, application/vnd.github.html+json"),o&&i.setRequestHeader("Authorization","token "+o),"GET"!==e&&"DELETE"!==e&&(c=JSON.stringify(n),i.setRequestHeader("Content-Type","application/json")),i.send(c),l}}Object.defineProperty(t,"__esModule",{value:!0}),t.http=t.Query=t.isString=void 0
    var o=function(){function e(e,t){var n=[],r=!0,i=!1,o=void 0
    try{for(var a,s=e[Symbol.iterator]();!(r=(a=s.next()).done)&&(n.push(a.value),!t||n.length!==t);r=!0);}catch(u){i=!0,o=u}finally{try{!r&&s["return"]&&s["return"]()}finally{if(i)throw o}}return n}return function(t,n){if(Array.isArray(t))return t
    if(Symbol.iterator in Object(t))return e(t,n)
    throw new TypeError("Invalid attempt to destructure non-iterable instance")}}()
    t.getTargetContainer=r
    var a=n(0),s=t.isString=function(e){return"[object String]"===toString.call(e)},u=t.Query={parse:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:window.location.search
    if(!e)return{}
    var t="?"===e[0]?e.substring(1):e,n={}
    return t.split("&").forEach(function(e){var t=e.split("="),r=o(t,2),i=r[0],a=r[1]
    i&&(n[i]=a)}),n},stringify:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"?",n=Object.keys(e).map(function(t){return t+"="+encodeURIComponent(e[t]||"")}).join("&")
    return n?t+n:""}}
    t.http={get:i("GET"),post:i("POST"),"delete":i("DELETE"),put:i("PUT")}},function(e,t,n){"use strict"
    var r,i="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e}
    r=function(){return this}()
    try{r=r||Function("return this")()||(1,eval)("this")}catch(o){"object"===("undefined"==typeof window?"undefined":i(window))&&(r=window)}e.exports=r},function(e,t,n){"use strict"
    function r(e){return e&&e.__esModule?e:{"default":e}}function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function o(e,t){e[t]=function(n){var r=(0,c.getTargetContainer)(n),i=e.theme[t]||e.defaultTheme[t]
    return(0,s.autorun)(function(){var t=i(e.state,e)
    r.firstChild?r.replaceChild(t,r.firstChild):r.appendChild(t)}),r}}var a=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n]
    r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),s=n(1),u=n(0),c=n(3),l=n(2),h=r(l),d="public_repo",p=function(){function e(){var t=this,n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{}
    i(this,e),this.defaultTheme=h["default"],this.useTheme(h["default"]),Object.assign(this,{id:window.location.href,title:window.document.title,link:window.location.href,desc:"",labels:[],theme:h["default"],oauth:{},perPage:20,maxCommentHeight:250},n),this.useTheme(this.theme)
    var r={}
    try{var o=localStorage.getItem(u.LS_USER_KEY)
    this.accessToken&&o&&Object.assign(r,JSON.parse(o),{fromCache:!0})}catch(a){localStorage.removeItem(u.LS_USER_KEY)}this.state=(0,s.observable)({user:r,error:null,meta:{},comments:void 0,reactions:[],commentReactions:{},currentPage:1})
    var l=c.Query.parse()
    if(l.code){var d=this.oauth,p=d.client_id,f=d.client_secret,m=l.code
    delete l.code
    var v=c.Query.stringify(l),g=""+window.location.origin+window.location.pathname+v+window.location.hash
    history.replaceState({},"",g),Object.assign(this,{id:g,link:g},n),this.state.user.isLoggingIn=!0,c.http.post("https://gh-oauth.riteme.site",{code:m,client_id:p,client_secret:f},"").then(function(e){t.accessToken=e.access_token,t.update()})["catch"](function(e){t.state.user.isLoggingIn=!1,alert(e)})}else this.update()}return a(e,[{key:"accessToken",get:function(){return localStorage.getItem(u.LS_ACCESS_TOKEN_KEY)},set:function(e){localStorage.setItem(u.LS_ACCESS_TOKEN_KEY,e)}},{key:"loginLink",get:function(){var e="https://github.com/login/oauth/authorize",t=this.oauth.redirect_uri||window.location.href,n=Object.assign({scope:d,redirect_uri:t},this.oauth)
    return""+e+c.Query.stringify(n)}}]),a(e,[{key:"init",value:function(){var e=this
    return this.createIssue().then(function(){return e.loadComments()}).then(function(t){return e.state.error=null,t})}},{key:"useTheme",value:function(){var e=this,t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{}
    this.theme=t
    var n=Object.keys(this.theme)
    n.forEach(function(t){return o(e,t)})}},{key:"update",value:function(){var e=this
    return Promise.all([this.loadMeta(),this.loadUserInfo()]).then(function(){return Promise.all([e.loadComments().then(function(){return e.loadCommentReactions()}),e.loadReactions()])})["catch"](function(t){return e.state.error=t})}},{key:"markdown",value:function(e){return c.http.post("/markdown",{text:e,mode:"gfm"})}},{key:"createIssue",value:function(){var e=this,t=this.id,n=this.owner,r=this.repo,i=this.title,o=this.link,a=this.desc,s=this.labels
    return c.http.post("/repos/"+n+"/"+r+"/issues",{title:i,labels:s.concat(["gitment",t]),body:o+"\n\n"+a}).then(function(t){return e.state.meta=t,t})}},{key:"getIssue",value:function(){return this.state.meta.id?Promise.resolve(this.state.meta):this.loadMeta()}},{key:"post",value:function(e){var t=this
    return this.getIssue().then(function(t){return c.http.post(t.comments_url,{body:e},"")}).then(function(e){t.state.meta.comments++
    var n=Math.ceil(t.state.meta.comments/t.perPage)
    return t.state.currentPage===n&&t.state.comments.push(e),e})}},{key:"loadMeta",value:function(){var e=this,t=this.id,n=this.owner,r=this.repo
    return c.http.get("/repos/"+n+"/"+r+"/issues",{creator:n,labels:t}).then(function(t){return t.length?(e.state.meta=t[0],t[0]):Promise.reject(u.NOT_INITIALIZED_ERROR)})}},{key:"loadComments",value:function(){var e=this,t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:this.state.currentPage
    return this.getIssue().then(function(n){return c.http.get(n.comments_url,{page:t,per_page:e.perPage},"")}).then(function(t){return e.state.comments=t,t})}},{key:"loadUserInfo",value:function(){var e=this
    return this.accessToken?c.http.get("/user").then(function(t){return e.state.user=t,localStorage.setItem(u.LS_USER_KEY,JSON.stringify(t)),t}):(this.logout(),Promise.resolve({}))}},{key:"loadReactions",value:function(){var e=this
    return this.accessToken?this.getIssue().then(function(e){return e.reactions.total_count?c.http.get(e.reactions.url,{},""):[]}).then(function(t){return e.state.reactions=t,t}):(this.state.reactions=[],Promise.resolve([]))}},{key:"loadCommentReactions",value:function(){var e=this
    if(!this.accessToken)return this.state.commentReactions={},Promise.resolve([])
    var t=this.state.comments,n={}
    return Promise.all(t.map(function(t){if(!t.reactions.total_count)return[]
    var n=e.owner,r=e.repo
    return c.http.get("/repos/"+n+"/"+r+"/issues/comments/"+t.id+"/reactions",{})})).then(function(r){return t.forEach(function(e,t){n[e.id]=r[t]}),e.state.commentReactions=n,n})}},{key:"login",value:function(){window.location.href=this.loginLink}},{key:"logout",value:function(){localStorage.removeItem(u.LS_ACCESS_TOKEN_KEY),localStorage.removeItem(u.LS_USER_KEY),this.state.user={}}},{key:"goto",value:function(e){return this.state.currentPage=e,this.state.comments=void 0,this.loadComments(e)}},{key:"like",value:function(){var e=this
    if(!this.accessToken)return alert("请先登录"),Promise.reject()
    var t=this.owner,n=this.repo
    return c.http.post("/repos/"+t+"/"+n+"/issues/"+this.state.meta.number+"/reactions",{content:"heart"}).then(function(t){e.state.reactions.push(t),e.state.meta.reactions.heart++})}},{key:"unlike",value:function(){var e=this
    if(!this.accessToken)return Promise.reject()
    var t=this.state,n=t.user,r=t.reactions,i=r.findIndex(function(e){return e.user.login===n.login})
    return c.http["delete"]("/reactions/"+r[i].id).then(function(){r.splice(i,1),e.state.meta.reactions.heart--})}},{key:"likeAComment",value:function(e){var t=this
    if(!this.accessToken)return alert("请先登录"),Promise.reject()
    var n=this.owner,r=this.repo,i=this.state.comments.find(function(t){return t.id===e})
    return c.http.post("/repos/"+n+"/"+r+"/issues/comments/"+e+"/reactions",{content:"heart"}).then(function(n){t.state.commentReactions[e].push(n),i.reactions.heart++})}},{key:"unlikeAComment",value:function(e){if(!this.accessToken)return Promise.reject()
    var t=this.state.commentReactions[e],n=this.state.comments.find(function(t){return t.id===e}),r=this.state.user,i=t.findIndex(function(e){return e.user.login===r.login})
    return c.http["delete"]("/reactions/"+t[i].id).then(function(){t.splice(i,1),n.reactions.heart--})}}]),e}()
    e.exports=p},function(e,t,n){"use strict"
    Object.defineProperty(t,"__esModule",{value:!0})
    t.close='<svg class="gitment-close-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50"><path d="M37.304 11.282l1.414 1.414-26.022 26.02-1.414-1.413z"/><path d="M12.696 11.282l26.022 26.02-1.414 1.415-26.022-26.02z"/></svg>',t.github='<svg class="gitment-github-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50"><path d="M25 10c-8.3 0-15 6.7-15 15 0 6.6 4.3 12.2 10.3 14.2.8.1 1-.3 1-.7v-2.6c-4.2.9-5.1-2-5.1-2-.7-1.7-1.7-2.2-1.7-2.2-1.4-.9.1-.9.1-.9 1.5.1 2.3 1.5 2.3 1.5 1.3 2.3 3.5 1.6 4.4 1.2.1-1 .5-1.6 1-2-3.3-.4-6.8-1.7-6.8-7.4 0-1.6.6-3 1.5-4-.2-.4-.7-1.9.1-4 0 0 1.3-.4 4.1 1.5 1.2-.3 2.5-.5 3.8-.5 1.3 0 2.6.2 3.8.5 2.9-1.9 4.1-1.5 4.1-1.5.8 2.1.3 3.6.1 4 1 1 1.5 2.4 1.5 4 0 5.8-3.5 7-6.8 7.4.5.5 1 1.4 1 2.8v4.1c0 .4.3.9 1 .7 6-2 10.2-7.6 10.2-14.2C40 16.7 33.3 10 25 10z"/></svg>',t.heart='<svg class="gitment-heart-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50"><path d="M25 39.7l-.6-.5C11.5 28.7 8 25 8 19c0-5 4-9 9-9 4.1 0 6.4 2.3 8 4.1 1.6-1.8 3.9-4.1 8-4.1 5 0 9 4 9 9 0 6-3.5 9.7-16.4 20.2l-.6.5zM17 12c-3.9 0-7 3.1-7 7 0 5.1 3.2 8.5 15 18.1 11.8-9.6 15-13 15-18.1 0-3.9-3.1-7-7-7-3.5 0-5.4 2.1-6.9 3.8L25 17.1l-1.1-1.3C22.4 14.1 20.5 12 17 12z"/></svg>',t.spinner='<svg class="gitment-spinner-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50"><path d="M25 18c-.6 0-1-.4-1-1V9c0-.6.4-1 1-1s1 .4 1 1v8c0 .6-.4 1-1 1z"/><path opacity=".3" d="M25 42c-.6 0-1-.4-1-1v-8c0-.6.4-1 1-1s1 .4 1 1v8c0 .6-.4 1-1 1z"/><path opacity=".3" d="M29 19c-.2 0-.3 0-.5-.1-.4-.3-.6-.8-.3-1.3l4-6.9c.3-.4.8-.6 1.3-.3.4.3.6.8.3 1.3l-4 6.9c-.2.2-.5.4-.8.4z"/><path opacity=".3" d="M17 39.8c-.2 0-.3 0-.5-.1-.4-.3-.6-.8-.3-1.3l4-6.9c.3-.4.8-.6 1.3-.3.4.3.6.8.3 1.3l-4 6.9c-.2.2-.5.4-.8.4z"/><path opacity=".93" d="M21 19c-.3 0-.6-.2-.8-.5l-4-6.9c-.3-.4-.1-1 .3-1.3.4-.3 1-.1 1.3.3l4 6.9c.3.4.1 1-.3 1.3-.2.2-.3.2-.5.2z"/><path opacity=".3" d="M33 39.8c-.3 0-.6-.2-.8-.5l-4-6.9c-.3-.4-.1-1 .3-1.3.4-.3 1-.1 1.3.3l4 6.9c.3.4.1 1-.3 1.3-.2.1-.3.2-.5.2z"/><path opacity=".65" d="M17 26H9c-.6 0-1-.4-1-1s.4-1 1-1h8c.6 0 1 .4 1 1s-.4 1-1 1z"/><path opacity=".3" d="M41 26h-8c-.6 0-1-.4-1-1s.4-1 1-1h8c.6 0 1 .4 1 1s-.4 1-1 1z"/><path opacity=".86" d="M18.1 21.9c-.2 0-.3 0-.5-.1l-6.9-4c-.4-.3-.6-.8-.3-1.3.3-.4.8-.6 1.3-.3l6.9 4c.4.3.6.8.3 1.3-.2.3-.5.4-.8.4z"/><path opacity=".3" d="M38.9 33.9c-.2 0-.3 0-.5-.1l-6.9-4c-.4-.3-.6-.8-.3-1.3.3-.4.8-.6 1.3-.3l6.9 4c.4.3.6.8.3 1.3-.2.3-.5.4-.8.4z"/><path opacity=".44" d="M11.1 33.9c-.3 0-.6-.2-.8-.5-.3-.4-.1-1 .3-1.3l6.9-4c.4-.3 1-.1 1.3.3.3.4.1 1-.3 1.3l-6.9 4c-.1.2-.3.2-.5.2z"/><path opacity=".3" d="M31.9 21.9c-.3 0-.6-.2-.8-.5-.3-.4-.1-1 .3-1.3l6.9-4c.4-.3 1-.1 1.3.3.3.4.1 1-.3 1.3l-6.9 4c-.2.2-.3.2-.5.2z"/></svg>'}])
