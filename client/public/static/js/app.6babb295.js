!function(e){function t(t){for(var n,s,o=t[0],u=t[1],l=t[2],c=0,m=[];c<o.length;c++)s=o[c],a[s]&&m.push(a[s][0]),a[s]=0;for(n in u)Object.prototype.hasOwnProperty.call(u,n)&&(e[n]=u[n]);for(d&&d(t);m.length;)m.shift()();return i.push.apply(i,l||[]),r()}function r(){for(var e,t=0;t<i.length;t++){for(var r=i[t],n=!0,s=1;s<r.length;s++){var u=r[s];0!==a[u]&&(n=!1)}n&&(i.splice(t--,1),e=o(o.s=r[0]))}return e}var n={},s={10:0},a={10:0},i=[];function o(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,o),r.l=!0,r.exports}o.e=function(e){var t=[];s[e]?t.push(s[e]):0!==s[e]&&{3:1,4:1,5:1,7:1}[e]&&t.push(s[e]=new Promise(function(t,r){for(var n="static/css/"+e+".styles."+{1:"cddc8fce",2:"d83c2ffc",3:"cfc84b7d",4:"6faf9acc",5:"31917cb6",6:"853a2b83",7:"6a2ab057"}[e]+".css",s=o.p+n,a=document.getElementsByTagName("link"),i=0;i<a.length;i++){var u=(c=a[i]).getAttribute("data-href")||c.getAttribute("href");if("stylesheet"===c.rel&&(u===n||u===s))return t()}var l=document.getElementsByTagName("style");for(i=0;i<l.length;i++){var c;if((u=(c=l[i]).getAttribute("data-href"))===n||u===s)return t()}var d=document.createElement("link");d.rel="stylesheet",d.type="text/css",d.onload=t,d.onerror=function(t){var n=t&&t.target&&t.target.src||s,a=new Error("Loading CSS chunk "+e+" failed.\n("+n+")");a.request=n,r(a)},d.href=s,document.getElementsByTagName("head")[0].appendChild(d)}).then(function(){s[e]=0}));var r=a[e];if(0!==r)if(r)t.push(r[2]);else{var n=new Promise(function(t,n){r=a[e]=[t,n]});t.push(r[2]=n);var i,u=document.getElementsByTagName("head")[0],l=document.createElement("script");l.charset="utf-8",l.timeout=120,o.nc&&l.setAttribute("nonce",o.nc),l.src=function(e){return o.p+"static/js/"+({}[e]||e)+"."+{1:"cddc8fce",2:"d83c2ffc",3:"cfc84b7d",4:"6faf9acc",5:"31917cb6",6:"853a2b83",7:"6a2ab057"}[e]+".js"}(e),i=function(t){l.onerror=l.onload=null,clearTimeout(c);var r=a[e];if(0!==r){if(r){var n=t&&("load"===t.type?"missing":t.type),s=t&&t.target&&t.target.src,i=new Error("Loading chunk "+e+" failed.\n("+n+": "+s+")");i.type=n,i.request=s,r[1](i)}a[e]=void 0}};var c=setTimeout(function(){i({type:"timeout",target:l})},12e4);l.onerror=l.onload=i,u.appendChild(l)}return Promise.all(t)},o.m=e,o.c=n,o.d=function(e,t,r){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},o.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(o.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)o.d(r,n,function(t){return e[t]}.bind(null,n));return r},o.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="/",o.oe=function(e){throw console.error(e),e};var u=window.webpackJsonp=window.webpackJsonp||[],l=u.push.bind(u);u.push=t,u=u.slice();for(var c=0;c<u.length;c++)t(u[c]);var d=l;i.push([140,9,8,0]),r()}({140:function(e,t,r){"use strict";r.r(t);r(266);var n=r(0),s={name:"TheHeader"},a=(r(256),r(35)),i={name:"App",components:{TheHeader:Object(a.a)(s,function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("ElHeader",{staticClass:"header"},[r("h1",{staticClass:"brand"},[r("router-link",{attrs:{to:"/"}},[e._v("\n      BINSPDT\n    ")])],1),e._v(" "),r("nav",{staticClass:"nav"},[r("ElMenu",{attrs:{mode:"horizontal","default-active":"/"+e.$route.path.split("/")[1],router:!0}},[r("ElMenuItem",{attrs:{index:"/"}},[e._v(e._s(e.$t("routes.home")))]),e._v(" "),r("ElMenuItem",{attrs:{index:"/binary"}},[e._v(e._s(e.$t("routes.binary")))]),e._v(" "),r("ElMenuItem",{attrs:{index:"/source"}},[e._v(e._s(e.$t("routes.source")))])],1)],1)])},[],!1,null,"2f54f9f0",null).exports}},o=(r(254),Object(a.a)(i,function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("ElContainer",{attrs:{direction:"vertical"}},[t("TheHeader"),this._v(" "),t("transition",{attrs:{name:"el-fade-in-linear",mode:"out-in"}},[t("router-view",{staticClass:"main-container"})],1)],1)],1)},[],!1,null,null,null).exports),u=r(86);n.default.use(u.a);var l=new u.a({routes:[{path:"/",name:"home",component:function(){return r.e(7).then(r.bind(null,282))}},{path:"/binary",name:"binary",redirect:{name:"binary.modules"},component:function(){return r.e(6).then(r.bind(null,284))},children:[{path:"/binary/modules",name:"binary.modules",component:function(){return Promise.all([r.e(0),r.e(5)]).then(r.bind(null,283))}},{path:"/binary/results",name:"binary.results",component:function(){return Promise.all([r.e(0),r.e(4)]).then(r.bind(null,278))}},{path:"/binary/analysis/api",name:"binary.analysis.api",component:function(){return r.e(3).then(r.bind(null,281))}}]},{path:"/source",name:"source",redirect:{name:"source.modules"},component:function(){return r.e(2).then(r.bind(null,280))},children:[{path:"/source/modules",name:"source.modules",component:function(){return r.e(1).then(r.bind(null,279))}}]}]}),c=r(50),d=(r(139),r(138),r(87),r(16)),m=(r(244),r(121),r(239),r(28)),p=r.n(m),f=document.head.querySelector('meta[name="csrf_token"]');p.a.defaults.headers.common["X-Requested-With"]="XMLHttpRequest",p.a.defaults.headers.common["X-CSRFToken"]=f.content,p.a.defaults.xsrfCookieName="csrftoken",p.a.defaults.xsrfHeaderName="X-CSRFToken";var g=p.a,h={binary:{modules:{index:function(){return"/api/binary/modules"},import:function(e){return"/api/binary/modules/v/".concat(e)},details:function(e){return"/api/binary/modules/".concat(e)},delete:function(e){return"/api/binary/modules/".concat(e)},load:function(e){return"/api/binary/modules/".concat(e,"/load")}},analysis:{api:function(){return"/api/binary/analysis/api"}},results:{index:function(){return"/api/binary/results"},details:function(e){return"/api/binary/results/".concat(e)}}}},_=r(85),b=r(36),y=r(136),v=r.n(y),x=Object(b.a)({},v.a,{buttons:{submit:"Submit",refresh:"Refresh",remove:"Remove",details:"Details"},status:{loading:"Loading...",importing:"Importing...",analysing:"Analysing...",executing:"Executing..."},messages:{title:{info:"Info",success:"Success",warning:"Warning",error:"Error"}},routes:{home:"Home",modules:"Modules",binary:"Binary Code",source:"Source Code",analysis:"Analysis",results:"Analysis Results",api:"API",basic_block:"Basic Block"},home:{welcome:"Welcome to BINSPDT",fullname:"BINary Software Plagiarism Detection Tool",lang:"Language"},binary:{modules:{title:"Binary Modules",import_button:"Import idb File",table:{id:"ID",name:"Name",architecture:"Architecture",import_time:"Import Time",exporter:"Exporter",base_address:"Base Address",md5:"MD5",sha1:"SHA1",functions_count:"Functions Count",basic_blocks_count:"Basic Blocks Count",instructions_count:"Instructions Count",operation:"Operation"},select:{module_1:"Module 1",module_2:"Module 2",module_1_placeholder:"Please select module 1",module_2_placeholder:"Please select module 2"},messages:{get_success:"Module loaded successfully",get_error:"Error occurs when loading modules",import_success:"Module imported successfully",import_error:"Error occurs when importing module",remove_confirm:"Confirm to remove module {name} ?",remove_success:"Removed module {name}",remove_error:"Removeing module {name}",details_success:"Loaded details of module {name}",details_error:"Loading details of module {name}"}},analysis:{api:{title:"API Similarity Analysis",select_modules_hint:"Choose two modules to calculate their API similarity",call_depth:"Call Depth [k]",call_depth_hint:"Set the call depth (k) of API birthmarking [default 2]",match_algorithm:"Match Algorithm",match_algorithm_hint:"Set the algorithm for matching similar functions [default KM]",result:{overall_similarity:"Overall Similarity",function_num:"Number of Functions"}},messages:{start:"Analysis started.",pending:"Analysis is in progress...",done:"Analysis finished. Go to the [Result] panel to check the result.",error:"Error occurs when starting analysis."}},results:{title:"Results of Similarity Analysis",table:{id:"ID",type:"Type",module_1:"Module 1",module_2:"Module 2",status:"Status",created_at:"Create Time",finished_at:"Finish Time",operation:"Operation"},status:{pending:"Analysing",done:"Finished"},messages:{get_success:"Loaded list of analysis results",get_error:"Loading list of analysis results",details_success:"Loaded details of result {name}",details_error:"Loading details of result {name}"}}}}),w=r(84),L=r.n(w),k=Object(b.a)({},L.a,{buttons:{submit:"提交",refresh:"刷新",remove:"移除",details:"详情"},status:{loading:"加载中...",importing:"导入中...",analysing:"分析中...",executing:"处理中..."},messages:{title:{info:"消息",success:"成功",warning:"警告",error:"错误"}},routes:{home:"主页",binary:"目标代码",source:"源代码",modules:"模块",analysis:"分析",results:"分析结果",api:"API",basic_block:"基本块"},home:{welcome:"欢迎使用BINSPDT",fullname:"BINary Software Plagiarism Detection Tool",lang:"语言"},binary:{modules:{title:"二进制文件模块",import_button:"导入idb文件",table:{id:"ID",name:"模块名称",architecture:"架构",import_time:"导入时间",exporter:"导出工具",base_address:"起始地址",md5:"MD5",sha1:"SHA1",functions_count:"函数数量",basic_blocks_count:"基本块数量",instructions_count:"指令数量",operation:"操作"},select:{module_1:"模块1",module_2:"模块2",module_1_placeholder:"请选择模块1",module_2_placeholder:"请选择模块2"},messages:{get_success:"模块加载成功",get_error:"加载模块时发生错误",import_success:"模块导入成功",import_error:"导入模块时发生错误",remove_confirm:"确认要删除该模块{name}吗？",remove_success:"移除模块{name}成功",remove_error:"移除模块{name}失败",details_success:"读取模块{name}详情成功",details_error:"读取模块{name}详情失败"}},analysis:{api:{title:"API相似性分析",select_modules_hint:"选择两个模块，计算它们的API相似性",call_depth:"调用深度[k]",call_depth_hint:"设定API Birthmarking的调用深度(k) [默认值 2]",match_algorithm:"匹配算法",match_algorithm_hint:"设定相似函数的整体匹配算法 [默认值 KM]",result:{overall_similarity:"整体相似度",function_num:"函数/方法数量"}},messages:{start:"分析已开始",pending:"分析正在进行中...",done:"分析已完成，前往[结果]面板查看分析结果",error:"启动分析时发生错误"}},results:{title:"相似性分析结果",table:{id:"ID",type:"类型",module_1:"模块 1",module_2:"模块 2",status:"状态",created_at:"创建时间",finished_at:"完成时间",operation:"操作"},status:{pending:"分析中",done:"已完成"},messages:{get_success:"获取分析结果列表成功",get_error:"获取分析结果列表失败",details_success:"获取分析结果{name}详情成功",details_error:"获取分析结果{name}详情失败"}}}});n.default.use(_.a);var D,M,P,A=new _.a({locale:"en",fallbackLocale:"zh",messages:{en:x,zh:k}}),S=r(2),I=r.n(S),T={namespaced:!0,state:{modules:[],modules_details:new Map,isLoading:!1,modules_isLoading_details:[],modules_isDeleting:[]},mutations:{setLoading:function(e,t){e.isLoading=t},setModules:function(e,t){e.modules=t},setModuleDetails:function(e,t){var r=t.id,n=t.details;e.modules_details.set(r,n)},addLoadingDetails:function(e,t){e.modules_isLoading_details.push(t)},removeLoadingDetails:function(e,t){e.modules_isLoading_details.splice(e.modules_isLoading_details.indexOf(t),1)},addDeleting:function(e,t){e.modules_isDeleting.push(t)},removeDeleting:function(e,t){e.modules_isDeleting.splice(e.modules_isDeleting.indexOf(t),1)}},actions:{get:(P=Object(d.a)(regeneratorRuntime.mark(function e(t){var r,n,s,a,i,o=arguments;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(r=t.state,n=t.commit,s=!(o.length>1&&void 0!==o[1])||o[1],!r.isLoading){e.next=4;break}return e.abrupt("return",!1);case 4:return e.prev=4,n("setLoading",!0),e.next=8,g.get(h.binary.modules.index());case 8:return a=e.sent,i=a.data.data,n("setModules",i),s&&S.Message.success(A.t("binary.modules.messages.get_success")),e.abrupt("return",i);case 15:e.prev=15,e.t0=e.catch(4),s&&S.Message.error(A.t("binary.modules.messages.get_error"));case 18:return e.prev=18,n("setLoading",!1),e.finish(18);case 21:case"end":return e.stop()}},e,this,[[4,15,18,21]])})),function(e){return P.apply(this,arguments)}),details:(M=Object(d.a)(regeneratorRuntime.mark(function e(t,r){var n,s,a,i;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(n=t.state,s=t.commit,!n.modules_isLoading_details.includes(r)){e.next=3;break}return e.abrupt("return",!1);case 3:if(!n.modules_details.has(r)){e.next=5;break}return e.abrupt("return",n.modules_details.get(r));case 5:return e.prev=5,s("addLoadingDetails",r),e.next=9,g.get(h.binary.modules.details(r));case 9:return a=e.sent,i=a.data.data,s("setModuleDetails",{id:r,details:i}),S.Notification.success({title:A.t("messages.title.success"),message:A.t("binary.modules.messages.details_success",{name:"[".concat(r,"]")})}),e.abrupt("return",i);case 16:e.prev=16,e.t0=e.catch(5),S.Notification.error({title:A.t("messages.title.error"),message:A.t("binary.modules.messages.details_error",{name:"[".concat(r,"]")})});case 19:return e.prev=19,s("removeLoadingDetails",r),e.finish(19);case 22:case"end":return e.stop()}},e,this,[[5,16,19,22]])})),function(e,t){return M.apply(this,arguments)}),delete:(D=Object(d.a)(regeneratorRuntime.mark(function e(t,r){var n,s,a,i;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(n=t.state,s=t.commit,a=t.dispatch,!n.modules_isDeleting.includes(r)){e.next=3;break}return e.abrupt("return",!1);case 3:return e.prev=3,s("addDeleting",r),e.next=7,g.delete(h.binary.modules.delete(r));case 7:return i=e.sent,S.Notification.success({title:A.t("messages.title.success"),message:A.t("binary.modules.messages.remove_success",{name:"[".concat(r,"]")})}),a("get",!1),e.abrupt("return",i);case 13:e.prev=13,e.t0=e.catch(3),S.Notification.error({title:A.t("messages.title.error"),message:A.t("binary.modules.messages.remove_error",{name:"[".concat(r,"]")})});case 16:return e.prev=16,s("removeDeleting",r),e.finish(16);case 19:case"end":return e.stop()}},e,this,[[3,13,16,19]])})),function(e,t){return D.apply(this,arguments)})}},O=(r(137),{namespaced:!0,modules:{modules:T,results:{namespaced:!0,state:{results:[],count:0,numPages:1,page:1,perPage:20,isLoading:!1,isLoadingDetails:!1},mutations:{setResults:function(e,t){e.results=t.data,e.count=t.count,e.numPages=t.num_pages,e.page=t.page,e.perPage=t.per_page},setLoading:function(e,t){e.isLoading=t},setLoadingDetails:function(e,t){e.isLoadingDetails=t}},actions:{get:function(){var e=Object(d.a)(regeneratorRuntime.mark(function e(t,r){var n,s,a,i,o,u,l,c;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(n=t.state,s=t.commit,a=r.page,i=void 0===a?1:a,o=r.perPage,u=void 0===o?20:o,!n.isLoading){e.next=4;break}return e.abrupt("return",!1);case 4:return e.prev=4,s("setLoading",!0),e.next=8,g.get(h.binary.results.index(),{params:{page:i,per_page:u}});case 8:return l=e.sent,c=l.data.data,s("setResults",c),S.Notification.success({title:A.t("messages.title.success"),message:A.t("binary.results.messages.get_success")}),e.abrupt("return",c);case 15:e.prev=15,e.t0=e.catch(4),S.Notification.error({title:A.t("messages.title.error"),message:A.t("binary.results.messages.get_error")});case 18:return e.prev=18,s("setLoading",!1),e.finish(18);case 21:case"end":return e.stop()}},e,this,[[4,15,18,21]])}));return function(t,r){return e.apply(this,arguments)}}(),details:function(){var e=Object(d.a)(regeneratorRuntime.mark(function e(t,r){var n,s,a,i;return regeneratorRuntime.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(n=t.state,s=t.commit,n.results.find(function(e){return e.id===r}).finished_at){e.next=3;break}return e.abrupt("return",!1);case 3:if(!n.isLoadingDetails){e.next=5;break}return e.abrupt("return",!1);case 5:return e.prev=5,s("setLoadingDetails",r),e.next=9,g.get(h.binary.results.details(r));case 9:return a=e.sent,i=a.data.data,S.Notification.success({title:A.t("messages.title.success"),message:A.t("binary.results.messages.details_success",{name:"[".concat(r,"]")})}),e.abrupt("return",i);case 15:throw e.prev=15,e.t0=e.catch(5),S.Notification.error({title:A.t("messages.title.error"),message:A.t("binary.results.messages.details_error",{name:"[".concat(r,"]")})}),e.t0;case 19:return e.prev=19,s("setLoadingDetails",!1),e.finish(19);case 22:case"end":return e.stop()}},e,this,[[5,15,19,22]])}));return function(t,r){return e.apply(this,arguments)}}()}}}});n.default.use(c.a);var R=new c.a.Store({modules:{binary:O}}),E=r(135),N=r.n(E),C={formatDateTime:function(e){return N()(e,"YYYY-MM-DD HH:mm:ss")}};r(145);n.default.use(I.a,{i18n:function(e,t){return A.t(e,t)}});r(143);n.default.config.productionTip=!1,n.default.prototype.$api=h,n.default.prototype.$axios=g,n.default.prototype.$helpers=C,new n.default({el:"#app",router:l,store:R,i18n:A,render:function(e){return e(o)}})},143:function(e,t,r){},254:function(e,t,r){"use strict";var n=r(48);r.n(n).a},256:function(e,t,r){"use strict";var n=r(49);r.n(n).a},48:function(e,t,r){},49:function(e,t,r){}});