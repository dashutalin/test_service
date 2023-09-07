from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Group, Set, Answer, Question


class SetListView(ListView):
    model = Set
    template_name = 'question/set_list.html'


class GroupListView(ListView):
    model = Group
    template_name = 'tests/group_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['set_name'] = self.set
        return context

    def get_queryset(self):
        self.set = get_object_or_404(
            Set, slug=self.kwargs['set_name'])
        return Group.objects.select_related(
            'set').filter(
            set=self.set.id)


def question_view(request, set_name, group_name):
    template_name = 'question/desc_question.html'
    context = {}
    context['group'] = get_object_or_404(
        Group, slug=group_name)
    context['count'] = Question.objects.select_related(
        'group').filter(group__slug=group_name).count()
    queryset = Question.objects.select_related(
        'group').filter(group__slug=group_name)
    request.session['queryset'] = [q.id for q in queryset]
    request.session['question_index'] = 0
    request.session['answers'] = 0
    return render(request, template_name, context)


@login_required(login_url='login')
def question_from_view(request, group_name, pk):
    last = False
    q_id = request.session['queryset'][pk]
    answers = Answer.objects.filter(question=q_id)
    question = Question.objects.get(pk=q_id)
    request.session['question_index'] += 1
    q_index = request.session['question_index']
    if q_index == len(request.session['queryset']):
        last = True
    right_ans = Answer.objects.filter(
            question=request.session['queryset'][pk-1], is_right=True)
    list_answers = [ans.ans for ans in right_ans]
    if request.method == 'POST':
        ans = request.POST.getlist('answer')
        if ans == list_answers:
            request.session['answers'] += 1
    return render(request, 'question/question_card.html',
                  {'quest': question, 'answers': answers,
                   'last': last, 'q_index': q_index,
                   'group_name': group_name})


@login_required(login_url='login')
def res(request):
    if request.method == 'POST':
        ans = request.POST.getlist('answer')
        pk = request.session['queryset'][-1]
        list_answers = [ans.ans for ans in
                        Answer.objects.filter(question=pk, is_right=True)]
        if ans == list_answers:
            request.session['answers'] += 1
    res = request.session['answers']
    amount = len(request.session['queryset'])
    return render(request, 'question/result.html',
                  {'res': res, 'amount': amount,
                   'percent': (res / amount * 100)})
