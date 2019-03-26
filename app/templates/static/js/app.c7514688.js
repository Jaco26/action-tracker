(function(e){function t(t){for(var n,c,i=t[0],s=t[1],u=t[2],d=0,m=[];d<i.length;d++)c=i[d],a[c]&&m.push(a[c][0]),a[c]=0;for(n in s)Object.prototype.hasOwnProperty.call(s,n)&&(e[n]=s[n]);l&&l(t);while(m.length)m.shift()();return o.push.apply(o,u||[]),r()}function r(){for(var e,t=0;t<o.length;t++){for(var r=o[t],n=!0,i=1;i<r.length;i++){var s=r[i];0!==a[s]&&(n=!1)}n&&(o.splice(t--,1),e=c(c.s=r[0]))}return e}var n={},a={app:0},o=[];function c(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,c),r.l=!0,r.exports}c.m=e,c.c=n,c.d=function(e,t,r){c.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,t){if(1&t&&(e=c(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(c.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)c.d(r,n,function(t){return e[t]}.bind(null,n));return r},c.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(t,"a",t),t},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},c.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],s=i.push.bind(i);i.push=t,i=i.slice();for(var u=0;u<i.length;u++)t(i[u]);var l=s;o.push([0,"chunk-vendors"]),r()})({0:function(e,t,r){e.exports=r("56d7")},"034f":function(e,t,r){"use strict";var n=r("64a9"),a=r.n(n);a.a},"56d7":function(e,t,r){"use strict";r.r(t);r("cadf"),r("551c"),r("f751"),r("097d");var n=r("2b0e"),a=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("the-navbar"),r("b-container",{attrs:{fluid:"",id:"app"}},[r("b-row",{attrs:{"no-gutters":""}},[r("b-col",[r("router-view")],1)],1)],1)],1)},o=[],c=r("cebc"),i=r("2f62"),s=r("bc3a"),u=r.n(s),l=u.a.create({baseURL:"/api/v1"}),d=function(){var e=this,t=e.$createElement,r=e._self._c||t;return e.isAuthenticated()?r("b-navbar",{attrs:{sticky:"",type:"dark",variant:"dark"}},[r("b-navbar-nav",{staticStyle:{width:"100%"}},[r("b-row",{staticStyle:{width:"100%"},attrs:{"justify-content-between":""}},[r("b-col",{staticClass:"d-flex justify-content-start"},[r("b-nav-item",{attrs:{to:"/"}},[e._v("Home")]),r("b-nav-item",{attrs:{to:"/reports"}},[e._v("Reports")])],1),r("b-col",{staticClass:"d-flex justify-content-end"},[r("b-nav-item-dropdown",{attrs:{text:e.username}},[r("b-dropdown-item",{on:{click:e.logout}},[e._v("Logout")])],1)],1)],1)],1)],1):e._e()},m=[],p={computed:Object(c["a"])({},Object(i["c"])("auth",["isAuthenticated"]),Object(i["d"])("auth",["username"])),methods:Object(c["a"])({},Object(i["b"])("auth",["logout"]))},g=p,f=r("2877"),h=Object(f["a"])(g,d,m,!1,null,null,null),b=h.exports,v={components:{theNavbar:b},computed:Object(c["a"])({},Object(i["c"])("auth",["isAuthenticated"]),Object(i["d"])("auth",["accessToken"]),Object(i["d"])("myActions",["actions","actionsLoading","categories","categoriesLoading"])),methods:Object(c["a"])({},Object(i["b"])("myActions",["getAllCategories","getAllActions"]),{shouldFetch:function(e){return this[e]&&!this[e].length&&!this["".concat(e,"Loading")]}}),watch:{accessToken:{immediate:!0,handler:function(e){e&&(l.defaults.headers.common["Authorization"]="Bearer ".concat(e),this.shouldFetch("actions")&&this.getAllActions(),this.shouldFetch("categories")&&this.getAllCategories())}}}},y=v,_=(r("034f"),Object(f["a"])(y,a,o,!1,null,null,null)),w=_.exports,A=r("8c4f"),E=r("75fc"),O=(r("7f7f"),r("5176")),T=r.n(O),D=r("f499"),S=r.n(D),j=(r("6762"),r("2fdb"),r("28a5"),r("ac6a"),r("a4bb")),k=r.n(j),x=r("7618"),C=r("a745"),L=r.n(C),N=r("768b"),R=r("0a0d"),I=r.n(R),P=(r("a481"),r("795b")),$=r.n(P),F=(r("5df3"),r("96cf"),r("3b8d")),G="auth",V={clearFields:function(e){var t=function(t,r){return e(t,r,{root:!0})};t("myActions/CLEAR_FIELDS",{actions:[],categories:[],errors:[]}),t("newAction/CLEAR_FIELDS",{currentDate:"",description:"",overrideTime:"",selectedCategoryId:null,errors:[]}),t("auth/CLEAR_FIELDS",{accessToken:"",refreshToken:"",username:"",errors:[]})}};function z(e){var t=localStorage.getItem(G);return t&&(t=JSON.parse(t),k()(t).forEach(function(r){void 0!==e[r]&&(e[r]=t[r])})),e}function B(){return{accessToken:"",refreshToken:"",username:"",errors:[]}}var U={namespaced:!0,state:z(B()),mutations:{handleLoginResponse:function(e,t){e.errors=t.errors,e.accessToken=t.data.access_token,e.refreshToken=t.data.refresh_token,e.username=t.data.username}},actions:{register:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(t,r){var n,a;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return t.commit,n=r.username,a=r.password,e.prev=2,e.next=5,l.post("/auth/register",{username:n,password:a});case 5:e.next=10;break;case 7:return e.prev=7,e.t0=e["catch"](2),e.abrupt("return",e.t0);case 10:case"end":return e.stop()}},e,null,[[2,7]])}));function t(t,r){return e.apply(this,arguments)}return t}(),login:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(t,r){var n,a,o,c,i;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return n=t.commit,a=t.state,o=r.username,c=r.password,e.prev=2,e.next=5,l({url:"/auth/login",method:"POST",data:{username:o,password:c}});case 5:i=e.sent,console.log(i),n("handleLoginResponse",i.data),n("SAVE_TO_STORAGE",{STORAGE_KEY:G,keys:["accessToken","refreshToken","username"]}),bt.push({name:"home"}),e.next=15;break;case 12:e.prev=12,e.t0=e["catch"](2),n("SET_STATE_VAL",["errors",[].concat(Object(E["a"])(a.errors),[e.t0.message])]);case 15:case"end":return e.stop()}},e,null,[[2,12]])}));function t(t,r){return e.apply(this,arguments)}return t}(),logout:function(e){var t=e.commit,r=e.state;$.a.all([l({url:"/auth/logout-access",method:"POST"}),l({url:"/auth/logout-refresh",method:"POST",headers:{Authorization:"Bearer ".concat(r.refreshToken)}})]).then(function(e){}).catch(function(e){console.error("ERROR LOGIN OUT",e)}).finally(function(){V.clearFields(t),t("SAVE_TO_STORAGE",{STORAGE_KEY:G,keys:k()(r)}),bt.push({name:"login"})})},refresh:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(t){var r,n,a;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return r=t.commit,n=t.state,e.prev=1,e.next=4,l({url:"/auth/refresh",method:"POST",headers:{Authorization:"Bearer ".concat(n.refreshToken)}});case 4:a=e.sent,r("SET_STATE_VAL",["accessToken",a.data.data.access_token]),e.next=11;break;case 8:e.prev=8,e.t0=e["catch"](1),r("SET_STATE_VAL",["errors",[].concat(Object(E["a"])(n.errors),[e.t0.message])]);case 11:case"end":return e.stop()}},e,null,[[1,8]])}));function t(t){return e.apply(this,arguments)}return t}()},getters:{parseJWT:function(e){if(e.accessToken){var t=e.accessToken.split(".")[1],r=t.replace(/-/g,"+").replace(/_/g,"/");return JSON.parse(window.atob(r))}return null},isAuthenticated:function(e,t){return t.parseJWT?function(){var e=I()().valueOf()/1e3,r=t.parseJWT.exp;return r>e}:function(){return!1}}}},M={state:{categories:[],categoriesLoading:!1,actions:[],actionsLoading:!1,errors:[],dateStr1:"",dateStr2:""},actions:{getAllCategories:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(t,r){var n,a,o;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return n=t.commit,a=t.state,e.prev=1,n("LOADING",["categories",!0]),e.next=5,l.get("/action-category/");case 5:o=e.sent,n("SET_STATE_VAL",["categories",o.data.data.action_categories]),e.next=12;break;case 9:e.prev=9,e.t0=e["catch"](1),n("SET_STATE_VAL",["errors",[].concat(Object(E["a"])(a.errors),[e.t0.message])]);case 12:return e.prev=12,n("LOADING",["categories",!1]),e.finish(12);case 15:case"end":return e.stop()}},e,null,[[1,9,12,15]])}));function t(t,r){return e.apply(this,arguments)}return t}(),getAllActions:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(t){var r,n;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return r=t.commit,t.state,e.prev=1,r("LOADING",["actions",!0]),e.next=5,l.get("/action-taken/");case 5:n=e.sent,r("SET_STATE_VAL",["actions",n.data.data.actions.map(function(e){return e.displayDate=new Date(e.ts).toLocaleString(),e})]),e.next=12;break;case 9:e.prev=9,e.t0=e["catch"](1),r("ERROR",e.t0.message);case 12:return e.prev=12,r("LOADING",["actions",!1]),e.finish(12);case 15:case"end":return e.stop()}},e,null,[[1,9,12,15]])}));function t(t){return e.apply(this,arguments)}return t}(),getAllActionsByDate:function(e,t){e.commit},getAllActionsByCategory:function(e,t){e.commit},deleteAction:function(e,t){e.commit},editAction:function(e,t){e.commit}},getters:{groupActionsByCategory:function(e){return e.actions.length?e.actions.reduce(function(e,t){e[t.category_name]||(e[t.category_name]=[]);var r=t.ts,n=t.displayDate,a=t.description,o=t.id;return e[t.category_name].push({ts:r,displayDate:n,description:a,id:o}),e},{}):null},filterActionsByDate:function(e,t){if(e.actions&&e.dateStr1){var r=e.dateStr1,n=e.dateStr2,a=new Date(r),o=6e4*a.getTimezoneOffset(),c=864e5,i=new Date(a.getTime()+o),s=n?new Date(new Date(n).getTime()+c+o):new Date(i.getTime()+c+o);return e.actions.reduce(function(e,t){var r=new Date(new Date(t.ts)+o);return console.log(r-i),r>i&&r<s&&e.push(t),e},[])}return null}}},J={state:{selectedCategoryId:null,description:"",currentDate:"",overrideTime:"",errors:[],submissionLoading:!1},actions:{addNewAction:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(t){var r,n,a,o,c;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return r=t.commit,n=t.dispatch,a=t.state,e.prev=1,r("LOADING",["submission",!0]),o=a.overrideTime?new Date(a.currentDate+" "+a.overrideTime).toISOString():(new Date).toISOString(),c={ts:o,description:a.description,category_id:a.selectedCategoryId},e.next=7,l.post("/action-taken/",{action:c});case 7:e.sent,n("myActions/getAllActions",null,{root:!0}),r("CLEAR_FIELDS",{selectedCategoryId:null,description:"",overrideTime:""}),e.next=15;break;case 12:e.prev=12,e.t0=e["catch"](1),r("ERROR",e.t0);case 15:return e.prev=15,r("LOADING",["submission",!1]),e.finish(15);case 18:case"end":return e.stop()}},e,null,[[1,12,15,18]])}));function t(t){return e.apply(this,arguments)}return t}()}},Y={state:{categoryName:"",categoryEditId:"",categoryEditName:"",categoryDeleteId:"",categoryDeleteName:"",confirmCategoryDelete:!1,categoryNameLoading:!1,errors:[]},actions:{addNewCategory:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(t){var r,n,a;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:if(r=t.commit,n=t.state,!n.categoryName){e.next=17;break}return e.prev=2,r("LOADING",["categoryName",!0]),e.next=6,l.post("/action-category/",{category_name:n.categoryName.trim()});case 6:a=e.sent,r("myActions/SET_STATE_VAL",["categories",a.data.data.action_categories],{root:!0}),e.next=13;break;case 10:e.prev=10,e.t0=e["catch"](2),r("SET_STATE_VAL",["errors",[].concat(Object(E["a"])(n.errors),[e.t0.message])]);case 13:return e.prev=13,r("LOADING",["categoryName",!1]),r("CLEAR_FIELDS",["categoryName"]),e.finish(13);case 17:case"end":return e.stop()}},e,null,[[2,10,13,17]])}));function t(t){return e.apply(this,arguments)}return t}(),submitEdit:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(t){var r,n,a;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:if(r=t.commit,n=t.dispatch,a=t.state,!a.categoryEditName){e.next=15;break}return e.prev=2,e.next=5,l.put("/action-category/",{new_category_name:a.categoryEditName,category_id:a.categoryEditId});case 5:n("myActions/getAllCategories",null,{root:!0}),n("myActions/getAllActions",null,{root:!0}),e.next=12;break;case 9:e.prev=9,e.t0=e["catch"](2),r("SET_STATE_VAL",["errors",[].concat(Object(E["a"])(a.errors),[e.t0.message])]);case 12:return e.prev=12,r("CLEAR_FIELDS",["categoryEditId","categoryEditName"]),e.finish(12);case 15:case"end":return e.stop()}},e,null,[[2,9,12,15]])}));function t(t){return e.apply(this,arguments)}return t}(),deleteCategory:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(t){var r,n,a;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return r=t.commit,n=t.dispatch,a=t.state,e.prev=1,e.next=4,l.delete("/action-category/".concat(a.categoryDeleteId));case 4:e.sent,n("myActions/getAllCategories",null,{root:!0}),n("myActions/getAllActions",null,{root:!0}),e.next=13;break;case 9:e.prev=9,e.t0=e["catch"](1),console.log(e.t0),r("SET_STATE_VAL",["errors",[].concat(Object(E["a"])(a.errors),[e.t0.message])]);case 13:case"end":return e.stop()}},e,null,[[1,9]])}));function t(t){return e.apply(this,arguments)}return t}()}};n["a"].use(i["a"]);var q={LOADING:function(e,t){var r=Object(N["a"])(t,2),n=r[0],a=r[1];void 0!==e["".concat(n,"Loading")]?e["".concat(n,"Loading")]=a:console.error("state.".concat(n,"Loading does not exist."))},MAP_TO_STATE:function(e,t){var r=t.payload,n=t.nested,a=void 0!==n&&n,o=function(e){return e&&!L()(e)&&"object"===Object(x["a"])(e)};(function e(t,r){var n=k()(t);n.forEach(function(n){o(t[n])&&a&&void 0!==r[n]?e(t[n],r[n]):void 0!==r[n]&&(t[n]=r[n])})})(e,r)},SET_STATE_VAL:function(e,t){var r=Object(N["a"])(t,4),n=r[0],a=r[1],o=r[2],c=void 0!==o&&o,i=r[3],s=void 0!==i&&i;c?q.MAP_TO_STATE(e[n],{payload:a,nested:s}):e[n]=a},SET_STATE:function(e,t){var r=t.key,n=t.data,a=e;r.split(".").reduce(function(e,t,r,o){return r===o.length-1?a[t]=n:a=a[t],a},a)},ERROR:function(e,t){L()(e.errors)?e.errors.push(t):console.error("State does not have an Array property named `errors`")},SAVE_TO_STORAGE:function(e,t){var r=t.STORAGE_KEY,n=t.keys,a=k()(e).reduce(function(t,r){return n.includes(r)&&(t[r]=e[r]),t},{});localStorage.setItem(r,S()(a))},CLEAR_FIELDS:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];console.log(t),t&&!L()(t)&&"object"===Object(x["a"])(t)?k()(t).forEach(function(r){e[r]=t[r]}):t.forEach(function(t){e[t]=""})}};function K(e,t){return t.mutations=Object(c["a"])({},t.mutations,q),T()(e,t)}var W=new i["a"].Store(H({strict:!1,modules:{auth:U,myActions:M,newAction:J,actionCategory:Y}}));function H(e){var t=K({namespaced:!0,state:{},mutations:{},actions:{},getters:{},modules:{}},e);return t.modules=Q(t.modules),t}function Q(e){return k()(e).reduce(function(t,r){return t[r]=H(e[r]),t},{})}function X(e,t){var r=W.state;return[].concat(Object(E["a"])(e.split("/")),[t]).reduce(function(e,t){return r=r[t],r},r)}function Z(e,t){return t.reduce(function(t,r){return t[r]={get:function(){return X(e,r)},set:function(t){return W.commit(e+"/SET_STATE",{key:r,data:t})}},t},{})}var ee=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("b-row",[r("b-col",[r("b-card",{attrs:{"no-body":""}},[r("b-tabs",{attrs:{card:"",pills:""}},[r("b-tab",{attrs:{title:"New Action",active:""}},[r("the-new-action-form")],1),r("b-tab",{attrs:{title:"Action Categories"}},[r("b-row",[r("b-col",[r("the-new-category-form")],1)],1),r("b-row",{staticClass:"my-4"},[r("b-col",[r("the-categories-list")],1)],1)],1)],1)],1)],1)],1)},te=[],re=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("b-card",[r("b-form",{on:{submit:function(t){return t.preventDefault(),e.addNewCategory(t)}}},[r("b-form-group",{attrs:{label:"New Action Category",description:"Enter a name you can use to categorize your actions"}},[r("b-form-input",{attrs:{type:"text",placeholder:"Enter a category name"},model:{value:e.categoryName,callback:function(t){e.categoryName=t},expression:"categoryName"}})],1),r("b-row",[r("b-col",[r("b-button",{attrs:{block:"",type:"submit"}},[e._v("Submit")])],1)],1)],1)],1)},ne=[],ae={computed:Object(c["a"])({},Z("actionCategory",["categoryName"])),methods:Object(c["a"])({},Object(i["b"])("actionCategory",["addNewCategory"]))},oe=ae,ce=Object(f["a"])(oe,re,ne,!1,null,null,null),ie=ce.exports,se=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("the-delete-category-modal"),r("b-card",[r("h3",[e._v("My Categories")]),r("table",{staticClass:"table table-sm table-hover"},[r("thead",[r("th",[e._v("Category Name")]),r("th")]),r("tbody",[e._l(e.categories,function(t){return[e.categoryEditId===t.id?r("tr",{key:t.id},[r("td",[r("b-form",{on:{submit:function(t){return t.preventDefault(),e.submitEdit(t)}}},[r("b-form-input",{attrs:{type:"text",placeholder:e.categoryNameToEdit},model:{value:e.categoryEditName,callback:function(t){e.categoryEditName="string"===typeof t?t.trim():t},expression:"categoryEditName"}})],1)],1),r("td",{staticClass:"d-flex justify-content-end"},[r("b-button",{attrs:{size:"sm",variant:"light"},on:{click:e.cancelEdit}},[e._v("Cancel")]),r("b-button",{attrs:{size:"sm",variant:"outline-primary"},on:{click:e.submitEdit}},[e._v("Save")])],1)]):r("tr",{key:t.id+"edit"},[r("td",[e._v(e._s(t.category_name))]),r("td",{staticClass:"d-flex justify-content-end"},[r("b-button",{attrs:{size:"sm",variant:"outline-info"},on:{click:function(r){return e.doEdit(t.id)}}},[e._v("Edit")]),r("b-button",{attrs:{size:"sm",variant:"outline-danger"},on:{click:function(r){return e.doDelete(t.id)}}},[e._v("Delete")])],1)])]})],2)])])],1)},ue=[],le=(r("7514"),function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("b-modal",{attrs:{"no-close-on-backdrop":"","hide-header-close":""},on:{ok:e.completeDelete,cancel:e.cancelDelete},model:{value:e.confirmCategoryDelete,callback:function(t){e.confirmCategoryDelete=t},expression:"confirmCategoryDelete"}},[r("b-form",{on:{submit:function(t){return t.stopPropagation(),t.preventDefault(),e.completeDelete(t)}}},[r("p",[e._v(' \n      If you delete the category "'),r("strong",[e._v(e._s(e.categoryDeleteName))]),e._v("\"\n      all actions you've saved under this category will be erased as well!\n    ")]),r("p",[e._v("\n      Type "),r("strong",[e._v('"DELETE '+e._s(e.categoryDeleteName.toUpperCase())+'"')]),e._v(" and hit "),r("strong",[e._v("Ok")]),e._v(" to continue.\n    ")]),r("b-form-input",{attrs:{type:"text",placeholder:"DELETE "+e.categoryDeleteName.toUpperCase()},model:{value:e.matchToDelete,callback:function(t){e.matchToDelete=t},expression:"matchToDelete"}})],1)],1)}),de=[],me={data:function(){return{matchToDelete:""}},computed:Object(c["a"])({},Z("actionCategory",["confirmCategoryDelete","categoryDeleteId","categoryDeleteName"])),methods:{completeDelete:function(){this.matchToDelete==="DELETE ".concat(this.categoryDeleteName.toUpperCase())&&this.$store.dispatch("actionCategory/deleteCategory"),this.categoryDeleteId="",this.categoryDeleteName="",this.matchToDelete="",this.confirmCategoryDelete=!1},cancelDelete:function(){this.categoryDeleteId="",this.categoryDeleteName="",this.matchToDelete=""}}},pe=me,ge=Object(f["a"])(pe,le,de,!1,null,null,null),fe=ge.exports,he={components:{theDeleteCategoryModal:fe},computed:Object(c["a"])({},Object(i["d"])("myActions",["categories"]),Z("actionCategory",["categoryEditId","categoryEditName","categoryDeleteId","categoryDeleteName","confirmCategoryDelete"]),{categoryNameToEdit:function(){var e=this,t=this.categories.find(function(t){return t.id===e.categoryEditId});return t?t.category_name:null}}),methods:Object(c["a"])({},Object(i["b"])("actionCategory",["deleteCategory","submitEdit"]),{doEdit:function(e){this.categoryEditId=e,this.categoryEditName=this.categoryNameToEdit},cancelEdit:function(){this.categoryEditId="",this.categoryEditName=""},doDelete:function(e){this.confirmCategoryDelete=!0,this.categoryDeleteId=e,this.categoryDeleteName=this.categories.find(function(t){return t.id===e}).category_name}})},be=he,ve=Object(f["a"])(be,se,ue,!1,null,null,null),ye=ve.exports,_e=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("b-card",[r("b-form",{on:{submit:function(t){return t.preventDefault(),e.onSubmit(t)}}},[r("b-form-group",{attrs:{label:"Select a category",description:"Select the category under which you want to log this action"}},[r("b-form-select",{attrs:{options:e.selectableCategories},model:{value:e.selectedCategoryId,callback:function(t){e.selectedCategoryId=t},expression:"selectedCategoryId"}})],1),r("b-form-group",{attrs:{label:"Add a note"}},[r("b-form-textarea",{attrs:{rows:"3","max-rows":"3","no-resize":""},model:{value:e.description,callback:function(t){e.description="string"===typeof t?t.trim():t},expression:"description"}})],1),r("b-form-group",{attrs:{label:"Override time",description:"This action will be stored with the time of submission by default. Choose a time to override the default"}},[r("b-form-row",[r("b-col",[r("b-form-input",{attrs:{type:"date",value:e.currentDate},on:{input:function(t){e.currentDate=t}}})],1),r("b-col",[r("b-form-input",{attrs:{type:"time"},model:{value:e.overrideTime,callback:function(t){e.overrideTime=t},expression:"overrideTime"}})],1)],1)],1),r("b-form-group",[r("b-form-row",[r("b-col",{staticClass:"d-flex justify-content-center"},[r("b-button",{attrs:{block:"",variant:"primary",type:"submit",disabled:e.submissionLoading}},[e.submissionLoading?r("b-spinner",{attrs:{label:"Submitting..."}}):r("span",[e._v("Submit")])],1)],1)],1)],1)],1)],1)},we=[],Ae={mounted:function(){var e=new Date,t=e.getUTCFullYear(),r=e.getUTCMonth()+1,n=e.getUTCDate(),a=r<10?"0".concat(r):r,o=n<10?"0".concat(n):n;this.currentDate="".concat(t,"-").concat(a,"-").concat(o)},computed:Object(c["a"])({},Z("newAction",["selectedCategoryId","description","currentDate","overrideTime"]),Object(i["d"])("newAction",["submissionLoading"]),{selectableCategories:function(){var e=this.$store.state.myActions.categories.map(function(e){return{value:e.id,text:e.category_name}});return[{value:null,text:"Please select an option"}].concat(Object(E["a"])(e))}}),methods:Object(c["a"])({},Object(i["b"])("newAction",["addNewAction"]),{onSubmit:function(){this.selectedCategoryId?this.addNewAction():alert("You haven't selected this actions category")}})},Ee=Ae,Oe=Object(f["a"])(Ee,_e,we,!1,null,null,null),Te=Oe.exports,De={components:{theNewCategoryForm:ie,theCategoriesList:ye,theNewActionForm:Te}},Se=De,je=Object(f["a"])(Se,ee,te,!1,null,null,null),ke=je.exports,xe=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"auth"},[e.showLogin?r("section",[r("the-login-form"),r("b-button",{on:{click:function(t){e.showLogin=!1}}},[e._v("create account")])],1):r("section",[r("the-registration-form"),r("b-button",{on:{click:function(t){e.showLogin=!0}}},[e._v("go to login")])],1)])},Ce=[],Le=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"login"},[r("input",{directives:[{name:"model",rawName:"v-model",value:e.username,expression:"username"}],attrs:{type:"text",placeholder:"Username"},domProps:{value:e.username},on:{input:function(t){t.target.composing||(e.username=t.target.value)}}}),r("input",{directives:[{name:"model",rawName:"v-model",value:e.password,expression:"password"}],attrs:{type:"password",placeholder:"Password"},domProps:{value:e.password},on:{input:function(t){t.target.composing||(e.password=t.target.value)}}}),r("button",{on:{click:e.onLogin}},[e._v("Login")])])},Ne=[],Re={data:function(){return{username:"",password:""}},methods:Object(c["a"])({},Object(i["b"])("auth",["login"]),{onLogin:function(){this.login({username:this.username,password:this.password}),this.username="",this.password=""}})},Ie=Re,Pe=Object(f["a"])(Ie,Le,Ne,!1,null,null,null),$e=Pe.exports,Fe=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"register"},[r("input",{directives:[{name:"model",rawName:"v-model",value:e.username,expression:"username"}],attrs:{type:"text",placeholder:"Username"},domProps:{value:e.username},on:{input:function(t){t.target.composing||(e.username=t.target.value)}}}),r("input",{directives:[{name:"model",rawName:"v-model",value:e.password,expression:"password"}],attrs:{type:"password",placeholder:"Password"},domProps:{value:e.password},on:{input:function(t){t.target.composing||(e.password=t.target.value)}}}),r("button",{on:{click:e.onRegister}},[e._v("Register")])])},Ge=[],Ve={data:function(){return{username:"",password:""}},methods:Object(c["a"])({},Object(i["b"])("auth",["register"]),{onRegister:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(){return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,this.register({username:this.username,password:this.password});case 3:this.username="",this.password="",this.$router.push({name:"login"}),e.next=11;break;case 8:e.prev=8,e.t0=e["catch"](0),console.log(e.t0);case 11:case"end":return e.stop()}},e,this,[[0,8]])}));function t(){return e.apply(this,arguments)}return t}()})},ze=Ve,Be=Object(f["a"])(ze,Fe,Ge,!1,null,null,null),Ue=Be.exports,Me={components:{theLoginForm:$e,theRegistrationForm:Ue},data:function(){return{showLogin:!0}}},Je=Me,Ye=Object(f["a"])(Je,xe,Ce,!1,null,null,null),qe=Ye.exports,Ke=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("the-actions-list")],1)},We=[],He=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("b-card",[r("b-form-input",{attrs:{type:"date"},model:{value:e.dateStr1,callback:function(t){e.dateStr1=t},expression:"dateStr1"}}),r("b-form-input",{attrs:{type:"date"},model:{value:e.dateStr2,callback:function(t){e.dateStr2=t},expression:"dateStr2"}}),r("pre",[e._v("    "+e._s(e.filterableActions)+"\n  ")])],1)},Qe=[],Xe={computed:Object(c["a"])({},Z("myActions",["dateStr1","dateStr2"]),Object(i["d"])("myActions",["actions"]),Object(i["c"])("myActions",["groupActionsByCategory","filterActionsByDate"]),{filterableActions:function(){return this.dateStr1?this.filterActionsByDate:this.actions}})},Ze=Xe,et=Object(f["a"])(Ze,He,Qe,!1,null,null,null),tt=et.exports,rt={components:{theActionsList:tt}},nt=rt,at=Object(f["a"])(nt,Ke,We,!1,null,null,null),ot=at.exports,ct=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[e._v("\n  Access Denied\n  "),r("router-link",{attrs:{to:{name:"login"}}},[e._v("Login")])],1)},it=[],st={},ut=Object(f["a"])(st,ct,it,!1,null,null,null),lt=ut.exports,dt=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[e._v("\n  Oops! There's nothing here.\n  "),r("router-link",{attrs:{to:{name:"home"}}},[e._v("take me home")])],1)},mt=[],pt={},gt=Object(f["a"])(pt,dt,mt,!1,null,null,null),ft=gt.exports;n["a"].use(A["a"]);var ht=new A["a"]({mode:"history",base:"/",routes:[{path:"/",name:"home",meta:{requiresAuth:!0},component:ke},{path:"/login",name:"login",component:qe},{path:"/reports",name:"reports",component:ot,meta:{requiresAuth:!0}},{path:"/access-denied",name:"access-denied",component:lt},{path:"*",component:ft}]});ht.beforeEach(function(e,t,r){e.matched.some(function(e){return e.meta.requiresAuth})?W.state.auth.accessToken&&W.getters["auth/isAuthenticated"]()?r():W.dispatch("auth/logout"):r()});var bt=ht,vt=r("9f7b"),yt=r.n(vt);r("f9e3"),r("2dd8");n["a"].use(yt.a),n["a"].config.productionTip=!1,new n["a"]({router:bt,store:W,render:function(e){return e(w)}}).$mount("#app")},"64a9":function(e,t,r){}});
//# sourceMappingURL=app.c7514688.js.map