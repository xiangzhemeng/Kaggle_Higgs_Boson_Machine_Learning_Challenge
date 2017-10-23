import numpy as np
from costs import *
from tools import *


"""least_squares_gd"""

def least_squares_gd(y, tx, initial_w, max_iters, gamma):
    if (initial_w is None):
        initial_w = np.zeros(tx.shape[1])
    loss = 0
    w = initial_w
    for n_iter in range(max_iters):
        loss = compute_loss(y, tx, w)
        grad = compute_gradient(y, tx, w)
        w -= gamma * grad
    return w, loss


"""least_squares_sgd"""

def least_squares_sgd(y, tx, initial_w, max_iters, gamma):
    if (initial_w is None):
        initial_w = np.zeros(tx.shape[1])
    loss = 0
    w = initial_w
    batch_size = 1
    for n_iter in range(max_iters):
        for y_batch, tx_batch in batch_iter(y, tx, batch_size = batch_size, num_batches = 1):
            loss = compute_loss(y, tx, w)
            grad = compute_gradient(y_batch, tx_batch, w)
            w -= gamma * grad
    return w, loss


"""least squares"""

def least_squares(y, tx):
    m = tx.T.dot(tx)
    n = tx.T.dot(y)
    w = np.linalg.solve(m, n) #sovle: mX=n --> X
    loss = compute_loss(y, tx, w)
    return w, loss


"""ridge regression"""

def ridge_regression(y, tx, lambda_):
    regularizer = 2 * tx.shape[0] * lambda_ * np.identity(tx.shape[1])
    a = tx.T.dot(tx) + regularizer
    b = tx.T.dot(y)
    w = np.linalg.solve(a, b)
    loss = compute_loss(y, tx, w)
    return w, loss


"""logistic regression"""

def learning_by_gradient_descent(y, tx, w, gamma):
    loss = compute_loss_neg_log_likelihood(y, tx, w)
    grad = tx.T.dot(sigmoid(tx.dot(w)) - y)
    w -= gamma * grad
    return w, loss


def logistic_regression(y, tx, initial_w, max_iters, gamma):
    if (initial_w is None):
        initial_w = np.zeros(tx.shape[1])
    w = initial_w
    losses = []
    threshold = 1e-8

    for iter in range(max_iters):
        # get loss and update w.
        w, loss = learning_by_gradient_descent(y, tx, w, gamma)
        losses.append(loss)
        if len(losses) > 1 and np.abs(losses[-1] - losses[-2]) < threshold:
            break
    return w, loss


"""Regularized Logistic Regression"""

def penalized_logistic_regression(y, tx, w, lambda_):
    loss = compute_loss_neg_log_likelihood(y, tx, w) + lambda_ * np.squeeze(w.T.dot(w))
    gradient = tx.T.dot(sigmoid(tx.dot(w)) - y) + 2 * lambda_ * w

    return loss, gradient

def regularized_logistic_regression(y, tx, lambda_, initial_w, max_iters, gamma):
    if (initial_w is None):
        initial_w = np.zeros(tx.shape[1])

    w = initial_w
    losses = []
    threshold = 1e-8

    for n_iter in range(max_iters):
        # get loss and update w.
        loss, gradient = penalized_logistic_regression(y, tx, w, lambda_)
        w = w - gamma * gradient
        losses.append(loss)
        # Stop criteria
        if len(losses) > 1 and np.abs(losses[-1] - losses[-2]) < threshold:
            break

    return w, losses[-1]
