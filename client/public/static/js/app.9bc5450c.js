!function(e){function t(t){for(var r,a,i=t[0],u=t[1],l=t[2],c=0,m=[];c<i.length;c++)a=i[c],o[a]&&m.push(o[a][0]),o[a]=0;for(r in u)Object.prototype.hasOwnProperty.call(u,r)&&(e[r]=u[r]);for(d&&d(t);m.length;)m.shift()();return s.push.apply(s,l||[]),n()}function n(){for(var e,t=0;t<s.length;t++){for(var n=s[t],r=!0,a=1;a<n.length;a++){var u=n[a];0!==o[u]&&(r=!1)}r&&(s.splice(t--,1),e=i(i.s=n[0]))}return e}var r={},a={1:0},o={1:0},s=[];function i(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,i),n.l=!0,n.exports}i.e=function(e){var t=[];a[e]?t.push(a[e]):0!==a[e]&&{3:1,4:1,5:1,6:1}[e]&&t.push(a[e]=new Promise(function(t,n){for(var r="static/css/"+e+".styles."+{3:"cf084f60",4:"a9f491ac",5:"34e19fa1",6:"ce3262d4",7:"5af1e243",8:"c61f7897"}[e]+".css",a=i.p+r,o=document.getElementsByTagName("link"),s=0;s<o.length;s++){var u=(c=o[s]).getAttribute("data-href")||c.getAttribute("href");if("stylesheet"===c.rel&&(u===r||u===a))return t()}var l=document.getElementsByTagName("style");for(s=0;s<l.length;s++){var c;if((u=(c=l[s]).getAttribute("data-href"))===r||u===a)return t()}var d=document.createElement("link");d.rel="stylesheet",d.type="text/css",d.onload=t,d.onerror=function(t){var r=t&&t.target&&t.target.src||a,o=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");o.request=r,n(o)},d.href=a,document.getElementsByTagName("head")[0].appendChild(d)}).then(function(){a[e]=0}));var n=o[e];if(0!==n)if(n)t.push(n[2]);else{var r=new Promise(function(t,r){n=o[e]=[t,r]});t.push(n[2]=r);var s,u=document.getElementsByTagName("head")[0],l=document.createElement("script");l.charset="utf-8",l.timeout=120,i.nc&&l.setAttribute("nonce",i.nc),l.src=function(e){return i.p+"static/js/"+({}[e]||e)+"."+{3:"cf084f60",4:"a9f491ac",5:"34e19fa1",6:"ce3262d4",7:"5af1e243",8:"c61f7897"}[e]+".js"}(e),s=function(t){l.onerror=l.onload=null,clearTimeout(c);var n=o[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src,s=new Error("Loading chunk "+e+" failed.\n("+r+": "+a+")");s.type=r,s.request=a,n[1](s)}o[e]=void 0}};var c=setTimeout(function(){s({type:"timeout",target:l})},12e4);l.onerror=l.onload=s,u.appendChild(l)}return Promise.all(t)},i.m=e,i.c=r,i.d=function(e,t,n){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},i.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(i.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)i.d(n,r,function(t){return e[t]}.bind(null,r));return n},i.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/",i.oe=function(e){throw console.error(e),e};var u=window.webpackJsonp=window.webpackJsonp||[],l=u.push.bind(u);u.push=t,u=u.slice();for(var c=0;c<u.length;c++)t(u[c]);var d=l;s.push([131,2,0]),n()}({123:function(e,t,n){},131:function(e,t,n){"use strict";n.r(t);n(73),n(83),n(96);var r=n(1),a=(n(97),n(98),{name:"Alert",props:{dismissible:{type:Boolean,required:!1,default:!0},icon:{type:[String,Boolean,Array],required:!1,default:!0},type:{type:String,required:!1,default:"info",validator:function(e){return["info","success","warning","danger"].includes(e)}}},computed:{className:function(){return[{"alert-dismissible":this.dismissible},"alert-".concat(this.type)]},iconName:function(){return!0===this.icon?{info:"info",success:"check",warning:"exclamation-triangle",danger:"ban"}[this.type]:this.type}}}),o=n(4),s=Object(o.a)(a,function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"alert",class:e.className},[e.dismissible?n("button",{staticClass:"close",attrs:{type:"button","data-dismiss":"alert"},on:{click:function(t){e.$emit("close")}}},[e._v("\n    ×\n  ")]):e._e(),e._v(" "),n("h5",[e.icon?n("FaIcon",{staticClass:"mr-1",attrs:{icon:e.iconName,"fixed-width":""}}):e._e(),e._v(" "),e._t("title")],2),e._v(" "),e._t("text")],2)},[],!1,null,null,null);s.options.__file="Alert.vue";var i={name:"TheNotification",components:{Alert:s.exports}},u=Object(o.a)(i,function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("VueNotification",{attrs:{position:"top right",width:"400"},scopedSlots:e._u([{key:"body",fn:function(t){var r=t.item,a=r.title;void 0===a&&(a="");var o=r.type;void 0===o&&(o="info");var s=r.text;void 0===s&&(s="");var i=t.close;return[n("Alert",{attrs:{type:o},on:{close:i}},[n("template",{slot:"title"},[e._v("\n        "+e._s(a||o.charAt(0).toUpperCase()+o.slice(1))+"\n      ")]),e._v(" "),n("span",{attrs:{slot:"text"},domProps:{innerHTML:e._s(s)},slot:"text"})],2)]}}])})},[],!1,null,null,null);u.options.__file="TheNotification.vue";var l={name:"App",components:{TheNotification:u.exports}},c=Object(o.a)(l,function(){var e=this.$createElement,t=this._self._c||e;return t("div",[t("RouterView"),this._v(" "),t("TheNotification")],1)},[],!1,null,null,null);c.options.__file="App.vue";var d=c.exports,m=n(40),f=[{path:"/",name:"home",redirect:{name:"dashboard"}},{path:"/login",name:"login",component:function(){return Promise.all([n.e(0),n.e(4)]).then(n.bind(null,159))},meta:{requiresAuth:!1}},{path:"/register",name:"register",component:function(){return Promise.all([n.e(0),n.e(5)]).then(n.bind(null,157))},meta:{requiresAuth:!1}},{path:"/dashboard",component:function(){return n.e(3).then(n.bind(null,154))},meta:{requiresAuth:!0,linkText:"Dashboard"},children:[{path:"",name:"dashboard",component:function(){return n.e(6).then(n.bind(null,155))},meta:{title:"Dashboard",linkText:"Home"}},{path:"modules",name:"dashboard.modules",component:function(){return n.e(8).then(n.bind(null,158))},meta:{title:"Modules",linkText:"Modules"}}]},{path:"*",name:"NotFound",component:function(){return n.e(7).then(n.bind(null,156))},meta:{requiresAuth:!1}}],p=(n(102),n(29)),h=n(42),g=(n(43),n(10)),_=n(11),v=n.n(_),b=document.head.querySelector('meta[name="csrf_token"]');v.a.defaults.headers.common["X-Requested-With"]="XMLHttpRequest",v.a.defaults.headers.common["X-CSRFToken"]=b.content,v.a.defaults.xsrfCookieName="csrftoken",v.a.defaults.xsrfHeaderName="X-CSRFToken",v.a.interceptors.response.use(function(e){return e},function(e){var t=e.response;return e.notify={type:"danger",title:"Error",text:"[".concat(t.status," ").concat(t.statusText,"] ").concat(t.data.msg)},Promise.reject(e)});var y=v.a,w=function(e){var t=e.token,n=e.page,r=void 0===n?1:n,a=e.perPage,o=void 0===a?25:a,s=e.orderBy,i=void 0===s?"id":s;return y.request({url:"/api/v1/binary/modules",method:"get",params:{page:r,per_page:o,order_by:i},headers:{Authorization:"Token ".concat(t)}})},k={namespaced:!0,modules:{modules:{namespaced:!0,state:{modules:[]},mutations:{setLoading:function(e,t){e.isLoading=t},setModules:function(e,t){e.modules=t},setModuleDetails:function(e,t){var n=t.id,r=t.details;e.modules_details.set(n,r)},addLoadingDetails:function(e,t){e.modules_isLoading_details.push(t)},removeLoadingDetails:function(e,t){e.modules_isLoading_details.splice(e.modules_isLoading_details.indexOf(t),1)},addDeleting:function(e,t){e.modules_isDeleting.push(t)},removeDeleting:function(e,t){e.modules_isDeleting.splice(e.modules_isDeleting.indexOf(t),1)}},actions:{getModules:function(){var e=Object(g.a)(regeneratorRuntime.mark(function e(t){var n,r,a,o,s,i,u=arguments;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(n=t.state,r=t.commit,a=t.rootState,o=u.length>1&&void 0!==u[1]?u[1]:{},!n.isLoading){e.next=4;break}return e.abrupt("return",!1);case 4:return e.prev=4,r("setLoading",!0),e.next=8,w(Object(h.a)({},o,{token:a.token}));case 8:return s=e.sent,i=s.data.data,r("setModules",i),e.abrupt("return",i);case 14:e.prev=14,e.t0=e.catch(4);case 16:return e.prev=16,r("setLoading",!1),e.finish(16);case 19:case"end":return e.stop()}},e,this,[[4,14,16,19]])}));return function(t){return e.apply(this,arguments)}}(),deleteModule:function(){var e=Object(g.a)(regeneratorRuntime.mark(function e(t){var n,r,a,o;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(n=t.state,r=t.commit,a=t.rootState,!n.isLoading){e.next=3;break}return e.abrupt("return",!1);case 3:return e.prev=3,r("setLoading",!0),e.next=7,w({token:a.token});case 7:return o=e.sent,e.abrupt("return",o);case 11:e.prev=11,e.t0=e.catch(3);case 13:return e.prev=13,r("setLoading",!1),e.finish(13);case 16:case"end":return e.stop()}},e,this,[[3,11,13,16]])}));return function(t){return e.apply(this,arguments)}}()}}}},A=function(e){var t=e.username,n=e.password;return y.request({url:"/api/v1/auth/login",method:"post",data:{username:t,password:n}})},L=function(){return y.request({url:"/api/v1/auth/logout",method:"post"})},x=function(e){var t=e.username,n=e.password,r=e.passwordConfirm,a=e.email;return y.request({url:"/api/v1/auth/register",method:"post",data:{username:t,email:a,password:n,passwordConfirm:r}})},I=function(e){var t=e.token;return y.request({url:"/api/v1/user",method:"get",headers:{Authorization:"Token ".concat(t)}})},S=n(39),M=n.n(S),P="binspdt.user.remember_me",T="binspdt.user.token",R=function(){return"true"===M.a.get(P)},E=function(e){return M.a.set(P,e)},C=function(e){arguments.length>1&&void 0!==arguments[1]&&!arguments[1]?sessionStorage.setItem(T,e):localStorage.setItem(T,e)},N=function(){sessionStorage.removeItem(T),localStorage.removeItem(T)},O={namespaced:!0,modules:{user:{namespaced:!0,state:{token:function(){return sessionStorage.getItem(T)||localStorage.getItem(T)}()||null,username:"",email:"",lastLogin:"",rememberMe:!1!==R(),isLoading:!1},mutations:{setToken:function(e,t){e.token=t,null===t?N():C(t,e.rememberMe)},setUsername:function(e,t){e.username=t},setEmail:function(e,t){e.email=t},setLastLogin:function(e,t){e.lastLogin=t},setIsLoading:function(e,t){e.isLoading=t},setRememberMe:function(e,t){e.rememberMe=t,E(t)}},actions:{login:function(){var e=Object(g.a)(regeneratorRuntime.mark(function e(t,n){var r,a,o,s;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return r=t.commit,a=n.username,o=n.password,e.prev=2,r("setIsLoading",!0),e.next=6,A({username:a,password:o});case 6:return s=e.sent,r("setUsername",s.data.username),r("setToken",s.data.token),e.abrupt("return",s);case 12:throw e.prev=12,e.t0=e.catch(2),e.t0;case 15:return e.prev=15,r("setIsLoading",!1),e.finish(15);case 18:case"end":return e.stop()}},e,this,[[2,12,15,18]])}));return function(t,n){return e.apply(this,arguments)}}(),logout:function(){var e=Object(g.a)(regeneratorRuntime.mark(function e(t){var n,r;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return n=t.commit,e.prev=1,n("setIsLoading",!0),e.next=5,L();case 5:return r=e.sent,n("setUsername",""),n("setToken",null),n("setEmail",""),n("setLastLogin",""),e.abrupt("return",r);case 13:throw e.prev=13,e.t0=e.catch(1),e.t0;case 16:return e.prev=16,n("setIsLoading",!1),e.finish(16);case 19:case"end":return e.stop()}},e,this,[[1,13,16,19]])}));return function(t){return e.apply(this,arguments)}}(),getUserInfo:function(){var e=Object(g.a)(regeneratorRuntime.mark(function e(t){var n,r,a;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(n=t.state,r=t.commit,t.getters.isLogined){e.next=3;break}return e.abrupt("return",!1);case 3:return e.prev=3,r("setIsLoading",!0),e.next=7,I({token:n.token});case 7:return a=e.sent,r("setUsername",a.data.username),r("setEmail",a.data.email),r("setLastLogin",a.data.lastLogin),e.abrupt("return",a);case 14:throw e.prev=14,e.t0=e.catch(3),e.t0;case 17:return e.prev=17,r("setIsLoading",!1),e.finish(17);case 20:case"end":return e.stop()}},e,this,[[3,14,17,20]])}));return function(t){return e.apply(this,arguments)}}(),register:function(){var e=Object(g.a)(regeneratorRuntime.mark(function e(t,n){var r;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,x(n);case 2:return r=e.sent,e.abrupt("return",r);case 4:case"end":return e.stop()}},e,this)}));return function(t,n){return e.apply(this,arguments)}}()},getters:{isLogined:function(e){return Boolean(e.token)}}}}};r.a.use(p.a);var D=new p.a.Store({modules:{binary:k,website:O}});var j=n(27),q=n.n(j);n(121);r.a.use(m.a);var B=new m.a({mode:"history",linkActiveClass:"active",routes:f});!function(e){e.beforeEach(function(e,t,n){var r=D.getters["website/user/isLogined"];e.matched.some(function(e){return e.meta.requiresAuth})?r?n():n({name:"login",query:{redirect:e.fullPath}}):!r||"login"!==e.name&&"register"!==e.name?n():n({name:"dashboard"})})}(B),function(e){q.a.configure({showSpinner:!1}),e.beforeEach(function(e,t,n){e.path!==t.path&&q.a.start(),n()}),e.afterEach(function(){q.a.done()})}(B);var F=B,H=n(41),U={buttons:{submit:"Submit",refresh:"Refresh",remove:"Remove",details:"Details"},status:{loading:"Loading...",importing:"Importing...",analysing:"Analysing...",executing:"Executing...",error:"Error"},messages:{title:{info:"Info",success:"Success",warning:"Warning",error:"Error"}},routes:{home:"Home",modules:"Modules",binary:"Binary Code",source:"Source Code",analysis:"Analysis",results:"Analysis Results",api:"API",basic_block:"Basic Block"},home:{welcome:"Welcome to BINSPDT",fullname:"BINary Software Plagiarism Detection Tool",lang:"Language"},binary:{modules:{title:"Binary Modules",import_button:"Import idb File",table:{id:"ID",name:"Name",architecture:"Architecture",import_time:"Import Time",exporter:"Exporter",base_address:"Base Address",md5:"MD5",sha1:"SHA1",functions_count:"Functions Count",basic_blocks_count:"Basic Blocks Count",instructions_count:"Instructions Count",operation:"Operation"},select:{module_1:"Module 1",module_2:"Module 2",module_1_placeholder:"Please select module 1",module_2_placeholder:"Please select module 2"},messages:{get_success:"Module loaded successfully",get_error:"Error occurs when loading modules",import_success:"Module imported successfully",import_error:"Error occurs when importing module",remove_confirm:"Confirm to remove module {name} ?",remove_success:"Removed module {name}",remove_error:"Removeing module {name}",details_success:"Loaded details of module {name}",details_error:"Loading details of module {name}"}},analysis:{api:{title:"API Similarity Analysis",select_modules_hint:"Choose two modules to calculate their API similarity",call_depth:"Call Depth [k]",call_depth_hint:"Set the call depth (k) of API birthmarking [default 2]",match_algorithm:"Match Algorithm",match_algorithm_hint:"Set the algorithm for matching similar functions [default KM]",result:{overall_similarity:"Overall Similarity",functions_with_api_count:"Number of Functions with API calls in k call depth",similar_functions:"Similar Functions",function_api:"API calls of Function in Module [{module}]"}},messages:{start:"Analysis started.",pending:"Analysis is in progress...",done:"Analysis finished. Go to the [Result] panel to check the result.",error:"Error occurs when starting analysis."}},results:{title:"Results of Similarity Analysis",table:{id:"ID",type:"Type",module_1:"Module 1",module_2:"Module 2",status:"Status",created_at:"Create Time",finished_at:"Finish Time",operation:"Operation"},status:{pending:"Analysing",done:"Finished"},messages:{get_success:"Loaded list of analysis results",get_error:"Loading list of analysis results",details_success:"Loaded details of result {name}",details_error:"Loading details of result {name}",close_confirm:"Confirm to close? (Remember to save it)"},result:{title:"Analysis Result",save:"Save",close:"Close",similarity:"Similarity",module_details:"Module {name} Details",module_function_address:"Function Address of Module {name}"}}}},z={buttons:{submit:"提交",refresh:"刷新",remove:"移除",details:"详情"},status:{loading:"加载中...",importing:"导入中...",analysing:"分析中...",executing:"处理中...",error:"错误"},messages:{title:{info:"消息",success:"成功",warning:"警告",error:"错误"}},routes:{home:"主页",binary:"目标代码",source:"源代码",modules:"模块",analysis:"分析",results:"分析结果",api:"API",basic_block:"基本块"},home:{welcome:"欢迎使用BINSPDT",fullname:"BINary Software Plagiarism Detection Tool",lang:"语言"},binary:{modules:{title:"二进制文件模块",import_button:"导入idb文件",table:{id:"ID",name:"模块名称",architecture:"架构",import_time:"导入时间",exporter:"导出工具",base_address:"起始地址",md5:"MD5",sha1:"SHA1",functions_count:"函数数量",basic_blocks_count:"基本块数量",instructions_count:"指令数量",operation:"操作"},select:{module_1:"模块1",module_2:"模块2",module_1_placeholder:"请选择模块1",module_2_placeholder:"请选择模块2"},messages:{get_success:"模块加载成功",get_error:"加载模块时发生错误",import_success:"模块导入成功",import_error:"导入模块时发生错误",remove_confirm:"确认要删除该模块{name}吗？",remove_success:"移除模块{name}成功",remove_error:"移除模块{name}失败",details_success:"读取模块{name}详情成功",details_error:"读取模块{name}详情失败"}},analysis:{api:{title:"API相似性分析",select_modules_hint:"选择两个模块，计算它们的API相似性",call_depth:"调用深度[k]",call_depth_hint:"设定API Birthmarking的调用深度(k) [默认值 2]",match_algorithm:"匹配算法",match_algorithm_hint:"设定相似函数的整体匹配算法 [默认值 KM]",result:{overall_similarity:"整体相似度",functions_with_api_count:"在调用深度k以内存在API调用的函数数量",similar_functions:"相似函数",function_api:"模块[{module}]中函数的API调用"}},messages:{start:"分析已开始",pending:"分析正在进行中...",done:"分析已完成，前往[结果]面板查看分析结果",error:"启动分析时发生错误"}},results:{title:"相似性分析结果",table:{id:"ID",type:"类型",module_1:"模块 1",module_2:"模块 2",status:"状态",created_at:"创建时间",finished_at:"完成时间",operation:"操作"},status:{pending:"分析中",done:"已完成"},messages:{get_success:"获取分析结果列表成功",get_error:"获取分析结果列表失败",details_success:"获取分析结果{name}详情成功",details_error:"获取分析结果{name}详情失败",close_confirm:"确认关闭吗？（记得保存结果）"},result:{title:"分析结果",save:"保存",close:"关闭",similarity:"相似度",module_details:"模块 {name} 详情",module_function_address:"模块 {name} 函数地址"}}}};r.a.use(H.a);var $=new H.a({locale:"en",fallbackLocale:"zh",messages:{en:U,zh:z}}),X=n(69);n(122),n(123);r.a.prototype.$adminlte={init:X.a};var V=n(70);r.a.use(V.a,{delay:1e3});var W=n(6),J=n(28);W.c.add(J.a,J.b,J.c);var K=n(0);W.c.add(K.a,K.b,K.c,K.d,K.e,K.f,K.g,K.h,K.j,K.i,K.k,K.l,K.m,K.n,K.o,K.p,K.q,K.r,K.s);var G=n(71);r.a.component("FaIcon",G.a);var Q=n(72);r.a.use(Q.a,{componentName:"VueNotification"}),r.a.config.productionTip=!1,new r.a({el:"#app",router:F,store:D,i18n:$,render:function(e){return e(d)}})},69:function(e,t,n){"use strict";(function(e){function r(){e(window).trigger("load"),e(window).trigger("resize")}n.d(t,"a",function(){return r})}).call(this,n(17))}});