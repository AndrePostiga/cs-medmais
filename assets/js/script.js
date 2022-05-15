/// <reference path="../../typings/globals/jquery/index.d.ts" />

$(document).ready(function () {

    function LikeDislike(idLike, idDislike, btnLike, btnDislike) {
        // this = {};
        // this.__proto__ = LikeDislike.prototype;
        this.Like = idLike;
        this.Dislike = idDislike;
        this.BtnLike = btnLike;
        this.BtnDislike = btnDislike;
        //return this;
    }

    LikeDislike.prototype.ToogleLike = function () {
        let like = $(this.Like).data("like");
        let dislike = $(this.Dislike).data("dislike");

        let graphLike = $(this.BtnLike).find("i");
        if (graphLike.hasClass("far") == true) {
            like = parseInt(like) + 1;
            graphLike.removeClass("far");
            graphLike.addClass("fas");

            $(this.BtnDislike + " > i").hasClass("fas") ? dislike = parseInt(dislike) - 1 : dislike;
            $(this.BtnDislike + " > i").removeClass("fas");
            $(this.BtnDislike + " > i").addClass("far");
        }
        else {
            like = parseInt(like) - 1;
            graphLike.removeClass("fas");
            graphLike.addClass("far");
        }

        $(this.Like).data("like", like);
        $(this.Dislike).data("dislike", dislike);
        $(this.Like).text(like);
        $(this.Dislike).text(dislike);
    }

    LikeDislike.prototype.ToogleDislike = function () {
        let like = $(this.Like).data("like");
        let dislike = $(this.Dislike).data("dislike");

        let graphDislike = $(this.BtnDislike).find("i");
        if (graphDislike.hasClass("far") == true) {
            dislike = parseInt(dislike) + 1;
            graphDislike.removeClass("far");
            graphDislike.addClass("fas");

            $(this.BtnLike + " > i").hasClass("fas") ? like = parseInt(like) - 1 : like;
            $(this.BtnLike + " > i").removeClass("fas");
            $(this.BtnLike + " > i").addClass("far");
        }
        else {
            dislike = parseInt(dislike) - 1;
            graphDislike.removeClass("fas");
            graphDislike.addClass("far");
        }

        $(this.Like).data("like", like);
        $(this.Dislike).data("dislike", dislike);
        $(this.Like).text(like);
        $(this.Dislike).text(dislike);
    }

    $("#like-produtos-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-produtos", "#dislike-produtos", "#like-produtos-btn", "#dislike-produtos-btn");
        likeDislikeSystem.ToogleLike();
    });

    $("#dislike-produtos-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-produtos", "#dislike-produtos", "#like-produtos-btn", "#dislike-produtos-btn");
        likeDislikeSystem.ToogleDislike();
    });

    $("#like-recolhimento-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-recolhimento", "#dislike-recolhimento", "#like-recolhimento-btn", "#dislike-recolhimento-btn");
        likeDislikeSystem.ToogleLike();
    });

    $("#dislike-recolhimento-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-recolhimento", "#dislike-recolhimento", "#like-recolhimento-btn", "#dislike-recolhimento-btn");
        likeDislikeSystem.ToogleDislike();
    });

    $("#like-entrega-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-entrega", "#dislike-entrega", "#like-entrega-btn", "#dislike-entrega-btn");
        likeDislikeSystem.ToogleLike();
    });

    $("#dislike-entrega-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-entrega", "#dislike-entrega", "#like-entrega-btn", "#dislike-entrega-btn");
        likeDislikeSystem.ToogleDislike();
    });

    $("#like-pesquisa-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-pesquisa", "#dislike-pesquisa", "#like-pesquisa-btn", "#dislike-pesquisa-btn");
        likeDislikeSystem.ToogleLike();
    });

    $("#dislike-pesquisa-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-pesquisa", "#dislike-pesquisa", "#like-pesquisa-btn", "#dislike-pesquisa-btn");
        likeDislikeSystem.ToogleDislike();
    });

    $("#like-consultoria-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-consultoria", "#dislike-consultoria", "#like-consultoria-btn", "#dislike-consultoria-btn");
        likeDislikeSystem.ToogleLike();
    });

    $("#dislike-consultoria-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-consultoria", "#dislike-consultoria", "#like-consultoria-btn", "#dislike-consultoria-btn");
        likeDislikeSystem.ToogleDislike();
    });

    $("#like-equipamentos-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-equipamentos", "#dislike-equipamentos", "#like-equipamentos-btn", "#dislike-equipamentos-btn");
        likeDislikeSystem.ToogleLike();
    });

    $("#dislike-equipamentos-btn").click(function () {
        let likeDislikeSystem = new LikeDislike("#like-equipamentos", "#dislike-equipamentos", "#like-equipamentos-btn", "#dislike-equipamentos-btn");
        likeDislikeSystem.ToogleDislike();
    });
});