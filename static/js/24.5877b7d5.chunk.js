(window.webpackJsonp=window.webpackJsonp||[]).push([[24],{1038:function(e,t,a){"use strict";var n=a(133);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var l=n(a(0)),c=(0,n(a(134)).default)(l.default.createElement("path",{d:"M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"}),"Mail");t.default=c},1039:function(e,t,a){"use strict";var n=a(133);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var l=n(a(0)),c=(0,n(a(134)).default)(l.default.createElement("path",{d:"M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"}),"Phone");t.default=c},1062:function(e,t,a){"use strict";a.r(t);var n=a(28),l=a(29),c=a(31),r=a(30),i=a(32),o=a(0),s=a.n(o),u=a(14),m=(a(71),a(192)),d=a(228),f=a(168),g=a.n(f),p=a(19),h=a(1038),E=a.n(h),v=a(1039),b=a.n(v),k=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(c.a)(this,Object(r.a)(t).call(this,e))).state={},a}return Object(i.a)(t,e),Object(l.a)(t,[{key:"componentWillMount",value:function(){}},{key:"render",value:function(){return s.a.createElement("div",{className:" "},s.a.createElement("div",{className:"mobile_header_sdk_img"},s.a.createElement("svg",{xmlns:"https://www.w3.org/2000/svg",viewBox:"0 0 1418 995",id:"svg-icon"},s.a.createElement("defs",null,s.a.createElement("clipPath",{id:"clip-path"},s.a.createElement("rect",{id:"Rectangle_696","data-name":"Rectangle 696",className:"cls-1",width:"1418",height:"995",transform:"translate(502)"}))),s.a.createElement("g",{id:"Mask_Group_36","data-name":"Mask Group 36",className:"cls-2",transform:"translate(-502)"},s.a.createElement("path",{id:"Path_546","data-name":"Path 546",className:"cls-3",d:"M3690.005,707.591c133.569,324.227,422.867,194.932,474.868,344.832s-34.88,420.957,447.224,625.954,468.65,145.523,468.65,145.523-28.86-370.6,111.43-621.966-116.268-156.175-44.342-331.1S5091.89,707.666,5126.521,653.2s-274.385,42.715-356.968-32.25,50.616,8.33-303.69-13.883-58.607-24.989-338.322-22.212S3556.437,383.365,3690.005,707.591Z",transform:"translate(-3235.185 -479.435) rotate(-4)"})))),s.a.createElement(m.a,null),s.a.createElement("div",{className:" flex-column justify-center items-center relative flex",style:{flexGrow:1,zIndex:1}},s.a.createElement("div",{className:"contact-us-logo"},s.a.createElement("img",{src:g.a}),s.a.createElement("h1",null,p.a)),s.a.createElement("div",{className:"contact-us-details"},s.a.createElement("h3",null,s.a.createElement(E.a,null)," support@myweblink.store"),s.a.createElement("h3",null,s.a.createElement(b.a,null)," +91 70034 42036"),s.a.createElement("h3",null,"Onkar Bearing Co , No 38/1 Laxmipura , Vaderahalli -Sakalvara Road , Anekal Taluk , Bangalore -560083"))),s.a.createElement(d.a,null))}}]),t}(o.Component);t.default=Object(u.c)(function(e){return{}},function(e){return{}})(k)},170:function(e,t,a){},177:function(e,t,a){},192:function(e,t,a){"use strict";a.d(t,"a",function(){return v});var n=a(28),l=a(29),c=a(31),r=a(30),i=a(32),o=a(0),s=a.n(o),u=(a(14),a(45)),m=(a(71),a(170),a(232)),d=a.n(m),f=a(1051),g=a(20),p=a(145),h=a(19),E=[{link:"/",text:"Home"},{link:"/#products",text:"Products"},{link:"/#pricing",text:"Pricing"}],v=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(c.a)(this,Object(r.a)(t).call(this,e))).toggleDrawer=function(e,t){return function(e){("keydown"!==e.type||"Tab"!==e.key&&"Shift"!==e.key)&&a.Toggle()}},a.Toggle=function(){a.setState({toggle:!a.state.toggle})},a.list=function(e){return s.a.createElement("ul",{className:"nav-links pa0"},E.map(function(e,t){return s.a.createElement("li",{key:t,onClick:function(){return a.setState({toggle:!1})}},s.a.createElement("a",{href:e.link},e.text))}),a.state.mobileView?a.state.loggedIn?s.a.createElement("li",null,s.a.createElement("a",{onClick:function(){return g.c.dispatch(Object(u.a)("/admin"))}},"Go To My Account")):s.a.createElement("div",null,s.a.createElement("li",null,s.a.createElement("a",{onClick:function(){return g.c.dispatch(Object(u.a)("/signup"))}},"Get Started")),s.a.createElement("li",null,s.a.createElement("a",{onClick:function(){return g.c.dispatch(Object(u.a)("/login"))}},"Login"))):null)},a.state={toggle:!1,mobileView:!0,loggedIn:!1,navBgStyle:null},a.path="",a}return Object(i.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){window.addEventListener("resize",this.resize.bind(this)),this.resize(),this.props.loggedIn&&this.setState({loggedIn:this.props.loggedIn}),window.localStorage.getItem(h.j)?this.setState({loggedIn:!0}):this.setState({loggedIn:!1})}},{key:"resize",value:function(){this.setState({mobileView:window.innerWidth<=600})}},{key:"render",value:function(){return s.a.createElement(s.a.Fragment,null,s.a.createElement("div",{className:"navBar items-center ",style:this.state.navBgStyle},s.a.createElement("div",{className:"flex"},s.a.createElement(p.a,{parent:"landing-page"}),this.state.mobileView?null:this.list()),s.a.createElement("div",{className:"flex"},this.state.mobileView?s.a.createElement("button",{onClick:this.Toggle,className:"drawer-btn   "},s.a.createElement(d.a,{style:{color:"black"}})):s.a.createElement("div",{className:"flex align-center justify-center"},this.state.loggedIn?s.a.createElement("button",{onClick:function(){return g.c.dispatch(Object(u.a)("/admin"))},type:"button",className:"  nav-btn center "},"Go To My Account"):s.a.createElement("div",{className:"flex"},s.a.createElement("button",{onClick:function(){return g.c.dispatch(Object(u.a)("/signup"))},type:"button",className:" nav-btn  "},"Get Started"),s.a.createElement("button",{onClick:function(){return g.c.dispatch(Object(u.a)("/login"))},type:"button",className:"nav-btn "},"Login")))),s.a.createElement(f.a,{anchor:"top",open:this.state.toggle,onClose:this.toggleDrawer("right",!1),className:"",style:{width:window.innerWidth}},s.a.createElement("div",{className:"drawer"},s.a.createElement(p.a,{parent:"landing-page"}),this.list("right")))))}}]),t}(o.Component)},228:function(e,t,a){"use strict";var n=a(28),l=a(29),c=a(31),r=a(30),i=a(32),o=a(0),s=a.n(o),u=a(14),m=(a(71),a(45)),d=(a(177),a(20)),f=a(145),g=a(229),p=a.n(g),h=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(c.a)(this,Object(r.a)(t).call(this,e))).state={loggedIn:!1},a}return Object(i.a)(t,e),Object(l.a)(t,[{key:"componentWillMount",value:function(){}},{key:"componentWillReceiveProps",value:function(e){}},{key:"render",value:function(){return s.a.createElement("footer",{className:"footer"},s.a.createElement("div",{className:"tc flex flex-column items-center justify-center"},s.a.createElement("div",{className:"footer-logo"},s.a.createElement(f.a,{parent:"landing-page"})),s.a.createElement("div",{className:"flex items-center justify-center ma2 "},s.a.createElement("a",{href:"https://www.instagram.com/myweblink/"},s.a.createElement(p.a,{style:{background:"#0095f6",color:"white",padding:"3px"}}))),s.a.createElement("p",{className:"mb0 mt0 b"},"support@myweblink.store")),s.a.createElement("div",{className:"footer-links tc"},s.a.createElement("ul",null,s.a.createElement("li",null,s.a.createElement("a",{onClick:function(){return d.c.dispatch(Object(m.a)("/faqs"))}},"FAQs")),s.a.createElement("li",null,s.a.createElement("a",{onClick:function(){return d.c.dispatch(Object(m.a)("/terms-and-conditions"))}},"Terms & Conditions")),s.a.createElement("li",null,s.a.createElement("a",{onClick:function(){return d.c.dispatch(Object(m.a)("/privacy-policy"))}},"Privacy Policy")),s.a.createElement("li",null,s.a.createElement("a",{onClick:function(){return d.c.dispatch(Object(m.a)("/refund-policy/"))}},"Refund Policy")),s.a.createElement("li",null,s.a.createElement("a",null,"Help & Support")),s.a.createElement("li",null,s.a.createElement("a",{onClick:function(){return d.c.dispatch(Object(m.a)("/contact-us/"))}},"Contact Us"))),s.a.createElement("h3",{style:{color:"#0095f6"},className:"i mb0 pb0"},"Handcrafted In India!")))}}]),t}(o.Component);t.a=Object(u.c)(function(e){return{}},function(e){return{}})(h)},229:function(e,t,a){"use strict";var n=a(133);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var l=n(a(0)),c=(0,n(a(134)).default)(l.default.createElement("path",{d:"M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2m-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.39 5.61 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.61 18.39 4 16.4 4H7.6m9.65 1.5a1.25 1.25 0 0 1 1.25 1.25A1.25 1.25 0 0 1 17.25 8 1.25 1.25 0 0 1 16 6.75a1.25 1.25 0 0 1 1.25-1.25M12 7a5 5 0 0 1 5 5 5 5 0 0 1-5 5 5 5 0 0 1-5-5 5 5 0 0 1 5-5m0 2a3 3 0 0 0-3 3 3 3 0 0 0 3 3 3 3 0 0 0 3-3 3 3 0 0 0-3-3z"}),"Instagram");t.default=c}}]);
//# sourceMappingURL=24.5877b7d5.chunk.js.map