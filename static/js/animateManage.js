/**
 ************************************************************
 * @project 動畫管理 (Animate Manage)
 * @author XinLiang
 * @Mail 939898101@qq.com
 * @ver version 1.0
 * @time 2013-12-18
 * @Copyright : BSD License
 ************************************************************
 */

; (function (window, document, undefined) {

    var   _aniQueue = [],//動畫佇列
        _baseUID = 0,//元素的UID基礎值
        _aniUpdateTimer = 13, //動畫更新的時間
        _aniID = -1 ,//檢測的進程ID
        isTicking = false;//檢測狀態

    /*
    * optios參數
    * context --- 被操作的元素上下文
    * effect --- 動畫效果的演算法
    * time --- 效果的持續時間
    * starCss --- 元素的起始偏移量
    * css --- 元素的結束值偏移量
    * */
    window.animateManage = function( optios ) {
        this.context =  optios;//目前物件
    }

    animateManage.prototype = {

        init : function( ){//初始化方法
            this.start(this.context);
        },

        stop : function(_e){//停止動畫
            clearInterval(_aniID);
            isTicking = false;
        },

        start : function(optios){//開始動畫
           if(optios) this.pushQueue(optios);//填充佇列屬性
           if(isTicking || _aniQueue.length === 0) return false;
           this.tick();
           return true;
        },

        tick : function(){ //動畫檢測
            var self = this;
            isTicking = true;
            _aniID = setInterval(function(){
                if(_aniQueue.length === 0) {
                    self.stop();
                }
                else{
                    var i = 0,
                        _aniLen = _aniQueue.length
                        ;
                    for(; i < _aniLen ; i++){
                        _aniQueue[i] && self.go(_aniQueue[i], i);
                    }
                }
            }, _aniUpdateTimer)

        },

        go : function(_options, i){//執行具體的動畫作業
            var n = this.now(),
                st = _options.startTime,
                ting = _options.time,
                e = _options.context,
                t = st + ting,
                name = _options.name,
                tPos = _options.value,
                sPos = _options.startValue,
                effect = _options.effect,
                scale = 1;

            if(n >=  t){//如果目前的時間 > 開始時間+結束時間則停止目前動畫
                _aniQueue[i] = null;
                this.delQueue();
            }
            else{
                tPos = this.aniEffect({
                    e:e,
                    ting :ting ,
                    n :n ,
                    st :st ,
                    sPos:sPos,
                    tPos:tPos
                },effect)
            }
            e.style[name] = name == "zIndex" ? tPos : tPos + "px";
            this.goCallBack(_options.callback, _options.uid);//是否執行回呼函數
        },

        aniEffect : function(_options, effect){//動畫效果,感興趣的朋友可以擴展一下動畫演算法
             effect = effect || "linear";
             var _effect ={
                 "linear":function(__options){//線性運動
                     var scale = (__options.n - __options.st)/__options.ting,
                         tPos = __options.sPos + (__options.tPos - __options.sPos)*scale;
                     return tPos;
                 }
             }
            return _effect[effect](_options);
        },

        goCallBack : function(callback, u){//回檔
            var i = 0,
                _aniLen = _aniQueue.length,
                isCallback = true;
            for(; i < _aniLen ; i++){
                if(_aniQueue[i].uid == u){
                    isCallback = false;
                }
            }
            if(isCallback){
                callback && callback();
            }
        },

        pushQueue : function(options){ //壓入執行動畫佇列
            var con =  options.context,
                t =  options.time || 1000,
                callback =  options.callback,
                effect =  options.effect,
                starCss =  options.starCss,
                c =  options.css,
                name = "",
                u = this.setUID(con)
            ;
            for(name in c){
                _aniQueue.push({
                    "context" : con,
                    "time" : t,
                    "name" : name,
                    "value":parseInt(c[name], 10),
                    "startValue":parseInt((starCss[name] || 0)),
                    "effect":effect,
                    "uid" : u,
                    "callback":callback,
                    "startTime" : this.now()
                })
            }
        },

        delQueue : function(){//刪除動畫佇列中指定的動畫
            var i = 0,//尋找到指定動畫佇列，將其刪除
                l = _aniQueue.length;
            for(; i < l; i++ ){
                if(_aniQueue[i] === null) _aniQueue.splice(i, 1);
            }
        },

        now : function(){//獲取現在時間
           return new Date().getTime();
        },

        getUID : function(_e){//獲取元素的UID
            return _e.getAttribute("aniUID");
        },

        setUID : function(_e, _v){//設定元素的UID
            var u = this.getUID(_e);

            if(u) return  u;//如果存在UID則直接返回

            u = _v || _baseUID++;//生成UID
            _e.setAttribute("aniUID", u);
            return u;
        }

    };

})(window, document)
