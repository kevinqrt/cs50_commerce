from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Product, Bid, Comment
from django.utils import timezone


def index(request):

    return render(request, "auctions/index.html", {
        "products": Product.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def listing(request):

    if request.user is None:
        return render(request, "auctions/login.html", {
            "product": newProduct
        })
    # get data from form
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        imageURL = request.POST["imageURL"]
        minStartBid = request.POST["minStartBid"]
        category = request.POST["category"]
        expiration_date = request.POST["expiration_date"]

        # check user
        currentUser = request.user

        # create new object from model
        newProduct = Product(
            title=title,
            imageURL=imageURL,
            description=description,
            minStartBid=minStartBid,
            category=category,
            expiration_date=expiration_date,
            owner=currentUser
        )
        newProduct.save()

        return render(request, "auctions/entry.html", {
            "product": newProduct
        })

    return render(request, "auctions/create_listing.html", {

    })


def entry(request, id):

    productDATA = Product.objects.get(pk=id)
    isProductinWatchlist = request.user in productDATA.watchlist.all()
    seller = request.user

    # return product id in URL
    return render(request, "auctions/entry.html", {
        "product": Product.objects.get(pk=id),
        "isProductinWatchlist": isProductinWatchlist,
        "seller": seller,
        "comments": Comment.objects.all().filter(product=productDATA)
    })


def displayWatchlist(request):

    currentUser = request.user
    products = currentUser.productWatchlist.all()
    return render(request, "auctions/index.html", {
        "products": products
    })


def REMOVEwatchlist(request, id):
    productDATA = Product.objects.get(pk=id)
    currentUser = request.user
    productDATA.watchlist.remove(currentUser)

    return HttpResponseRedirect(reverse("entry", args=(id, )))


def ADDwatchlist(request, id):
    productDATA = Product.objects.get(pk=id)
    currentUser = request.user
    productDATA.watchlist.add(currentUser)

    return HttpResponseRedirect(reverse("entry", args=(id, )))


def placeBid(request, id):

    if request.method == "POST":
        ProductDATA = Product.objects.get(pk=id)
        newBid = request.POST.get("Bid")

        if ProductDATA.price is None and float(newBid) > ProductDATA.minStartBid:
            addBid = Bid(user=request.user, bid=newBid, product=ProductDATA)
            addBid.save()
            ProductDATA.price = addBid
            ProductDATA.save()

            return render(request, "auctions/entry.html", {
                "product": Product.objects.get(pk=id),
                "BidPlaced": True,
                "update": True
            })

        elif ProductDATA.price is not None and float(newBid) > ProductData.price.bid:
            addBid = Bid(user=request.user, bid=float(
                newBid), product=ProductDATA)
            addBid.save()
            ProductDATA.price = addBid
            ProductDATA.save()

            return render(request, "auctions/entry.html", {
                "product": Product.objects.get(pk=id),
                "BidPlaced": True,
                "update": True
            })
        else:
            return render(request, "auctions/entry.html", {
                "product": Product.objects.get(pk=id),
                "BidPlaced": True,
                "update": False
            })


def closeListing(request, id):

    ProductDATA = Product.objects.get(pk=id)

    if request.method == "POST":
        ProductDATA.closed = True
        ProductDATA.save()

        return render(request, "auctions/entry.html", {
            "product": Product.objects.get(pk=id)
        })


def addComment(request, id):

    if request.method == "POST":
        ProductDATA = Product.objects.get(pk=id)
        userComment = request.POST.get("Comment")

        # create Comment object
        addComment = Comment(
            user=request.user, field=userComment, product=ProductDATA)
        addComment.save()

        return HttpResponseRedirect(reverse("entry", args=(id, )))


def selectCategory(request):

    if request.method == "POST":

        category = request.POST["category"]

        if category == "All Categorys":
            return render(request, "auctions/index.html", {
                "products": Product.objects.all(),
                "category": category
            })

        return render(request, "auctions/index.html", {
            "products": Product.objects.all().filter(category=category),
            "category": category
        })
