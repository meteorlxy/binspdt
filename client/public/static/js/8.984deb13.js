(window.webpackJsonp=window.webpackJsonp||[]).push([[8],{181:function(e,o,t){},195:function(e,o,t){"use strict";var n=t(181);t.n(n).a},197:function(e,o,t){"use strict";t.r(o);var n=t(54),s=t(37),a={name:"BoxInfo",props:{bg:{type:String,required:!1,default:"info"},icon:{type:[String,Boolean,Array],required:!1,default:!1}},computed:{className:function(){return"bg-".concat(this.bg)}}},i=t(4),c=Object(i.a)(a,function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("div",{staticClass:"info-box"},[t("span",{staticClass:"info-box-icon elevation-1",class:e.className},[e._t("icon",[e.icon?t("FaIcon",{attrs:{icon:e.icon}}):e._e()])],2),e._v(" "),t("div",{staticClass:"info-box-content"},[t("span",{staticClass:"info-box-text"},[e._t("text")],2),e._v(" "),t("span",{staticClass:"info-box-number"},[e._t("number")],2)])])},[],!1,null,null,null);c.options.__file="BoxInfo.vue";var l={name:"TheModulesBox",components:{BoxInfo:c.exports},computed:Object(n.a)({},Object(s.d)("binary/modules",["isLoading","modules"]))},r=Object(i.a)(l,function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("BoxInfo",{staticClass:"box-link",attrs:{bg:"info",icon:"cubes"}},[t("template",{slot:"text"},[e._v("\n    Modules\n  ")]),e._v(" "),t("template",{slot:"number"},[t("FaIcon",{directives:[{name:"show",rawName:"v-show",value:e.isLoading,expression:"isLoading"}],attrs:{icon:"spinner",spin:""}}),e._v(" "),t("span",{directives:[{name:"show",rawName:"v-show",value:!e.isLoading,expression:"!isLoading"}]},[e._v("\n      "+e._s(e.modules.count)+"\n    ")])],1)],2)},[],!1,null,null,null);r.options.__file="TheModulesBox.vue";var u={name:"DashboardHome",components:{TheModulesBox:r.exports}},d=(t(195),Object(i.a)(u,function(){var e=this.$createElement,o=this._self._c||e;return o("div",{staticClass:"row"},[o("div",{staticClass:"col-12 col-sm-6"},[o("RouterLink",{attrs:{to:{name:"dashboard.modules"}}},[o("TheModulesBox")],1)],1),this._v(" "),o("div",{staticClass:"col-12 col-sm-6"},[o("RouterLink",{attrs:{to:{name:""}}})],1)])},[],!1,null,"c52cd44c",null));d.options.__file="Home.vue";o.default=d.exports}}]);