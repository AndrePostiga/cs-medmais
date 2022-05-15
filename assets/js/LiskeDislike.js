// Contructor function
// Partes comentadas são adicionadas automaticamente pela palavra new
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

module.exports = LikeDislike;
